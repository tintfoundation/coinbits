import unittest

from coinbits.encoding import b58decode, b58encode, b256encode, b58_check_decode


class TestBase58(unittest.TestCase):
    def test_base58(self):
        self.assertEqual(b58encode(123), '38')
        self.assertEqual(b58decode('38'), 123)

    def test_base256(self):
        self.assertEqual(b256encode(12), '\x0c')

    def test_b58_check_decode(self):
        addy = '1D3BKJghxWVwXwQiZwowC8DrSzNFLyDCqY'
        shouldbe = '\x84\n\xf3\xcd\xd8\x04\x1a\x10"R\xf3\xc9\x0eM\xf7\xc8\xad\xfa\xe1L'
        self.assertEqual(b58_check_decode(addy), shouldbe)
