
class Message:

    def __init__(self, peer, peerConn):
        self.peer = peer
        self.peerConn = peerConn

    def handler(self, msgData):
        raise NotImplementedError

    def __REQ(self, *data):
        raise NotImplementedError

    def __RES(self, *data):
        raise NotImplementedError

    @staticmethod
    def wrapperS():
        raise NotImplementedError

    def wrapper(self):
        raise NotImplementedError
