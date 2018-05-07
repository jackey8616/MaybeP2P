
from MaybeP2P.peer import PeerInfo

class TestLIST:

    def test_handler(self, peer, peerConnection, msgLIST):
        assert msgLIST.handler(peerConnection, None) == False

        assert msgLIST.handler(peerConnection, 'REQ') == True

        msgLIST.protocol._peersInfo = {}
        assert msgLIST.handler(peerConnection, 'RES') == False
        data = 'RES,123|0.0.0.0|25565,456|0.0.0.0|25566'
        assert msgLIST.handler(peerConnection, data) == True
        assert msgLIST.protocol._peersInfo['123'].getHost() == ('0.0.0.0', 25565)
        assert msgLIST.protocol._peersInfo['456'].getHost() == ('0.0.0.0', 25566)
 
        assert msgLIST.handler(peerConnection, 'FOR') == True

    def test__REQ(self, peerConnection, msgLIST):
        assert msgLIST._REQ(('REQ')) == True

    def test__RES(self, peerConnection, msgLIST):
        pass

    def test__FOR(self, peerConnection, msgLIST):
        assert msgLIST._FOR(('FOR')) == True

    def test_pack(self, msgLIST):
        pi = PeerInfo('123', ('0.0.0.0', 25565), 'Active')
        msgLIST.protocol._peersInfo = { pi.pid: pi }
        data = 'RES,123|0.0.0.0|25565'
        assert msgLIST.pack('RES') == (len(data), data)

