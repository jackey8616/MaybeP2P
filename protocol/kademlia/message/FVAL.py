import traceback

from protocol.message import Message

class FVAL(Message):

    def __init__(self, protocol):
        Message.__init__(self, protocol)

    def handler(self, peerConn, msgData):
        return True

    def _REQ(self, *data):
        return True

    def _RES(self, *data):
        return True

    def _FOR(self, *date):
        return True

    def pack(self, pkType):
        return True
