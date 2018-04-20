import logging

from message import Message

class JOIN(Message):

    def __init__(self, peer, peerConn):
        Message.__init__(self, peer, peerConn)

    def handler(self, msgData):
        try:
            self.peer.lock.acquire()
            pkType, pid, addr, port = msgData.split(',')
            if pkType == 'REQ':
                self.__REQ((pid, addr, port))
            elif pkType == 'RES':
                self.__RES((pid, addr, port))
        except Exception as e:
            self.peerConn.sendData('ERRO', e)
        finally:
            self.peer.lock.release()

    def __REQ(self, *data):
        (pid, addr, port), = data
        if self.peer.addPeer(pid, addr, port):
            self.peerConn.sendData('JOIN', 'RES,%s,%s,%s' % (self.peer.id, self.peer.peerInfo.addr[0], self.peer.peerInfo.addr[1]))
        else:
            self.peerConn.sendData('ERRO', 'Peer %s exists' % pid)

    def __RES(self, *data):
        (pid, addr, port), = data
        if self.peer.addPeer(pid, addr, port):
            logging.debug('Peer added pid: %s' % pid)
        else:
            self.peerConn.sendData('ERRO', 'Peer %s exists' % pid)

