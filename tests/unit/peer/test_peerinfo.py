import pytest

from MaybeP2P.peer import PeerInfo

class TestPeerInfo:

    def test_initial(self):
        pi = PeerInfo('pid', ('0.0.0.0', 65535), None, test=123)
        assert pi.test == 123
        assert str(pi) == 'pid'

    def test_pid(self, peerInfo):
        pidtemp = peerInfo.pid
        peerInfo.pid = pidtemp + '1'
        assert peerInfo.pid == pidtemp + '1'

    def test_host(self, peerInfo):
        hosttemp = peerInfo.host
        with pytest.raises(ValueError, message='Host must be a tuple.'):
            peerInfo.host = 123
        with pytest.raises(ValueError, message='Address must be a str.'):
            peerInfo.host = (123, 456)
        with pytest.raises(ValueError, message='Port must be in range of 0 - 65535'):
            peerInfo.host = (hosttemp[0], -1)
            peerInfo.host = (hosttemp[0], 65536)
        peerInfo.host = ('1.1.1.1', 65535)
        assert peerInfo.host == ('1.1.1.1', 65535)
        peerInfo.host = hosttemp

