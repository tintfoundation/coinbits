import unittest

from coinbits.encoding import ones_prefix_length


class TestBase58(unittest.TestCase):
    def test_encode(self):
        x = ones_prefix_length(1)
        self.assertEqual(x, 5)
        self.assertEqual(1, 1)
