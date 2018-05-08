import pytest

from MaybeP2P.protocol import Protocol
from MaybeP2P.peer import PeerInfo

class TestProtocol:

    def test_init(self, peer):
        with pytest.raises(ValueError):
            p = Protocol(None, peer)
        with pytest.raises(ValueError):
            p = Protocol('name', None)

    def test_handler(self, protocol):
        assert protocol.handler(None, None, None) == False

    #def test_wrapper(self, protocol):
    #    assert protocol.wrapper(None, None, None) == None

    def test_getPeerInfoBy(self, protocol):
        pi = PeerInfo('123', ('0.0.0.0', 25565), 'Active')
        protocol._peersInfo = { pi.pid: pi }
        assert protocol.getPeerInfoBy(('123')) == (pi.pid, pi)
        assert protocol.getPeerInfoBy(('0.0.0.0:25565')) == (pi.pid, pi)
        assert protocol.getPeerInfoBy(('456')) == (None, None)

    def test_addPeer(self, protocol):
        #protocol._peers = {}
        protocol._peersInfo = {}
        assert protocol.addPeer('000', '111', '222') == True
        assert protocol.addPeer('000', '444', '555') == False

    def test_removePeer(self, protocol):
        pi = PeerInfo('123', ('0.0.0.0', 25565), 'Active')
        pi2 = PeerInfo('456', ('0.0.0.0', 25566), 'Active')
        protocol._peersInfo = { pi.pid: pi, pi2.pid: pi2 }
        assert protocol.removePeer(('789')) == False
        assert protocol.removePeer(('0.0.0.0:25565')) == True
        assert protocol.removePeer(('456')) == True
        assert protocol._peersInfo == {}

    def test_broadcast(self, protocol):
        with pytest.raises(NotImplementedError):
            protocol.broadcast(None)

    def test_exit(self, protocol):
        with pytest.raises(NotImplementedError):
            protocol.exit()

