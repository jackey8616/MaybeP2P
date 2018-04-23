import sys, logging, json, struct

if sys.version_info > (3, 0):
    from .message import REPL, TEST
else:
    from message import REPL, TEST
#,SYNC, MESG, ERRO

names = '<PROTONAME>'
messages = {}

class Protocol:

    def __init__(self, name, peerConn, peer):
        self._name = self._nameRegister(name if name else '<PROTONAME>')
        self._peerConn = peerConn
        self._peer = peer
        self._messages = {
            #'REPL': REPL,
            #'TEST': TEST,
        }

        self._messageExtand()
        self._messageRegister()

    def _nameRegister(self, name):
        global names
        names = name
        return names

    def _messageExtand(self):
        raise NotImplementedError

    def _messageRegister(self):
        global messages
        for (name, message) in self._messages.items():
            messages[name] = message
            self._messages[name] = message()

    @staticmethod
    def wrapperS(peer, peerConn, msgType, pkType):
        global names, messages
        msgLen, msgData = messages[msgType].packetS(pkType, peer, peerConn)
        message = struct.pack('!12s4sL%ds' % msgLen, names.encode(), msgType.encode(), msgLen, msgData.encode())
        return message

    def wrapper(self, msgType, pkType):
        return Protocol.wrapperS(self._peer, self._peerConn, msgType, pkType)

