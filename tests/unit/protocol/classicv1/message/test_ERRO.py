
class TestERRO:

    def test_handler(self, peerConnection, msgERRO):
        assert msgERRO.handler(peerConnection, None) == True

    def test__REQ(self, msgERRO):
        assert msgERRO._REQ(()) == True

    def test__RES(self, msgERRO):
        assert msgERRO._RES(()) == True

    def test__FOR(self, msgERRO):
        assert msgERRO._FOR(()) == True

    def test_pack(self, msgERRO):
        assert msgERRO.pack(None) == (4, 'ERRO')
