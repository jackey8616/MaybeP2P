from uuid import uuid4
import logging, socket, threading, json
try:
    import Queue as queue
except ImportError:
    import queue

class Peer(threading.Thread):

    def __init__(self, serverAddr='0.0.0.0', serverPort=25565):
        threading.Thread.__init__(self)
        self.uuid = str(uuid4())
        self.stopped = False

        self.serverAddr = (serverAddr, serverPort)
        self.peers = {}
        self.handlers = {}
        self.msgs = queue.Queue()
        logging.debug('Inited Peer {%s}' % self.uuid)

    def _initServerSock(self):
        self.serverSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.serverSock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.serverSock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        self.serverSock.bind(self.serverAddr)

    def _handlePeerConnect(self):
        pass

    def run(self):
        while not self.stopped:
            (data, addr) = self.serverSock.recvfrom(128 * 1024)
            data = json.loads(data.decode())
            if data['uuid_from'] != self.uuid:
                print(data)
        self.serverSock.close()

    def sendData(self, msg, addr):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        if addr[0] == '255.255.255.255':
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        message = json.dumps({
            'uuid_from': self.uuid,
            'data': msg
        })
        sock.sendto(message.encode(), addr)
        sock.close()

    def broadcastData(self, msg, port=25565):
        self.sendData(msg, ('255.255.255.255', port))

