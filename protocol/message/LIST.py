import sys

if sys.version_info > (3, 0):
    from .message import Message
else:
    from message import Message

class LIST(Message):

    def __init__(self, peer, peerConn):
        Message.__init__(self, peer, peerConn)

    def handle(self, msgData):
        try:
            self.peer.lock.acquire()
            if msgData.startwith('REQ'):
                self.__REQ(())
            elif msgData.startwith('RES'):
                self.__RES((msgData[4:].split(',')))
        except Exception as e:
            self.peerConn.sendData('ERRO', e)
        finally:
            self.peer.lock.release()

    def __REQ(self, *data):
        for (pid, host) in self.peer.peers.items():
            if pid != self.peer.id and pid != self.peerConn.id:
                self.peerConn.sendData('LIST', 'RES,%s,%s,%s' % (pid, host[0], host[1]))

    def __RES(self, *data):
        (pid, addr, port), = data
        self.peer.addPeer(pid, addr, port)
        print(self.peer.peers)

