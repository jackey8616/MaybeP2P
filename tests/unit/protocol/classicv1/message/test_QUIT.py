
class TestQUIT:

    def test_handler(self, peer, peerConnection, msgQUIT):
        assert msgQUIT.handler(peer, peerConnection, None) == False

    def test__REQ(self, peer, peerConnection, msgQUIT):
        assert msgQUIT._REQ(None) == True

    def test__RES(self, peer, peerConnection, msgQUIT):
        assert msgQUIT._RES(None) == True

    def test__FOR(self, peer, peerConnection, msgQUIT):
        assert msgQUIT._FOR(None) == True

