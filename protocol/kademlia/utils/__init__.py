import sys

if sys.version_info > (3, 0):
    from .bukket import Bukket
    from .node import Node
else:
    from bukket import Bukket
    from node import Node
