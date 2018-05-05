import sys, copy, traceback
import dns.resolver

from ..protocol import Protocol
from .message import JOIN, LIST, QUIT, MESG

class ClassicV1(Protocol):

    def __init__(self, peer, name='ClassicV1'):
        Protocol.__init__(self, name, peer)

    def _messageExtand(self):
        extandMessages = {
            'JOIN': JOIN,
            'LIST': LIST,
            'QUIT': QUIT,
            'MESG': MESG,
        }
        self._messages.update(extandMessages)
        return True

    def broadcast(self, message, waitReply=False):
        netReply = []
        for (pid, host) in copy.deepcopy(self._peers).items():
            netReply.append({ pid: self._peer.sendToPeer(message, host, pid=pid, waitReply=waitReply) })
        return netReply

    def exit(self):
        try:
            message = self.QUIT.packWrap('REQ')
            self.broadcast(message, waitReply=False)
            self._peer.sendToPeer(message, host=self._peer.peerInfo.getHost(), waitReply=False)
        except:
            traceback.print_exc()

    def _joinNetFromPeer(self, remotePeerAddr):
        message = self.JOIN.packWrap('REQ')
        self._peer.sendToPeer(message, host=remotePeerAddr)

    def _joinNetFromDNS(self, remoteDNS):
        peersInDNS = dns.resolver.query(remoteDNS, 'TXT', raise_on_no_answer=True)
        for each in peersInDNS:
            addr, port = str(each)[1:-1].split(':')
            message = self.JOIN.packWrap('REQ')
            self._peer.sendToPeer(message, host=(addr, port))

    def _syncListFromPeer(self, remoteHost):
        message = self.LIST.packWrap('REQ')
        self._peer.sendToPeer(message, host=remoteHost, timeout=5)

    def sendMessage(self, message, pid=None, host=None):
        message = self.MESG.packWrap('REQ', message)
        self._peer.sendToPeer(message, host=host, timeout=5)


