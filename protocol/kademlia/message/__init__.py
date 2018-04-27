import sys

if sys.version_info > (3, 0):
    from .PING import PING
    from .STOR import STOR
    from .FNOD import FNOD
    from .FVAL import FVAL
else:
    from PING import PING
    from STOR import STOR
    from FNOD import FNOD
    from FVAL import FVAL
