import pytest, time

from peer.peer import PeerInfo, Peer

class TestPeerInfo:

    def test_peerInfo(self):
        pi = PeerInfo(('127.0.0.1', 65535), 'Active')
        assert pi.addr == ('127.0.0.1', 65535)
        assert pi.status == 'Active'

class TestPeer:


    @pytest.mark.skip('Temp skip')
    def test_peer(self):
        p = Peer()
        assert p.peerInfo.addr == ('0.0.0.0', 25565)
        p._initServerSock()
        assert p.serverSock
        p.start()

        p2 = Peer(serverPort=25566)
        assert p2.peerInfo.addr == ('0.0.0.0', 25566)
        p2._initServerSock()
        p2.start()

        p.stopped = True
        p2.stopped = True

        p.exit()
        p2.exit()
        assert p.stopped
        assert p2.stopped

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
        pass

    def test_getPeerByHost(self, peer):
        pass

