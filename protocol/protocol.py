import sys, logging, json, struct

if sys.version_info > (3, 0):
    from .message import JOIN, LIST, QUIT, REPL, TEST
else:
    from message import JOIN, LIST, QUIT, REPL, TEST
#,SYNC, MESG, ERRO

names = '<NAME>'
messages = {
    'JOIN': JOIN,
    'LIST': LIST,
#    'NAME': NAME,
#    'SYNC': SYNC,
#    'MESG': MESG,
    'QUIT': QUIT,
    'REPL': REPL,
#    'ERRO': ERRO
    'TEST': TEST,
}

class Protocol:

    def __init__(self, name, peerConn, peer):
        self._name = self._nameRegister(name)
        self._peerConn = peerConn
        self._peer = peer
        self._messages = {}

        self._messageRegister()

    def _nameRegister(self, name):
        global names
        names = name
        return names

    def _messageRegister(self):
        global messages
        for (name, message) in messages.items():
            self._messages[name] = message(self._peer, self._peerConn)

    @staticmethod
    def wrapperS(peer, peerConn, msgType, pkType):
        global names, messages
        msgLen, msgData = messages[msgType].packetS(pkType, peer, peerConn)
        message = struct.pack('!12s4sL%ds' % msgLen, names.encode(), msgType.encode(), msgLen, msgData.encode())
        return message

    def wrapper(self, msgType, pkType):
        return Protocol.wrapperS(self._peer, self._peerConn, msgType, pkType)

