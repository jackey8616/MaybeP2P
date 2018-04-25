
class TestJOIN:

    def test_handler(self, peerConnection, msgJOIN):
        assert msgJOIN.handler(peerConnection, ' , , , ') == False
        assert msgJOIN.handler(peerConnection, None) == False
        
        peerConnection.peer.peers = {}
        assert msgJOIN.handler(peerConnection, 'REQ,123,456,789') == True
        assert msgJOIN.handler(peerConnection, 'REQ,123,456,789') == False

        peerConnection.peer.peers = {}
        assert msgJOIN.handler(peerConnection, 'RES,123,456,789') == True
        assert msgJOIN.handler(peerConnection, 'RES,123,456,789') == False
    
        assert msgJOIN.handler(peerConnection, 'FOR, , , ') == True


    def test__REQ(self, msgJOIN):
        msgJOIN.peerConn.peer.peers = {}
        assert msgJOIN._REQ(('123', '456' ,789)) == True
        assert msgJOIN._REQ(('123', '456', 789)) == False

    def test__RES(self, msgJOIN):
        msgJOIN.peerConn.peer.peers = {}
        assert msgJOIN._RES(('123', '456', 789)) == True
        assert msgJOIN._RES(('123', '456', 789)) == False
    
    def test__FOR(self, msgJOIN):
        assert msgJOIN._FOR((None,None,None)) == True

    def test_pack(self, msgJOIN):
        data = '%s,%s,%s,%s' % ('RES', msgJOIN.peer.id, msgJOIN.peer.peerInfo.addr[0], msgJOIN.peer.peerInfo.addr[1])
        assert msgJOIN.pack('RES') == (len(data), data)

