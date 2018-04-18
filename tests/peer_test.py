import time
from peer import Peer

class TestPeer:

    def test_peer(self):
        p = Peer()
        assert p.serverAddr == ('0.0.0.0', 25565)
        p._initServerSock()
        assert p.serverSock
        p.start()

        p2 = Peer(serverPort=25566)
        p2._initServerSock()
        p2.start()
        p.stopped = True
        p2.stopped = True

        p.broadcastData('Exit')
        p2.broadcastData('Exit', 25566)
        assert p.stopped
        assert p2.stopped
