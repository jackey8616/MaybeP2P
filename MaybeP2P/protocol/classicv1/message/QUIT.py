import sys

from ....protocol.message import Message

class QUIT(Message):

    def __init__(self, protocol):
        Message.__init__(self, protocol)

    def handler(self, peerConn, msgData):
        self.peerConn = peerConn
        self.peer = peerConn.peer

        try:
            self.peer.lock.acquire()
            pid = msgData
            return self.protocol.removePeer(pid)
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

    def pack(self, pkType, *data):
        data = str(self.protocol._peer.id)
        return len(data), data

