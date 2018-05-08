import sys, copy, traceback
import dns.resolver

from ..protocol import Protocol
from .message import JOIN, LIST, QUIT, MESG

class ClassicV1(Protocol):

    def __init__(self, peer, name='ClassicV1'):
        Protocol.__init__(self, name, peer, {
            'JOIN': JOIN,
            'LIST': LIST,
            'QUIT': QUIT,
            'MESG': MESG
        })

    def broadcast(self, message, waitReply=False):
        netReply = []
        for (pid, peerInfo) in copy.deepcopy(self._peersInfo).items():
            netReply.append({ pid: self._peer.sendToPeer(message, peerInfo.getHost(), pid=pid, waitReply=waitReply) })
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


