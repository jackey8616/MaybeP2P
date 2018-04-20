from message import Message

class TEST(Message):

    def __init__(self, peer, peerConn):
        self.peer = peer
        self.peerConn = peerConn

    def handle(self, msgData):
        pass

    def __REQ(self, *data):
        pass

    def __RES(self, *data):
        pass 
