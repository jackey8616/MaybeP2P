import traceback

from protocol.message import Message

class PONG(Message):

    def __init__(self, peer, peerConn):
        Message.__init__(self, peer, peerConn)

    def handler(self, msgData):
        pass

    def __REQ(self, *data):
        pass

    def __RES(self, *data):
        pass

    @staticmethod
    def packetS(pkType, peer, peerConn):
        data = 'REQ'
        return len(data), data

    def packet(self, pkType, peer, peerConn):
        return PONG.packetS(pkType, peer, peerConn)
