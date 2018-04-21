import pytest, time

from peer.peer import PeerInfo, Peer

class TestPeerInfo:

    def test_peerInfo(self):
        pi = PeerInfo(('127.0.0.1', 65535), 'Active')
        assert pi.addr == ('127.0.0.1', 65535)
        assert pi.status == 'Active'

class TestPeer:

    def test__initServerSock(self, peer):
        pass

    def test__joinNetFromPeer(self, peer):
        pass

    def test__syncListFromPeer(self, peer):
        pass

    def test_run(self, peer):
        pass

    def test_exit(self, peer):
        pass

    def test_sendToPeer(self, peer):
        pass

    def test_sendToNet(self, peer):
        pass

    def test_addPeer(self, peer):
        assert peer.addPeer('000', '111', '222') == True
        assert peer.addPeer('000', '444', '555') == False

    def test_getPeerByHost(self, peer):
        assert peer.getPeerByHost(('111', 222)) == '000'
        assert peer.getPeerByHost(('444', 555)) == None

