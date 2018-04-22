
from classicv1 import ClassicV1

names = ''
messages = {}

class ClassicV2(ClassicV1):

    def __init__(self, peer, peerConn):
        ClassicV1.__init__(self, 'ClassicV2', peer, peerConn)

    def _messageExtand(self):
        extandMessages = {}
        self._messages.update(extandMessages)

