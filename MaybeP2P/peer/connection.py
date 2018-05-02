import sys, threading, logging, socket, struct, traceback

class PeerConnection(threading.Thread):

    def __init__(self, peerId, peer, protocol, addr=None, port=None, sock=None, timeout=1):
        threading.Thread.__init__(self)
        self.stopped = False

        self.id = peerId
        self.peer = peer
        self.timeout = timeout
        if sock:
            self.sock = sock
        else:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.sock.settimeout(timeout)
            self.sock.connect((addr, int(port)))
            self.sock.settimeout(None)
        if sys.version_info > (3, 0):
            self.sd = self.sock.makefile('rw', None)
        else:
            self.sd = self.sock.makefile('rw', 0)
        self.protocol = protocol

    def run(self):
        try:
            protoType, msgType, msgData = self.recvData()
            self.protocol.handler(self, msgType, msgData)
            logging.debug((protoType, msgType, msgData))
        except Exception as e:
            traceback.print_exc()
        finally:
            self.exit()

    def sendData(self, message):
        try:
            self.sd.write(message.decode())
            self.sd.flush()
        except:
            return False
        return True
        
    def recvData(self):
        try:
            protoType = self.sd.read(12).replace('\x00', '')
            msgtype = self.sd.read(4)
            if not msgtype:
                return(None, None, None)
            lenstr = self.sd.read(4)
            msglen = int(struct.unpack('!L', lenstr.encode())[0])
            msg = ""

            while len(msg) != msglen:
                data = self.sd.read(min(2048, msglen - len(msg)))
                if not len(data):
                    break
                msg += data

            if len(msg) != msglen:
                return (None, None, None)
        except:
            traceback.print_exc()
            return (None, None, None)
        return (protoType, msgtype, msg)

    def exit(self):
        self.sock.close()
        self.sock = None
        self.sd = None

