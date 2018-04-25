import sys, logging, socket, threading, traceback, copy
from uuid import uuid4

from protocol.classicv1 import ClassicV1
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

        self.protocol = self._initPeerProtocol()
        logging.debug('Protocol loaded.')

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

    def _initPeerProtocol(self):
        setattr(self, 'ClassicV1', ClassicV1(self))
        return {
            'ClassicV1': self.ClassicV1
        }

    def run(self):
        while not self.stopped:
            try:
                clientSock, clientAddr = self.serverSock.accept()
                peerConn = PeerConnection(None, self, self.protocol, sock=clientSock)
                peerConn.start()
            except KeyboardInterrupt:
                self.stopped = True
                continue
        self.serverSock.close()

    def exit(self):
        self.stopped = True
        message = self.ClassicV1.QUIT.packWrap('REQ')
        self.sendToNet(message, waitReply=False)
        self.sendToPeer(self.peerInfo.addr[0], self.peerInfo.addr[1], message, waitReply=False)
        
    def sendToPeer(self, host, port, message, pid=None, waitReply=True):
        msgReply = []
        try:
            peerConn = PeerConnection(pid, self, self.protocol, host, port)
            peerConn.sendData(message)
        
            if waitReply:
                oneReply = peerConn.recvData()
                while (oneReply != (None, None, None)):
                    msgReply.append( oneReply )
                    oneReply = peerConn.recvData()
            peerConn.exit()
        except Exception as e:
            traceback.print_exc()
        for (protoType, msgType, msgData) in msgReply:
            peerConn.protocol[protoType]._messages[msgType].handler(peerConn, msgData)
        return msgReply

    def sendToNet(self, message, waitReply=True):
        netReply = []
        for (pid, host) in self.peers.items():
            netReply.append({ pid: self.sendToPeer(host[0], host[1], message, pid=pid, waitReply=waitReply) })
        return netReply

    def addPeer(self, pid, addr, port):
        if pid not in self.peers:
            self.peers[pid] = (addr, int(port))
            return True
        else:
            return False

    def removePeer(self, pid):
        try:
            self.peers.pop(pid)
            return True
        except:
            return False

    def getPeerByHost(self, queryHost):
        for (pid, host) in self.peers.items():
            if host == queryHost:
                return pid
        return None

