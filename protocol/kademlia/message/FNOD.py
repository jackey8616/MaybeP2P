import traceback

from protocol.message import Message

class FNOD(Message):

    def __init__(self, protocol):
        Message.__init__(self, protocol)

    def handler(self, peerConn, msgData):
        self.peerConn = peerConn
        self.peer = peerConn.peer

        try:
            self.peer.lock.acquire()
            nodeID = msgData
            
            return True
        except Exception as e:
            traceback.print_exc()
        finally:
            self.peer.lock.release()
        return False

    def _REQ(self, *data):
        return True

    def _RES(self, *data):
        return True

    def _FOR(self, *date):
        return True

    def pack(self, pkType):
        data = self.protocol._peer.id
        return (len(data), data)

