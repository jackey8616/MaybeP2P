import sys
if sys.version_info > (3, 0):
    from .JOIN import JOIN
    from .LIST import LIST
    from .QUIT import QUIT
    from .REPL import REPL
    from .ERRO import ERRO
    from .TEST import TEST
else:
    from JOIN import JOIN
    from LIST import LIST
    from QUIT import QUIT
    from REPL import REPL
    from ERRO import ERRO
    from TEST import TEST
