
class TestBukket:

    def test_insertNode(self, bukket):
        pass

    def test_exclusiveOR(self, bukket):
        temp = bukket.protocol._peer.id
        bukket.protocol._peer.id = 'cdeb95e3-778d-43d8-966e-9fd4f163643d'
        assert bukket.exlusiveOR('adcc30f1-0830-44b8-8a95-c0876fcb2ff3') == 127811735236059427915415362594671184846
        bukket.protocol._peer.id = temp

