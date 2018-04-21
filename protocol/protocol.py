import sys, logging, json, struct

if sys.version_info > (3, 0):
    from .message import JOIN, LIST, QUIT, REPL, TEST
else:
    from message import JOIN, LIST, QUIT, REPL, TEST
#,SYNC, MESG, ERRO

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
        self._name = name
        self._peerConn = peerConn
        self._peer = peer
        self._messages = {}

        self._messageRegister()

    def _messageRegister(self):
        global messages
        for (name, message) in messages.items():
            self._messages[name] = message(self._peer, self._peerConn)

    @staticmethod
    def wrapperS(peer, peerConn, msgType, pkType):
        global messages
        msgLen, msgData = messages[msgType].packetS(pkType, peer, peerConn)
        message = struct.pack('!12s4sL%ds' % msgLen, self._name.encode(), msgType.encode(), msgLen, msgData.encode())
        return message

    def wrapper(self, msgType, pkType):
        msgLen, msgData = self._messages[msgType].packet(pkType, self._peer, self._peerConn)
        message = struct.pack('!12s4sL%ds' % msgLen, self._name.encode(), msgType.encode(), msgLen, msgData.encode())
        return message

