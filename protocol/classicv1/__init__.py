import sys

from protocol import Protocol
from protocol.classicv1.message import JOIN, LIST, QUIT

names = ''
messages = {}

class ClassicV1(Protocol):

    def __init__(self, peerConn, peer):
        Protocol.__init__(self, 'ClassicV1', peerConn, peer)

    def _messageExtand(self):
        extandMessages = {
            'JOIN': JOIN,
            'LIST': LIST,
            'QUIT': QUIT,
        }
        self._messages.update(extandMessages)

