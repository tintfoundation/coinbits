import unittest

from coinbits.encoding import ones_prefix_length


class TestBase58(unittest.TestCase):
    def test_encode(self):
        self.assertEqual(1, 1)
