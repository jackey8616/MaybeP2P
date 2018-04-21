import pytest

from protocol.message import Message

class TestMessage:

    def test___REQ(self, message):
        with pytest.raises(NotImplementedError):
            message._Message__REQ()

    def test___RES(self, message):
        with pytest.raises(NotImplementedError):
            message._Message__RES()
    
    def test_wrapperS(self):
        with pytest.raises(NotImplementedError):
            Message.wrapperS() 

    def test_wrapper(self, message):
        with pytest.raises(NotImplementedError):
            message.wrapper()
