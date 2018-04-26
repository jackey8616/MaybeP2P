import traceback

from protocol.message import Message

class PING(Message):

    def __init__(self, protocol):
        Message.__init__(self, protocol)

    def handler(self, peerConn, msgData):
        return True

    def _REQ(self, *data):
        return True

    def _RES(self, *data):
        return Ture

    def _FOR(self, *date):
        return Ture

    def pack(self, pkType):
        return True 

