import sys
if sys.version_info > (3, 0):
    from .peer import Peer
    from .connection import PeerConnection
else:
    from peer import Peer
    from connection import PeerConnection
