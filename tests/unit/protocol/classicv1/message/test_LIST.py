
class TestLIST:

    def test_handler(self, peer, peerConnection, msgLIST):
        assert msgLIST.handler(peerConnection, None) == False

        assert msgLIST.handler(peerConnection, 'REQ') == True

        peer.peers = {}
        assert msgLIST.handler(peerConnection, 'RES') == False
        data = 'RES,123|456|789,000|111|222'
        assert msgLIST.handler(peerConnection, data) == True
        assert peer.peers['123'] == ('456', 789)
        assert peer.peers['000'] == ('111', 222)
 
        assert msgLIST.handler(peerConnection, 'FOR') == True

    def test__REQ(self, peerConnection, msgLIST):
        assert msgLIST._REQ(('REQ')) == True

    def test__RES(self, peerConnection, msgLIST):
        pass

    def test__FOR(self, peerConnection, msgLIST):
        assert msgLIST._FOR(('FOR')) == True

    def test_pack(self, msgLIST):
        msgLIST.protocol._peer.peers = {
            '123': ('456', 789)
        }
        data = 'RES,123|456|789'
        assert msgLIST.pack('RES') == (len(data), data)

