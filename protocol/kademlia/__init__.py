
from protocol import Protocol

class Kademlia(Protocol):

    def __init__(self, peer):
        Protocol.__init__(self, 'Kademlia', peer)

