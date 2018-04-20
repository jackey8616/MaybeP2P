import logging, json

from message import JOIN, LIST, QUIT, REPL, TEST
#,SYNC, MESG, ERRO

class Protocol:

    def __init__(self, peerConn, peer):
        self._peerConn = peerConn
        self._peer = peer
        self._handlers = {
            'JOIN': JOIN(peer, peerConn),
            'LIST': LIST(peer, peerConn),
#            'NAME': NAME(peer, peerConn),
#            'SYNC': SYNC(),
#            'MESG': MESG(),
            'QUIT': QUIT(peer, peerConn),
            'REPL': REPL(peer, peerConn),
#            'ERRO': ERRO()
            'TEST': TEST(peer, peerConn),
        }

    def _addHandler(self, name, handler):
        self._handlers[name] = handler

    def encoder(self, msgType, msgData=None):
        jsonData = { 'type': msgType }
        if msgType in self._handlers:
            jsonData['data'] = self._handlers[msgType].encoder(self._peerConn, msgData)
        else:
            jsonData['data'] = self._handlers['MESG'].encoder(self._peerConn, msgData)
        return json.dumps(jsonData)
           
    def decoder(self, msgData):
        jsonData = json.loads(msgData)
        msgType, msgData = (jsonData['type'], jsonData['data'])
        if jsonData['uuid_from'] == self._peerConn.peer.peerInfo.uuid:
            self._peerConn.close()
            return       

        if msgType in self._handlers:
            return self._handlers[msgType].decoder(self._peerConn, msgData)
        else:
            return self._handlers['ERRO'].decoder(self._peerConn, msgData)

