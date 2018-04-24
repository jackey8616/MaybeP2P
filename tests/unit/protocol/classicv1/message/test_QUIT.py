
class TestQUIT:

    def test_handler(self, peer, peerConnection, msgQUIT):
        assert msgQUIT.handler(peer, peerConnection, None) == False
        # This statement processed not enough data to raise Exceptions.
        #assert msgQUIT.handler(peer, peerConnection, len()) == False

    def test__REQ(self, peer, peerConnection, msgQUIT):
        assert msgQUIT._REQ(None) == True

    def test__RES(self, peer, peerConnection, msgQUIT):
        assert msgQUIT._RES(None) == True

    def test__FOR(self, peer, peerConnection, msgQUIT):
        assert msgQUIT._FOR(None) == True

    def test_packet(self, peer, peerConnection, msgQUIT):
        assert msgQUIT.packet('RES', peer, peerConnection) == (len(peer.id), peer.id)

