import pytest

from MaybeP2P.peer import Peer, PeerInfo, PeerConnection
from MaybeP2P.protocol import Protocol, Message
from MaybeP2P.protocol.message import REPL
from MaybeP2P.protocol.classicv1 import ClassicV1
from MaybeP2P.protocol.classicv1.message import JOIN, LIST, QUIT, ERRO, MESG

@pytest.fixture(scope='module')
def peerInfo():
    pi = PeerInfo(('127.0.0.1', 65535), 'Active')
    return pi

@pytest.fixture(scope='module')
def peer(request):
    p = Peer(serverAddr='0.0.0.0', serverPort=25565)
    p._initServerSock()
    p.start()

    def fin():
        p.exit()
    
    request.addfinalizer(fin)
    return p

@pytest.fixture(scope='module')
def peerConnection(request, peer):
    peerConn = PeerConnection(None, peer, peer.protocol, host=('0.0.0.0', 25565))

    def fin():
        peerConn.exit()

    request.addfinalizer(fin)
    return peerConn

@pytest.fixture(scope='module')
def protocol(peer):
    p = Protocol('name', peer)
    return p

@pytest.fixture(scope='module')
def message():
    m = Message('TestProtocol')
    return m

@pytest.fixture(scope='module')
def classicv1(peer):
    c = ClassicV1(peer)
    return c

@pytest.fixture(scope='module')
def msgJOIN(classicv1):
    j = JOIN(classicv1)
    return j

@pytest.fixture(scope='module')
def msgLIST(classicv1):
    l = LIST(classicv1)
    return l

@pytest.fixture(scope='module')
def msgQUIT(classicv1):
    q = QUIT(classicv1)
    return q
@pytest.fixture(scope='module')
def msgERRO(classicv1):
    e = ERRO(classicv1)
    return e

@pytest.fixture(scope='module')
def msgMESG(classicv1):
    m = MESG(classicv1)
    return m

@pytest.fixture(scope='module')
def msgREPL():
    r = REPL('TestProtocol')
    return r

