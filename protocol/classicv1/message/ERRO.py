import sys, logging

from protocol.message import Message

class ERRO(Message):

    def __init__(self, protoName):
        Message.__init__(self, protoName)

    def handler(self, peer, peerConn, msgData):
        pass

    def _REQ(self, *data):
        pass

    def _RES(self, *data):
        pass

    def _FOR(self, *data):
        pass

    @staticmethod
    def packS(pkType, peer, peerConn):
        pass

    def pack(self, pkType, peerConn):
        return ERRO.packetS(pkType, peerConn.peer, peerConn)

