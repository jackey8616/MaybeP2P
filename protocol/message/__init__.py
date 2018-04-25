import sys
if sys.version_info > (3, 0):
    from .message import Message
    from .REPL import REPL
else:
    from message import Message
    from REPL import REPL

