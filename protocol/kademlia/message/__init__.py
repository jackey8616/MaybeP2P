import sys

if sys.version_info > (3, 0):
    from .PING import PING
    from .PONG import PONG
else:
    from PING import PING
    from PONG import PONG
