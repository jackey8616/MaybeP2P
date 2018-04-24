import sys, logging, json, struct

names = '<PROTONAME>'
messages = {}

class Protocol:

    def __init__(self, name):
        self._name = self._nameRegister(name if name else '<PROTONAME>')
        self._messages = {}

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

    def wrapper(self, peer, peerConn, msgType, pkType):
        return Protocol.wrapperS(peer, peerConn, msgType, pkType)

