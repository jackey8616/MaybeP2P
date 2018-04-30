
class TestMESG:

    def test_handler(self, peerConnection, msgMESG):
        assert msgMESG.handler(peerConnection, None) == False
        assert msgMESG.handler(peerConnection, 'REQ,1234') == True
        assert msgMESG.handler(peerConnection, 'RES') == True
        assert msgMESG.handler(peerConnection, 'FOR') == True

    def test__REQ(self, msgMESG):
        assert msgMESG._REQ(None) == True

    def test__RES(self, msgMESG):
        assert msgMESG._RES() == True

    def test__FOR(self, msgMESG):
        assert msgMESG._FOR() == True

    def test_pack(self, msgMESG):
        assert msgMESG.pack('RES', ('1234',)) == (len('RES,1234'), 'RES,1234')

