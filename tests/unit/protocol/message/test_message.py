import pytest

from protocol.message import Message

class TestMessage:

    @pytest.mark.skip('Private function')
    def test___REQ(self, message):
        with pytest.raises(NotImplementedError):
            message.__REQ(())

    @pytest.mark.skip('Private function')
    def test___RES(self, message):
        with pytest.raises(NotImplementedError):
            message.__RES(())
    
    def test_wrapperS(self):
        with pytest.raises(NotImplementedError):
            Message.wrapperS() 

    def test_wrapper(self, message):
        with pytest.raises(NotImplementedError):
            message.wrapper()
