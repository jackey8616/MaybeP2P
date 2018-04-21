import sys

if sys.version_info > (3, 0):
    from .message import Message
else:
    from message import Message

class QUIT(Message):

    def __init__(self, peer, peerConn):
        Message.__init__(self, peer, peerConn)

    def handler(self, msgData):
        try:
            self.peer.lock.acquire()
            pid = msgData
            self.peer.removePeer(pid)
        except Exception as e:
            self.peerConn.sendData('ERRO', e)
        finally:
            self.peer.lock.release()

    def __REQ(self, *data):
        pass

    def __RES(self, *data):
        pass

    @staticmethod
    def packetS(pkType, peer, peerConn):
        data = peer.id
        return len(data), data

    def packet(self, pkType, peer, peerConn):
        return QUIT.packetS(pkType, peer, peerConn)

