
class TestJOIN:

    def test_handler(self, peerConnection, msgJOIN):
        assert msgJOIN.handler(peerConnection, ' , , , ') == False
        assert msgJOIN.handler(peerConnection, None) == False
        
        msgJOIN.protocol._peers = {}
        assert msgJOIN.handler(peerConnection, 'REQ,123,456,789') == True
        assert msgJOIN.handler(peerConnection, 'REQ,123,456,789') == False

        msgJOIN.protocol._peers = {}
        assert msgJOIN.handler(peerConnection, 'RES,123,456,789') == True
        assert msgJOIN.handler(peerConnection, 'RES,123,456,789') == False
    
        assert msgJOIN.handler(peerConnection, 'FOR, , , ') == True


    def test__REQ(self, msgJOIN):
        msgJOIN.protocol._peers = {}
        assert msgJOIN._REQ(('123', '456' ,789)) == True
        assert msgJOIN._REQ(('123', '456', 789)) == False

    def test__RES(self, msgJOIN):
        msgJOIN.protocol._peers = {}
        assert msgJOIN._RES(('123', '456', 789)) == True
        assert msgJOIN._RES(('123', '456', 789)) == False
    
    def test__FOR(self, msgJOIN):
        assert msgJOIN._FOR((None,None,None)) == True

    def test_pack(self, msgJOIN):
        data = '%s,%s,%s,%d' % ('RES', str(msgJOIN.peer.id), msgJOIN.peer.peerInfo.addr, msgJOIN.peer.peerInfo.port)
        assert msgJOIN.pack('RES') == (len(data), data)

