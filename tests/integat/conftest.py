import pytest

from peer.peer import Peer
from peer.connection import PeerConnection
from protocol import Protocol
from protocol.message import Message
from protocol.message import JOIN, LIST, QUIT, REPL, TEST

@pytest.fixture(scope='module')
def peer(request):
    p = Peer('0.0.0.0', 25565)
    p._initServerSock()
    p.start()

    def fin():
        p.exit()
    
    request.addfinalizer(fin)
    return p

@pytest.fixture(scope='module')
def peerConnection(request, peer):
    peerConn = PeerConnection(None, peer, '0.0.0.0', 25565)

    def fin():
        peerConn.exit()

    request.addfinalizer(fin)
    return peerConn

@pytest.fixture(scope='module')
def protocol(peer, peerConnection):
    p = Protocol('name', peer, peerConnection)
    return p

@pytest.fixture(scope='module')
def message(peer, peerConnection):
    m = Message(peer, peerConnection)
    return m

@pytest.fixture(scope='module')
def jOIN(peer, peerConnection):
    joIN = JOIN(peer, peerConnection)
    return joIN
@pytest.fixture(scope='module')
def lIST(peer, peerConnection):
    liST = LIST(peer, peerConnection)
    return liST

@pytest.fixture(scope='module')
def qUIT(peer, peerConnection):
    quIT = QUIT(peer, peerConnection)
    return quIT

@pytest.fixture(scope='module')
def rEPL(peer, peerConnection):
    rePL = REPL(peer, peerConnection)
    return rePL

@pytest.fixture(scope='module')
def tEST(peer, peerConnection):
    teST = TEST(peer, peerConnection)
    return teST
