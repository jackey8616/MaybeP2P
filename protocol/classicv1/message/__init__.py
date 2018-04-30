import sys

if sys.version_info > (3, 0):
    from .JOIN import JOIN
    from .LIST import LIST
    from .QUIT import QUIT
    from .ERRO import ERRO
    from .MESG import MESG
else:
    from JOIN import JOIN
    from LIST import LIST
    from QUIT import QUIT
    from ERRO import ERRO
    from MESG import MESG

