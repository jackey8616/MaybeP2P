import pytest

from MaybeP2P.peer import Peer, PeerConnection
from MaybeP2P.protocol import Protocol
from MaybeP2P.protocol.message import Message
from MaybeP2P.protocol.message import REPL

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

#@pytest.fixture(scope='module')
#def jOIN(peer, peerConnection):
#    joIN = JOIN(peer, peerConnection)
#    return joIN
#
#@pytest.fixture(scope='module')
#def lIST(peer, peerConnection):
#    liST = LIST(peer, peerConnection)
#    return liST
#
#@pytest.fixture(scope='module')
#def qUIT(peer, peerConnection):
#    quIT = QUIT(peer, peerConnection)
#    return quIT

@pytest.fixture(scope='module')
def rEPL(peer, peerConnection):
    rePL = REPL(peer, peerConnection)
    return rePL

