import sys
if sys.version_info > (3, 0):
    from .protocol import Protocol
    from .classicv1 import ClassicV1
else:
    from protocol import Protocol
    from classicv1 import ClassicV1
