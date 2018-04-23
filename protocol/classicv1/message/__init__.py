import sys

if sys.version_info > (3, 0):
    from .JOIN import JOIN
    from .LIST import LIST
    from .QUIT import QUIT
else:
    from JOIN import JOIN
    from LIST import LIST
    from QUIT import QUIT

