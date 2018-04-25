
class TestQUIT:

    def test_handler(self, peerConnection, msgQUIT):
        assert msgQUIT.handler(peerConnection, None) == False
        # This statement processed not enough data to raise Exceptions.
        #assert msgQUIT.handler(peer, peerConnection, len()) == False

    def test__REQ(self, peerConnection, msgQUIT):
        assert msgQUIT._REQ(None) == True

    def test__RES(self, peerConnection, msgQUIT):
        assert msgQUIT._RES(None) == True

    def test__FOR(self, peerConnection, msgQUIT):
        assert msgQUIT._FOR(None) == True

    def test_pack(self, peerConnection, msgQUIT):
        assert msgQUIT.pack('RES', peerConnection) == (len(msgQUIT.peerConn.peer.id), msgQUIT.peerConn.peer.id)

