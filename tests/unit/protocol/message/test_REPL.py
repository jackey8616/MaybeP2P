
class TestREPL:

    def test_handler(self, peer, peerConnection, msgREPL):
        assert msgREPL.handler(peer, peerConnection, None) == False
        assert msgREPL.handler(peer, peerConnection, 'REQ') == True
        assert msgREPL.handler(peer, peerConnection, 'RES') == True
        assert msgREPL.handler(peer, peerConnection, 'FOR') == True

    def test__REQ(self, peer, peerConnection, msgREPL):
        assert msgREPL._REQ(()) == True

    def test__RES(self, peer, peerConnection, msgREPL):
        assert msgREPL._RES(()) == True

    def test__FOR(self, peer, peerConnection, msgREPL):
        assert msgREPL._FOR(()) == True

    def test_packet(self, peer, peerConnection, msgREPL):
        assert msgREPL.packet('REQ', peer, peerConnection) == (len(str(peer.id)), str(peer.id))

