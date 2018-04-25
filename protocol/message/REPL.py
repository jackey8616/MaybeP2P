import sys

from protocol.message import Message

class REPL(Message):

    def __init__(self, protoName):
        Message.__init__(self, protoName)

    def handler(self, peer, peerConn, msgData):
        self.peer = peer
        self.peerConn = peerConn

        try:
            self.peer.lock.acquire()
            if msgData.startswith('REQ'):
                return self._REQ((msgData[4:]))
            elif msgData.startswith('RES'):
                return self._REQ((msgData[4:]))
            elif msgData.startswith('FOR'):
                return self._FOR((msgData[4:]))
        except Exception as e:
            print(e)
        finally:
            self.peer.lock.release()
        return False

    def _REQ(self, *data):
        print(data)
        return True

    def _RES(self, *data):
        return True

    def _FOR(self, *data):
        return True

    @staticmethod
    def packetS(pkType, peer, peerConn):
        data = peer.id
        return (len(data), data)

    def packet(self, pkType, peer, peerConn):
        return REPL.packetS(pkType, peer, peerConn)

