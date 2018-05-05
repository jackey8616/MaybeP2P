
class PeerInfo:

    def __init__(self, pid, host, status, **kwargs):
        self.pid = pid
        self.addr = host[0]
        self.port = int(host[1])
        self.status = status
        for key, value in kwargs.items():
            setattr(self, key, value)

    def getHost(self):
        return (self.addr, self.port)

    def __str__(self):
        return str(self.pid)

