import sys, logging, json, struct, traceback

names = '<PROTONAME>'
messages = {}

class Protocol:

    def __init__(self, name, peer):
        self._name = self._nameRegister(name if name else '<PROTONAME>')
        self._peer = peer
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
            setattr(self, name, message(self))
            self._messages[name] = getattr(self, name)

#    def _wrap(self, peerConn, *msg):
#        msgLen, msgType, msgData = msg
#        return struct.pack('!12s4sL%ds' % msgLen, names.encode(), msgType.encode(), msgLen, msgData.encode())

    def wrapper(self, peerConn, msgType, pkType):
        try:
            msgLen, msgData = getattr(self, msgType).pack(pkType)
            message = struct.pack('!12s4sL%ds' % msgLen, names.encode(), msgType.encode(), msgLen, msgData.encode())
            return message
        except Exception as e:
            traceback.print_exc()
            return None

