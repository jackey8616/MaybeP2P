
class PeerInfo(object):

    @property
    def pid(self):
        return self._pid

    @pid.setter
    def pid(self, value):
        self._pid = value

    @property
    def host(self):
        return self._host

    @host.setter
    def host(self, value):
        if not isinstance(value, tuple):
            raise ValueError('Host must be a tuple.')
        elif not isinstance(value[0], str):
            raise ValueError('Address must be a str.')
        elif int(value[1]) <= 0 or int(value[1]) > 65535:
            raise ValueError('Port must be in range of 0 - 65535')
        else:
            self._host = (value[0], int(value[1]))

    @property
    def addr(self):
        return self._host[0]

    @property
    def port(self):
        return self._host[1]

    def __init__(self, pid, host, status, **kwargs):
        self._pid = pid
        self._host = (host[0], int(host[1]))
        self.status = status
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self):
        return str(self.pid)

