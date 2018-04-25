import sys

if sys.version_info > (3, 0):
    from .JOIN import JOIN
    from .LIST import LIST
    from .QUIT import QUIT
    from .ERRO import ERRO
else:
    from JOIN import JOIN
    from LIST import LIST
    from QUIT import QUIT
    from ERRO import ERRO

