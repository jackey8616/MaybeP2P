
class TestJOIN:

    def test_handler(self, peer, peerConnection, msgJOIN):
        assert msgJOIN.handler(peerConnection, ' , , , ') == False
        assert msgJOIN.handler(peerConnection, None) == False
        
        peer.peers = {}
        assert msgJOIN.handler(peerConnection, 'REQ,123,456,789') == True
        assert msgJOIN.handler(peerConnection, 'REQ,123,456,789') == False

        peer.peers = {}
        assert msgJOIN.handler(peerConnection, 'RES,123,456,789') == True
        assert msgJOIN.handler(peerConnection, 'RES,123,456,789') == False
    
        assert msgJOIN.handler(peerConnection, 'FOR, , , ') == True


    def test__REQ(self, peerConnection, msgJOIN):
        msgJOIN.peerConn.peer.peers = {}
        assert msgJOIN._REQ(('123', '456' ,789)) == True
        assert msgJOIN._REQ(('123', '456', 789)) == False

    def test__RES(self, peer, peerConnection, msgJOIN):
        msgJOIN.peerConn.peer.peers = {}
        assert msgJOIN._RES(('123', '456', 789)) == True
        assert msgJOIN._RES(('123', '456', 789)) == False
    
    def test__FOR(self, peer, peerConnection, msgJOIN):
        assert msgJOIN._FOR((None,None,None)) == True

    def test_pack(self, peerConnection, msgJOIN):
        data = '%s,%s,%s,%s' % ('RES', msgJOIN.peer.id, msgJOIN.peer.peerInfo.addr[0], msgJOIN.peer.peerInfo.addr[1])
        assert msgJOIN.pack('RES', peerConnection) == (len(data), data)

