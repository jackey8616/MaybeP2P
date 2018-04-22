import sys, logging, socket, threading, traceback
import dns.resolver
from uuid import uuid4
if sys.version_info > (3, 0):
    import queue
    from .connection import PeerConnection
else:
    import Queue as queue
    from connection import PeerConnection


class PeerInfo:

    def __init__(self, addr, status):
        self.addr = addr
        self.status = status

class Peer(threading.Thread):

    def __init__(self, serverAddr='0.0.0.0', serverPort=25565):
        threading.Thread.__init__(self)
        self.listenHost = (serverAddr, int(serverPort))
        logging.debug('Listening at %s:%d' % (self.listenHost))

        self.peerInfo = PeerInfo((self._initServerHost(), int(serverPort)), 'Active')
        logging.debug('Link IP: %s' % self.peerInfo.addr[0])
        self.stopped = False
        self.lock = threading.RLock()

        self.id = str(uuid4())
        self.peers = {}
        self.msgs = queue.Queue()
        logging.info('Inited Peer %s' % self.id)

    def _initServerHost(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('www.google.com', 80))
        host = s.getsockname()[0]
        s.close()
        return host

    def _initServerSock(self):
        try:
            self.serverSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.serverSock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.serverSock.bind(self.listenHost)
            self.serverSock.listen(5)
            logging.info('Inited server socket')
        except:
            return False
        return True

    def _joinNetFromPeer(self, remotePeerAddr):
        addr = remotePeerAddr.split(':')[0]
        port = int(remotePeerAddr.split(':')[1])
        self.sendProtocolToPeer(addr, port, 'JOIN', 'REQ')

    def _joinNetFromDNS(self, remoteDNS):
        peersInDNS = dns.resolver.query(remoteDNS, 'TXT', raise_on_no_answer=True)
        for each in peersInDNS:
            addr, port = str(each)[1:-1].split(':')
            self.sendToPeer(addr, port, 'JOIN', 'REQ,%s,%s,%s' % (self.id, self.peerInfo.addr[0], self.peerInfo.addr[1]))

    def _syncListFromPeer(self, remoteHost):
        addr = remoteHost.split(':')[0]
        port = int(remoteHost.split(':')[1])
        self.sendProtocolToPeer(addr, port, 'LIST', 'REQ')

    def run(self):
        while not self.stopped:
            try:
                clientSock, clientAddr = self.serverSock.accept()
                peerConn = PeerConnection(None, self, sock=clientSock)
                peerConn.start()
            except KeyboardInterrupt:
                self.stopped = True
                continue
        self.serverSock.close()

    def exit(self):
        self.stopped = True
        self.sendProtocolToNet('QUIT', 'REQ', waitReply=False)
        self.sendProtocolToPeer(self.listenHost[0], self.listenHost[1], 'QUIT', 'REQ', waitReply=False)

    def sendProtocolToPeer(self, host, port, msgType, pkType, pid=None, waitReply=True):
        msgReply = []
        try:
            peerConn = PeerConnection(pid, self, host, port)
            message = peerConn.protocol.wrapper(msgType, pkType)
            peerConn.sendProtocolData(message)
        
            if waitReply:
                oneReply = peerConn.recvData()
                while (oneReply != (None, None, None)):
                    msgReply.append( oneReply )
                    oneReply = peerConn.recvData()
            peerConn.exit()
        except Exception as e:
            traceback.print_exc()
        for (protoType, msgType, msgData) in msgReply:
            peerConn.protocol._messages[msgType].handler(msgData)
        return msgReply
        
    def sendToPeer(self, host, port, msgType, msgData, pid=None, waitReply=True):
        msgReply = []
        try:
            peerConn = PeerConnection(pid, self, host, port)
            peerConn.sendData(msgType, msgData)
        
            if waitReply:
                oneReply = peerConn.recvData()
                while (oneReply != (None, None, None)):
                    msgReply.append( oneReply )
                    oneReply = peerConn.recvData()
            peerConn.exit()
        except Exception as e:
            traceback.print_exc()
        for each in msgReply:
            peerConn.protocol._messages[each[0]].handler(each[1])
        return msgReply

    def sendProtocolToNet(self, msgType, pkType, waitReply=True):
        netReply = []
        for (pid, host) in self.peers.items():
            print(pid, host)
            netReply.append({ pid: self.sendProtocolToPeer(host[0], host[1], msgType, pkType, pid=pid, waitReply=waitReply) })
        return netReply

    def sendToNet(self, msgType, msgData, waitReply=True):
        netReply = []
        for (pid, host) in self.peers.items():
            netReply.append({ pid: self.sendToPeer(host[0], host[1], msgType, msgData, pid=pid, waitReply=waitReply) })
        return netReply

    def addPeer(self, pid, addr, port):
        if pid not in self.peers:
            self.peers[pid] = (addr, int(port))
            return True
        else:
            return False

    def removePeer(self, pid):
        self.peers.pop(pid, None)

    def getPeerByHost(self, queryHost):
        for (pid, host) in self.peers.items():
            if host == queryHost:
                return pid
        return None

