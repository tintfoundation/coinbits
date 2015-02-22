import unittest

from coinbits.txns.keys import PublicKey, PrivateKey


class TestPrivateKey(unittest.TestCase):
    def test_equality(self):
        pk = PrivateKey.from_wif("5KXUXPCRpLxHqHdJVMr3n6bgdqYLQa9siJpfhi7hzWtfFCd2zZH")
        pkt = PrivateKey.from_wif("5KXUXPCRpLxHqHdJVMr3n6bgdqYLQa9siJpfhi7hzWtfFCd2zZH")
        self.assertEqual(pk, pkt)

    def test_address(self):
        pk = PrivateKey.from_wif("5KXUXPCRpLxHqHdJVMr3n6bgdqYLQa9siJpfhi7hzWtfFCd2zZH")
        self.assertEqual(pk.to_address(), "1wYiNC2EERnKPWP7QbvWGEfNprtHg1bsz")

    def test_wif(self):
        pk = PrivateKey("e1385343f7ea362b0de7e5772a6c766d44ce4bf69e1380381630bf1892c638d5")
        self.assertEqual(pk.to_wif(), "5KXUXPCRpLxHqHdJVMr3n6bgdqYLQa9siJpfhi7hzWtfFCd2zZH")

    def test_to_public(self):
        pubhex = "04c0e09b6c5cf729905dc5a87b6694b4ce72b5a9aab97ce194b15c428df82edeae460b1454"
        pubhex += "cfe915d68195eef67b824c76c21810372fc8b4676e6f251a5b2377c7"
        pk = PrivateKey("e1385343f7ea362b0de7e5772a6c766d44ce4bf69e1380381630bf1892c638d5")
        self.assertEqual(pk.get_public_key(), PublicKey(pubhex))

    def test_signing(self):
        pk = PrivateKey("e1385343f7ea362b0de7e5772a6c766d44ce4bf69e1380381630bf1892c638d5")
        sig = pk.sign('hi there')
        self.assertTrue(pk.get_public_key().verify(sig, 'hi there'))


class TestPublicKey(unittest.TestCase):
    def test_equality(self):
        pubhex = "04c0e09b6c5cf729905dc5a87b6694b4ce72b5a9aab97ce194b15c428df82edeae460b1454"
        pubhex += "cfe915d68195eef67b824c76c21810372fc8b4676e6f251a5b2377c7"
        self.assertEqual(PublicKey(pubhex), PublicKey(pubhex))

    def test_to_hex(self):
        pubhex = "04c0e09b6c5cf729905dc5a87b6694b4ce72b5a9aab97ce194b15c428df82edeae460b1454"
        pubhex += "cfe915d68195eef67b824c76c21810372fc8b4676e6f251a5b2377c7"
        pk = PrivateKey("e1385343f7ea362b0de7e5772a6c766d44ce4bf69e1380381630bf1892c638d5")
        self.assertEqual(pk.get_public_key().to_hex(), pubhex.upper())

    def test_address(self):
        pubhex = "04c0e09b6c5cf729905dc5a87b6694b4ce72b5a9aab97ce194b15c428df82edeae460b1454"
        pubhex += "cfe915d68195eef67b824c76c21810372fc8b4676e6f251a5b2377c7"
        self.assertEqual(PublicKey(pubhex).to_address(), "1wYiNC2EERnKPWP7QbvWGEfNprtHg1bsz")
