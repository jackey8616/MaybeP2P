import sys, socket, struct, traceback

from protocol import Protocol

class PeerConnection:

    def __init__(self, peerId, addr, port, peer, sock=None):
        self.stopped = False

        self.id = peerId
        if sock:
            self.sock = sock
        else:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.sock.connect((addr, int(port)))
        if sys.version_info > (3, 0):
            self.sd = self.sock.makefile('rw', None)
        else:
            self.sd = self.sock.makefile('rw', 0)
        self.protocol = Protocol(self, peer)

    def sendData(self, msgType, msgData):
        try:
            msgLen = len(msgData)
            message = struct.pack('!4sL%ds' % msgLen, msgType.encode(), msgLen, msgData.encode())
        #    message = self.protocol.encoder(msgType, msgData)
            self.sd.write(message.decode())
            self.sd.flush()
        except:
            return False
        return True
        
    def recvData(self):
        try:
            msgtype = self.sd.read(4)
            #print(msgtype)
            if not msgtype:
                return(None, None)
            lenstr = self.sd.read(4)
            msglen = int(struct.unpack('!L', lenstr.encode())[0])
            msg = ""

            while len(msg) != msglen:
                data = self.sd.read(min(2048, msglen - len(msg)))
                if not len(data):
                    break
                msg += data

            if len(msg) != msglen:
                return (None, None)
        except:
            traceback.print_exc()
            return (None, None)
        return (msgtype, msg)

    def close(self):
        self.sock.close()
        self.sock = None
        self.sd = None

