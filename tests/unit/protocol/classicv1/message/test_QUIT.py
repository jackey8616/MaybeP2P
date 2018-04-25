
class TestQUIT:

    def test_handler(self, peerConnection, msgQUIT):
        assert msgQUIT.handler(peerConnection, None) == False
        # This statement processed not enough data to raise Exceptions.
        #assert msgQUIT.handler(None, None) == False

    def test__REQ(self, peerConnection, msgQUIT):
        assert msgQUIT._REQ(None) == True

    def test__RES(self, peerConnection, msgQUIT):
        assert msgQUIT._RES(None) == True

    def test__FOR(self, peerConnection, msgQUIT):
        assert msgQUIT._FOR(None) == True

    def test_pack(self, msgQUIT):
        assert msgQUIT.pack('RES') == (len(msgQUIT.protocol._peer.id), msgQUIT.protocol._peer.id)

