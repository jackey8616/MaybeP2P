
from MaybeP2P.peer import PeerInfo

class TestPeerInfo:

    def test_initial(self):
        pi = PeerInfo('pid', ('0.0.0.0', 65535), None, test=123)
        assert pi.test == 123
        assert str(pi) == 'pid'
        del pi

