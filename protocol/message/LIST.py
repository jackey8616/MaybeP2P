import sys

if sys.version_info > (3, 0):
    from .message import Message
else:
    from message import Message

class LIST(Message):

    def __init__(self, peer, peerConn):
        Message.__init__(self, peer, peerConn)

    def handle(self, msgData):
        try:
            self.peer.lock.acquire()
            if msgData.startwith('REQ'):
                self.__REQ(())
            elif msgData.startwith('RES'):
                self.__RES((msgData[4:].split(',')))
        except Exception as e:
            self.peerConn.sendData('ERRO', e)
        finally:
            self.peer.lock.release()

    def __REQ(self, *data):
        message = self.peerConn.protocol.wrapper('LIST', 'RES')
        self.peerConn.sendProtocolData(message)

    def __RES(self, *data):
        for each in data.split(','):
            (pid, addr, port) = each.split('|')
            self.peer.addPeer(pid, addr, port)
        print(self.peer.peers)

    @staticmethod
    def packetS(pkType, peer, peerConn):
        if pkType == 'REQ':
            data = 'REQ'
        elif pyType == 'RES':
            data = 'RES'
            for (pid, host) in peer.peers.items():
                data += ',%s|%s|%s' % (pid, host[0], host[1])
        return len(data), data

    def packet(self, pkType, peer, peerConn):
        if pkType == 'REQ':
            data = 'REQ'
        elif pkType == 'RES':
            data = 'RES'
            for (pid, host) in peer.peers.items():
                data += ',%s|%s|%s' % (pid, host[0], host[1])
        return len(data), data

