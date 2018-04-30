import sys, traceback

from protocol.message import Message

class LIST(Message):

    def __init__(self, protocol):
        Message.__init__(self, protocol)

    def handler(self, peerConn, msgData):
        self.peerConn = peerConn
        self.peer = peerConn.peer

        try:
            self.peer.lock.acquire()
            if msgData.startswith('REQ'):
                return self._REQ(())
            elif msgData.startswith('RES'):
                return self._RES((msgData[4:]))
            elif msgData.startswith('FOR'):
                return self._FOR((msgData[4:]))
        except:
            traceback.print_exc()
            #self.peerConn.sendData('ERRO', e)
        finally:
            self.peer.lock.release()
        return False

    def _REQ(self, *data):
        message = self.protocol.LIST.packWrap('RES')
        self.peerConn.sendData(message)
        return True

    def _RES(self, *data):
        for each in data[0].split(','):
            (pid, addr, port) = each.split('|')
            if pid != self.peer.id:
                self.protocol.addPeer(pid, addr, port)
        return True

    def _FOR(self, *data):
        return True

    def pack(self, pkType, *data):
        data = pkType
        if pkType == 'RES':
            for (pid, host) in self.protocol._peers.items():
                data += ',%s|%s|%s' % (pid, host[0], host[1])
        return len(data), data

