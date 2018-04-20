import sys

if sys.version_info > (3, 0):
    from .message import Message
else:
    from message import Message

class REPL(Message):

    def __init__(self, peer, peerConn):
        Message.__init__(self, peer, peerConn)

    def handler(self, msgData):
        try:
            self.peer.lock.acquire()
            print(msgData)
        except Exception as e:
            print(e)
        finally:
            self.peer.lock.release()

    def __REQ(self, *data):
        pass

    def __RES(self, *data):
        pass

