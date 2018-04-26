import sys
import dns.resolver

from protocol import Protocol
from protocol.classicv1.message import JOIN, LIST, QUIT

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
        return True

    def _joinNetFromPeer(self, remotePeerAddr):
        addr = remotePeerAddr.split(':')[0]
        port = int(remotePeerAddr.split(':')[1])
        message = self.JOIN.packWrap('REQ')
        self._peer.sendToPeer(addr, port, message)

    def _joinNetFromDNS(self, remoteDNS):
        peersInDNS = dns.resolver.query(remoteDNS, 'TXT', raise_on_no_answer=True)
        for each in peersInDNS:
            addr, port = str(each)[1:-1].split(':')
            message = self.JOIN.packWrap('REQ')
            self._peer.sendToPeer(addr, port, message)

    def _syncListFromPeer(self, remoteHost):
        addr = remoteHost.split(':')[0]
        port = int(remoteHost.split(':')[1])
        message = self.LIST.packWrap('REQ')
        self._peer.sendToPeer(addr, port, message)

