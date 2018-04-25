import pytest

from protocol.message import Message

class TestMessage:

    def test_handler(self, message):
        with pytest.raises(NotImplementedError):
            message.handler(None, None)

    def test__REQ(self, message):
        with pytest.raises(NotImplementedError):
            message._REQ()

    def test__RES(self, message):
        with pytest.raises(NotImplementedError):
            message._RES()

    def test__FOR(self, message):
        with pytest.raises(NotImplementedError):
            message._FOR()
    
    def test_packS(self):
        with pytest.raises(NotImplementedError):
            Message.packS(None, None, None) 

    def test_pack(self, message):
        with pytest.raises(NotImplementedError):
            message.pack(None, None)
