import logging, traceback

from protocol.message import Message

class JOIN(Message):

    def __init__(self, protocol):
        Message.__init__(self, protocol)

    def handler(self, peerConn, msgData):
        self.peerConn = peerConn
        self.peer = peerConn.peer

        try:
            self.peer.lock.acquire()
            pkType, pid, addr, port = msgData.split(',')
            if pkType == 'REQ':
                return self._REQ((pid, addr, port))
            elif pkType == 'RES':
                return self._RES((pid, addr, port))
            elif pkType == 'FOR':
                return self._FOR(())
        except Exception as e:
            traceback.print_exc()
            self.peerConn.sendData('ERRO', e)
        finally:
            self.peer.lock.release()
        return False

    def _REQ(self, *data):
        (pid, addr, port), = data
        if self.peer.addPeer(pid, addr, port):
            message = self.peerConn.protocol[self.protocol._name].wrapper(self.peerConn, 'JOIN', 'RES')
            self.peerConn.sendProtocolData(message)
        else:
            self.peerConn.sendData('ERRO', 'Peer %s exists' % pid)
            return False
        return True

    def _RES(self, *data):
        (pid, addr, port), = data
        if self.peer.addPeer(pid, addr, port):
            logging.debug('Peer added pid {%s} at %s:%s' % (pid, addr, port))
        else:
            self.peerConn.sendData('ERRO', 'Peer %s exists' % pid)
            return False
        return True

    def _FOR(self, *data):
        return True

    def pack(self, pkType, peerConn):
        data = '%s,%s,%s,%s' % (pkType, peerConn.peer.id, peerConn.peer.peerInfo.addr[0], peerConn.peer.peerInfo.addr[1])
        return len(data), data

