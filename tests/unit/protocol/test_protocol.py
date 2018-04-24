import pytest

from protocol.protocol import Protocol

class TestProtocol:

    def test__messageExtand(self):
        with pytest.raises(NotImplementedError):
            Protocol('test')
