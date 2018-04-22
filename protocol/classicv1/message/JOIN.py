import sys, logging, traceback

from protocol.message import Message
#if sys.version_info > (3, 0):
#    from .message import Message
#else:
#    from message import Message

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
            traceback.print_exc()
            self.peerConn.sendData('ERRO', e)
        finally:
            self.peer.lock.release()

    def __REQ(self, *data):
        (pid, addr, port), = data
        if self.peer.addPeer(pid, addr, port):
            message = self.peerConn.protocol.wrapper('JOIN', 'RES')
            self.peerConn.sendProtocolData(message)
        else:
            self.peerConn.sendData('ERRO', 'Peer %s exists' % pid)

    def __RES(self, *data):
        (pid, addr, port), = data
        if self.peer.addPeer(pid, addr, port):
            logging.debug('Peer added pid {%s} at %s:%s' % (pid, addr, port))
        else:
            self.peerConn.sendData('ERRO', 'Peer %s exists' % pid)

    @staticmethod
    def packetS(pkType, peer, peerConn):
        data = '%s,%s,%s,%s' % (pkType, peer.id, peer.peerInfo.addr[0], peer.peerInfo.addr[1])
        return len(data), data

    def packet(self, pkType, peer, peerConn):
        return JOIN.packetS(pkType, peer, peerConn)

