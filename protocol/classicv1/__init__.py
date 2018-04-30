import sys, traceback
import dns.resolver

from protocol import Protocol
from protocol.classicv1.message import JOIN, LIST, QUIT, MESG

class ClassicV1(Protocol):

    def __init__(self, peer):
        Protocol.__init__(self, 'ClassicV1', peer)

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
        for (pid, host) in self._peers.items():
            netReply.append({ pid: self._peer.sendToPeer(host[0], host[1], message, pid=pid, waitReply=waitReply) })
        return netReply

    def exit(self):
        try:
            message = self.QUIT.packWrap('REQ')
            self.broadcast(message, waitReply=False)
            self._peer.sendToPeer(self._peer.peerInfo.addr[0], self._peer.peerInfo.addr[1], message, waitReply=False)
        except:
            traceback.print_exc()

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
        self._peer.sendToPeer(addr, port, message, timeout=5)

    def sendMessage(self, message, pid=None, host=None):
        message = self.MESG.packWrap('REQ', message)
        self._peer.sendToPeer(host[0], host[1], message, timeout=5)


