
from protocol import Protocol
from protocol.kademlia.message import PING, STOR, FNOD, FVAL
from protocol.kademlia.utils import Bukket

class Kademlia(Protocol):

    def __init__(self, peer, k=20, alpha=3):
        Protocol.__init__(self, 'Kademlia', peer)
        self.bukket = Bukket(self, k, alpha)

    def _messageExtand(self):
        extandMessages = {
            'PING': PING,
            'STOR': STOR,
            'FNOD': FNOD,
            'FVAL': FVAL
        }
        self._messages.update(extandMessages)
        return True

    def broadcast(self, message, waitReply=True):
        pass    

    def exit(self):
        pass

