
class TestJOIN:

    def test_handler(self, peer, peerConnection, msgJOIN):
        assert msgJOIN.handler(peer, peerConnection, ' , , , ') == False
        assert msgJOIN.handler(peer, peerConnection, None) == False
        
    def test__REQ(self, peer, peerConnection, msgJOIN):
        peer.peers = {}
        assert msgJOIN.handler(peer, peerConnection, 'REQ,123,456,789') == True
        assert msgJOIN.handler(peer, peerConnection, 'REQ,123,456,789') == False

    def test__RES(self, peer, peerConnection, msgJOIN):
        peer.peers = {}
        assert msgJOIN.handler(peer, peerConnection, 'RES,123,456,789') == True
        assert msgJOIN.handler(peer, peerConnection, 'RES,123,456,789') == False
    
    def test__FOR(self, peer, peerConnection, msgJOIN):
        assert msgJOIN.handler(peer, peerConnection, 'FOR, , , ') == True

