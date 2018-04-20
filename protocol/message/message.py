
class Message:

    def __init__(self, peer, peerConn):
        self.peer = peer
        self.peerConn = peerConn

    def handler(self, msgData):
        pass

    def __REQ(self, *data):
        raise NotImplementedError

    def __RES(self, *data):
        raise NotImplementedError

    def encoder(self):
        pass

    def decoder(self):
        pass
