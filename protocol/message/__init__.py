import sys
if sys.version_info > (3, 0):
    from .message import Message
    from .REPL import REPL
    from .ERRO import ERRO
    from .TEST import TEST
else:
    from message import Message
    from REPL import REPL
    from ERRO import ERRO
    from TEST import TEST
