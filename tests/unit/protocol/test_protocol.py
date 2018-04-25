import pytest

from protocol.protocol import Protocol

class TestProtocol:

    def test__messageExtand(self, protocol):
        assert protocol._messageExtand() == True

    def test_wrapper(self, protocol):
        assert protocol.wrapper(None, None, None) == None
 
