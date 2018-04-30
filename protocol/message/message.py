
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

    def pack(self, pkType, data=None):
        raise NotImplementedError

    def packWrap(self, pkType, *data):
        dataLen, data = self.pack(pkType, data)
        return self.protocol._wrap((dataLen, self.__class__.__name__, data))

