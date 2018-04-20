import pytest

from protocol import Protocol

class TestProtocol:

    @pytest.fixture(scope='session')
    def protocol(self):
        p = Protocol(None, None)
        return p

    def test__addHandler(self, protocol):
        protocol._addHandler('TEST', None)
        assert 'TEST' in protocol._handlers
        assert protocol._handlers['TEST'] == None
