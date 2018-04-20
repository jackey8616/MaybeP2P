import sys, logging

if sys.version_info > (3, 0):
    from .message import Message
else:
    from message import Message

class ERRO(Message):

    def __init__(self, peer, peerConn):
        Message.__init__(self, peer, peerConn)

    def handler(self, msgData):
        pass

    def __REQ(self, *data):
        pass

    def __RES(self, *data):
        pass
