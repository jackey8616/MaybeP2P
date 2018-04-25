
class Message:

    def __init__(self, protocol):
        self.protocol = protocol

    def handler(self, peerConn, msgData):
        raise NotImplementedError

    def _REQ(self, *data):
        raise NotImplementedError

    def _RES(self, *data):
        raise NotImplementedError

    def _FOR(self, *data):
        raise NotImplementedError

    @staticmethod
    def packS(pkType, peerConn):
        raise NotImplementedError

    def pack(self, pkType, peerConn):
        raise NotImplementedError
