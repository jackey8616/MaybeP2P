import pytest

from peer import Peer
from protocol.classicv1 import ClassicV1

class TestPeer:

#    @pytest.mark.skip()
    def test_peer(self):
        p = Peer(protocol=ClassicV1)
        assert p.peerInfo.addr[1] == 25565
        p._initServerSock()
        assert p.serverSock
        p.start()

        p2 = Peer(serverPort=25566)
        assert p2.peerInfo.addr[1] == 25566
        p2._initServerSock()
        p2.start()

        p2.ClassicV1._joinNetFromPeer('0.0.0.0:25565')
        p2.ClassicV1._syncListFromPeer('0.0.0.0:25565')

        p.exit()
        p2.exit()
        assert p.stopped
        assert p2.stopped
    
