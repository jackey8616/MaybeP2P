
class Message:

    def __init__(self):
        pass

    def handler(self, peer, peerConn, msgData):
        raise NotImplementedError

    def _REQ(self, *data):
        raise NotImplementedError

    def _RES(self, *data):
        raise NotImplementedError

    def _FOR(self, *data):
        raise NotImplementedError

    @staticmethod
    def wrapperS():
        raise NotImplementedError

    def wrapper(self):
        raise NotImplementedError
