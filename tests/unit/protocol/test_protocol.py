import pytest

from MaybeP2P.protocol import Protocol

class TestProtocol:

    def test_init(self, peer):
        with pytest.raises(ValueError):
            p = Protocol(None, peer)
        with pytest.raises(ValueError):
            p = Protocol('name', None)

    def test__messageExtand(self, protocol):
        assert protocol._messageExtand() == True

    def test_handler(self, protocol):
        assert protocol.handler(None, None, None) == False

    #def test_wrapper(self, protocol):
    #    assert protocol.wrapper(None, None, None) == None

    def test_getPeerInfoBy(self, protocol):
        protocol._peers = {'000': ('111', 222)}
        assert protocol.getPeerInfoBy(('111', 222)) == ('000', ('111', 222))
        assert protocol.getPeerInfoBy('111:222') == ('000', ('111', 222))
        assert protocol.getPeerInfoBy(('444', 555)) == (None, None) 
 
    def test_addPeer(self, protocol):
        protocol._peers = {}
        assert protocol.addPeer('000', '111', '222') == True
        assert protocol.addPeer('000', '444', '555') == False

    def test_removePeer(self, protocol):
        protocol._peers = {'123': ('456', 789)}
        assert protocol.removePeer('123') == True
        assert protocol.removePeer('123') == False

    def test_broadcast(self, protocol):
        with pytest.raises(NotImplementedError):
            protocol.broadcast(None)

    def test_exit(self, protocol):
        with pytest.raises(NotImplementedError):
            protocol.exit()

