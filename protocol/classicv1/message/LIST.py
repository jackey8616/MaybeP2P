import sys, traceback

from protocol.message import Message

class LIST(Message):

    def __init__(self):
        Message.__init__(self)

    def handler(self, peer, peerConn, msgData):
        self.peer = peer
        self.peerConn = peerConn

        try:
            self.peer.lock.acquire()
            if msgData.startswith('REQ'):
                return self._REQ(())
            elif msgData.startswith('RES'):
                return self._RES((msgData[4:]))
            elif msgData.startswith('FOR'):
                return self._FOR((msgData[4:]))
        except Exception as e:
            traceback.print_exc()
            self.peerConn.sendData('ERRO', e)
        finally:
            self.peer.lock.release()
        return False

    def _REQ(self, *data):
        message = self.peerConn.protocol['ClassicV1'].wrapper(self.peer, self.peerConn, 'LIST', 'RES')
        self.peerConn.sendProtocolData(message)
        return True

    def _RES(self, *data):
        for each in data[0].split(','):
            (pid, addr, port) = each.split('|')
            if pid != self.peer.id:
                self.peer.addPeer(pid, addr, port)
        return True

    def _FOR(self, *data):
        return True

    @staticmethod
    def packetS(pkType, peer, peerConn):
        data = pkType
        if pkType == 'RES':
            for (pid, host) in peer.peers.items():
                data += ',%s|%s|%s' % (pid, host[0], host[1])
        return len(data), data

    def packet(self, pkType, peer, peerConn):
        return LIST.packetS(pkType, peer, peerConn)

