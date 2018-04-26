
from protocol import Protocol
from protocol.kademlia.message import PING, PONG

class Kademlia(Protocol):

    def __init__(self, peer):
        Protocol.__init__(self, 'Kademlia', peer)

    def _messageExtand(self):
        extandMessages = {
            'PING': PING,
            'PONG': PONG
        }
        self._messages.update(extandMessages)
        return True

    def broadcast(self, message, waitReply=True):
        pass    

    def exit(self):
        pass

