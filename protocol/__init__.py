import sys
if sys.version_info > (3, 0):
    from .protocol import Protocol
else:
    from protocol import Protocol
