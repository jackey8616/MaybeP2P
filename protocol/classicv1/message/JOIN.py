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
            self.peerConn.sendData(e)
        finally:
            self.peer.lock.release()
        return False

    def _REQ(self, *data):
        (pid, addr, port), = data
        if self.protocol.addPeer(pid, addr, port):
            message = self.protocol.JOIN.packWrap('RES')
            self.peerConn.sendData(message)
        else:
            #self.peerConn.sendData('Peer %s exists' % pid)
            return False
        return True

    def _RES(self, *data):
        (pid, addr, port), = data
        if self.protocol.addPeer(pid, addr, port):
            logging.debug('Peer added pid {%s} at %s:%s' % (pid, addr, port))
        else:
            #self.peerConn.sendData('Peer %s exists' % pid)
            return False
        return True

    def _FOR(self, *data):
        return True

    def pack(self, pkType, *data):
        data = '%s,%s,%s,%s' % (pkType, self.protocol._peer.id, self.protocol._peer.peerInfo.addr[0], self.protocol._peer.peerInfo.addr[1])
        return (len(data), data)

