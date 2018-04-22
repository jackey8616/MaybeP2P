import sys, traceback

from protocol.message import Message

class LIST(Message):

    def __init__(self, peer, peerConn):
        Message.__init__(self, peer, peerConn)

    def handler(self, msgData):
        try:
            self.peer.lock.acquire()
            if msgData.startswith('REQ'):
                self.__REQ(())
            elif msgData.startswith('RES'):
                self.__RES((msgData[4:]))
        except Exception as e:
            traceback.print_exc()
            self.peerConn.sendData('ERRO', e)
        finally:
            self.peer.lock.release()

    def __REQ(self, *data):
        message = self.peerConn.protocol.wrapper('LIST', 'RES')
        self.peerConn.sendProtocolData(message)

    def __RES(self, *data):
        for each in data[0].split(','):
            (pid, addr, port) = each.split('|')
            if pid != self.peer.id:
                self.peer.addPeer(pid, addr, port)
        print(self.peer.peers)

    @staticmethod
    def packetS(pkType, peer, peerConn):
        data = pkType
        if pkType == 'RES':
            for (pid, host) in peer.peers.items():
                data += ',%s|%s|%s' % (pid, host[0], host[1])
        return len(data), data

    def packet(self, pkType, peer, peerConn):
        return LIST.packetS(pkType, peer, peerConn)

