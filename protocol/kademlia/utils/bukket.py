import uuid

class Bukket:

    def __init__(self, protocol, k=20, alpha=3):
        self.protocol = protocol
        self.k = k
        self.alpha = alpha
        self.kbukket = {}

    def insertNode(self, *nodeInfo):
        addr, port, nodeID = nodeInfo
        d = self.exlusiveOR(nodeID)
        if (addr, port, nodeID) in self.kbukket[d]:
            element = self.kbukket[d].pop(0)
            self.kbukket[d].insert(len(kbukket[d], element))
        elif len(self.kbukket[d]) < self.k:
            self.kbukket[d].insert(len(kbukket[d], (addr, port, nodeID)))
        else:
            element = self.kbukket[d].pop(0)

    def exlusiveOR(self, nodeID):
        return int(uuid.UUID(nodeID).hex, 16) ^ int(uuid.UUID(self.protocol._peer.id).hex, 16)

