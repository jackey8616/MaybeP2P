import pytest

class TestPeerInfo:
    pass

class TestPeer:

    def test__initServerHost(self, peer):
        assert peer._initServerHost() == peer.peerInfo.addr[0]

    def test__initServerSock(self, peer):
        peer.listenHost = (None, None)
        assert peer._initServerSock() == False

    def test_run(self, peer):
        pass

    def test_exit(self, peer):
        pass

    def test_sendToPeer(self, peer):
        pass

