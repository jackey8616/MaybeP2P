
class TestJOIN:

    def test_handler(self, peer, peerConnection, msgJOIN):
        assert msgJOIN.handler(peer, peerConnection, ' , , , ') == False
        assert msgJOIN.handler(peer, peerConnection, None) == False
        
        peer.peers = {}
        assert msgJOIN.handler(peer, peerConnection, 'REQ,123,456,789') == True
        assert msgJOIN.handler(peer, peerConnection, 'REQ,123,456,789') == False

        peer.peers = {}
        assert msgJOIN.handler(peer, peerConnection, 'RES,123,456,789') == True
        assert msgJOIN.handler(peer, peerConnection, 'RES,123,456,789') == False
    
        assert msgJOIN.handler(peer, peerConnection, 'FOR, , , ') == True


    def test__REQ(self, peer, peerConnection, msgJOIN):
        peer.peers = {}
        assert msgJOIN._REQ(('123', '456' ,789)) == True
        assert msgJOIN._REQ(('123', '456', 789)) == False

    def test__RES(self, peer, peerConnection, msgJOIN):
        peer.peers = {}
        assert msgJOIN._RES(('123', '456', 789)) == True
        assert msgJOIN._RES(('123', '456', 789)) == False
    
    def test__FOR(self, peer, peerConnection, msgJOIN):
        assert msgJOIN._FOR((None,None,None)) == True

    def test_packet(self, peer, peerConnection, msgJOIN):
        data = '%s,%s,%s,%s' % ('RES', peer.id, peer.peerInfo.addr[0], peer.peerInfo.addr[1])
        assert msgJOIN.packet('RES', peer, peerConnection) == (len(data), data)

