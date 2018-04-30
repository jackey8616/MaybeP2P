import logging, traceback

from protocol.message import Message

class MESG(Message):

    def __init__(self, protocol):
        Message.__init__(self, protocol)

    def handler(self, peerConn, msgData):
        self.peerConn = peerConn
        self.peer = peerConn.peer

        try:
            if msgData.startswith('REQ'):
                self._REQ(msgData.split(',')[1])
            elif msgData.startswith('RES'):
                self._RES(msgData)
            elif msgData.startswith('FOR'):
                self._FOR(msgData)
            return True
        except Exception as e:
            traceback.print_exc()
        finally:
            pass
        return False

    def _REQ(self, *data):
        logging.info(data[0])
        return True

    def _RES(self, *data):
        return True

    def _FOR(self, *data):
        return True

    def pack(self, pkType, *data):
        data = '%s,%s' % (pkType, data[0][0])
        return (len(data), data)

