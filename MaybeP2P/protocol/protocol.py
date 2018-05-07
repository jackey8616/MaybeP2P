import logging, json, struct, traceback

from ..peer.peerinfo import PeerInfo

class Protocol:

    def __init__(self, name, peer):
        if name is None or peer is None:
            raise ValueError('Name and Peer parameter can not be None.')
        self._name = name
        self._peer = peer
        self._peersInfo = {}
        self._messages = {}

        self._messageExtand()
        self._messageRegister()
        self._protocolValidator()

    def _messageExtand(self):
        extandMessages = {
            # Put messages in here for protocol extand.
        }
        self._messages.update(extandMessages)
        return True

    def _messageRegister(self):
        for (name, message) in self._messages.items():
            setattr(self, name, message(self))
            self._messages[name] = getattr(self, name)

    def _protocolValidator(self):
        if self._messages == {}:
            logging.warning('Protocol initialed with no any loaded messages.')
            logging.warning('Consider there is _messageExtand() method to load messages?')
        else:
            logging.debug('Protocol initialed with %s' % (self._messages))

    def _wrap(self, *msg):
        (msgLen, msgType, msgData), = msg
        return struct.pack('!12s4sL%ds' % msgLen, self._name.encode(), msgType.encode(), msgLen, msgData.encode())

    def handler(self, peerConn, msgType, msgData):
        try:
            message = getattr(self, msgType)
            message.handler(peerConn, msgData)
            return True
        except:
            return False

    def getPeerInfoBy(self, *data):
        (query, ) = data
        if ':' in query:
            query = (query.split(':')[0], int(query.split(':')[1]))
        for (pid, peerInfo) in self._peersInfo.items():
            if peerInfo.getHost() == query or query in peerInfo.pid:
                return (pid, peerInfo)
        return (None, None)

    def addPeer(self, *data):
        pid, addr, port = data
        if pid not in self._peersInfo and pid != str(self._peer.id):
            self._peersInfo[pid] = PeerInfo(pid, (addr, port), 'Active')
            return True
        else:
            return False

    def removePeer(self, *data):
        (target, ) = data
        try:
            if ':' in target:
                for (pid, peerInfo) in self._peersInfo.items():
                    if peerInfo.getHost() == (target.split(':')[0], int(target.split(':')[1])):
                        self._peersInfo.pop(pid)
                        return True
            elif target in self._peersInfo:
                self._peersInfo.pop(target)
                return True
        except:
            traceback.print_exc()
        return False

    def broadcast(self, message, waitReply=False):
        raise NotImplementedError

    def exit(self):
        raise NotImplementedError

