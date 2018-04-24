
class TestLIST:

    def test_handler(self, peer, peerConnection, msgLIST):
        assert msgLIST.handler(peer, peerConnection, None) == False

        assert msgLIST.handler(peer, peerConnection, 'REQ') == True

        peer.peers = {}
        assert msgLIST.handler(peer, peerConnection, 'RES') == False
        data = 'RES,123|456|789,000|111|222'
        assert msgLIST.handler(peer, peerConnection, data) == True
        assert peer.peers['123'] == ('456', 789)
        assert peer.peers['000'] == ('111', 222)
 
        assert msgLIST.handler(peer, peerConnection, 'FOR') == True

    def test__REQ(self, peer, peerConnection, msgLIST):
        assert msgLIST._REQ(('REQ')) == True

    def test__RES(self, peer, peerConnection, msgLIST):
        pass

    def test__FOR(self, peer, peerConnection, msgLIST):
        assert msgLIST._FOR(('FOR')) == True

    def test_packet(self, peer, peerConnection, msgLIST):
        peer.peers = {
            '123': ('456', 789)
        }
        data = 'RES,123|456|789'
        assert msgLIST.packet('RES', peer, peerConnection) == (len(data), data)

