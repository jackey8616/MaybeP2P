import pytest

from protocol.message.message import Message

class TestMessage:

    @pytest.fixture(scope='session')
    def message(self):
        m = Message(None, None)
        return m

    @pytest.mark.skip('Private function')
    def test___REQ(self, message):
        with pytest.raises(NotImplementedError):
            message.__REQ(())

    @pytest.mark.skip('Private function')
    def test___RES(self, message):
        with pytest.raises(NotImplementedError):
            message.__RES(())
