import sys

from protocol import Protocol
from protocol.classicv1.message import JOIN, LIST, QUIT

names = ''
messages = {}

class ClassicV1(Protocol):

    def __init__(self, peer):
        Protocol.__init__(self, 'ClassicV1', peer)

    def _messageExtand(self):
        extandMessages = {
            'JOIN': JOIN,
            'LIST': LIST,
            'QUIT': QUIT,
        }
        self._messages.update(extandMessages)

    #def _joinNetFromPeer(self, peer, remotePeerAddr):
    #    addr = remotePeerAddr.split(':')[0]
    #    port = int(remotePeerAddr.split(':')[1])
    #    peer.sendProtocolToPeer(addr, port, 'ClassicV1', 'JOIN', 'REQ')

