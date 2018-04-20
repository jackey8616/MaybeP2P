import sys, logging, socket, threading, traceback
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
        self.peerInfo = PeerInfo((serverAddr, int(serverPort)), 'Active')
        logging.debug((serverAddr, serverPort))
        self.stopped = False
        self.lock = threading.RLock()

        self.id = str(uuid4())
        self.peers = {}
        self.msgs = queue.Queue()
        logging.info('Inited Peer %s' % self.id)

    def _initServerSock(self):
        try:
            self.serverSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.serverSock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.serverSock.bind(self.peerInfo.addr)
            self.serverSock.listen(5)
            logging.info('Inited server socket')
        except:
            return False
        return True

    def _joinNetFromPeer(self, remotePeerAddr):
        addr = remotePeerAddr.split(':')[0]
        port = int(remotePeerAddr.split(':')[1])
        msgType = 'JOIN'
        msgData ='REQ,%s,%s,%d' % (self.id, self.peerInfo.addr[0], self.peerInfo.addr[1])
        self.sendToPeer(addr, port, msgType, msgData)

    def _syncListFromPeer(self, remoteHost):
        pid = self.getPeerByHost(remoteHost)
        addr = remoteHost.split(':')[0]
        port = int(remoteHost.split(':')[1])
        msgType = 'LIST'
        msgData = 'REQ'
        self.sendToPeer(addr, port, msgType, msgData, pid=pid)

    def __handlePeer(self, clientSock):
        addr, port = clientSock.getpeername()
        peerConn = PeerConnection(None, addr, port, self, clientSock)
        msgType, msgData = peerConn.recvData()
        peerConn.protocol._handlers[msgType].handler(msgData)
        logging.debug((msgType, msgData))
        peerConn.close()

    def run(self):
        while not self.stopped:
            try:
                clientSock, clientAddr = self.serverSock.accept()
                peerConnThread = threading.Thread(target=self.__handlePeer, args=[clientSock])
                peerConnThread.start()
            except KeyboardInterrupt:
                self.stopped = True
                continue
        self.serverSock.close()

    def exit(self):
        self.stopped = True
        #self.sendToNet('QUIT', self.id, waitReply=False)
        self.sendToPeer(self.peerInfo.addr[0], self.peerInfo.addr[1], 'QUIT', self.id, waitReply=False)

    def sendToPeer(self, host, port, msgType, msgData, pid=None, waitReply=True):
        msgReply = []
        try:
            peerConn = PeerConnection(pid, host, port, self)
            peerConn.sendData(msgType, msgData)
        
            if waitReply:
                oneReply = peerConn.recvData()
                while (oneReply != (None,None)):
                    msgReply.append( oneReply )
                    oneReply = peerConn.recvData()
            peerConn.close()
        except Exception as e:
            print(e)
        for each in msgReply:
            peerConn.protocol._handlers[each[0]].handler(each[1])
        return msgReply
    
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

    def getPeerByHost(self, host):
        for (pid, host) in self.peers.items():
            if host == host:
                return pid
        return None

