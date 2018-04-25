import pytest


class TestPeerConnection:

    #def test_sendData(self, peerConnection):
    #    pass
        #assert peerConnection.sendData('TEST', None) == False
        #assert peerConnection.sendData('TEST', 'REQ') == True

    def test_recvData(self, peerConnection):
        temp = peerConnection.sd
        peerConnection.sd = None
        assert peerConnection.recvData() == (None, None, None)
        peerConnection.sd = temp
