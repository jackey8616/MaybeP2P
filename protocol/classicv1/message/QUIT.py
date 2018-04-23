import sys

from protocol.message import Message

class QUIT(Message):

    def __init__(self):
        Message.__init__(self)

    def handler(self, peer, peerConn, msgData):
        self.peer = peer
        self.peerConn = peerConn

        try:
            self.peer.lock.acquire()
            pid = msgData
            return self.peer.removePeer(pid)
        except Exception as e:
            self.peerConn.sendData('ERRO', e)
        finally:
            self.peer.lock.release()
        return False

    def _REQ(self, *data):
        return True

    def _RES(self, *data):
        return True

    def _FOR(self, *data):
        return True

    @staticmethod
    def packetS(pkType, peer, peerConn):
        data = peer.id
        return len(data), data

    def packet(self, pkType, peer, peerConn):
        return QUIT.packetS(pkType, peer, peerConn)

