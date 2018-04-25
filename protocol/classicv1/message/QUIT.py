import sys

from protocol.message import Message

class QUIT(Message):

    def __init__(self, protocol):
        Message.__init__(self, protocol)

    def handler(self, peerConn, msgData):
        self.peerConn = peerConn
        self.peer = peerConn.peer

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
    def packS(pkType, peer, peerConn):
        data = peerConn.peer.id
        return len(data), data

    def pack(self, pkType, peerConn):
        return QUIT.packS(pkType, self.peer, peerConn)

