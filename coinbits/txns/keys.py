import hashlib
import ecdsa

from coinbits.encoding import b58encode, b58decode
from coinbits.txns.exceptions import KeyDecodeError


class PublicKey(object):
    """
    This is a representation for Bitcoin public keys. In this
    class you'll find methods to import/export keys from multiple
    formats. Use a hex string representation to construct a new
    public key or use the clas methods to import from another format.
    """
    key_prefix = '\x04'

    def __init__(self, hexkey):
        """
        Initialize a public key object.  Requires an existing version
        of this key in hex.

        Args:
            hexkey: The key in hex string format
        """
        stringkey = hexkey.decode("hex")[1:]
        self.public_key = ecdsa.VerifyingKey.from_string(stringkey,
                                                         curve=ecdsa.SECP256k1)

    @classmethod
    def from_private_key(klass, private_key):
        """
        This class method will create a new PublicKey based on a
        PrivateKey.

        Args:
            private_key: The PrivateKey

        Returns:
            A new PublicKey
        """
        public_key = private_key.private_key.get_verifying_key()
        hexkey = (klass.key_prefix + public_key.to_string()).encode("hex")
        return klass(hexkey)

    def verify(self, signature, message):
        """
        Verify the given signature of the message.  Returns True if
        verification is successful, False otherwise.
        """
        digest = hashlib.sha256(hashlib.sha256(message).digest()).digest()
        return self.public_key.verify_digest(signature[:-1], digest, sigdecode=ecdsa.util.sigdecode_der)

    def to_hex(self):
        """
        This method will convert the public key to
        a hex string representation.

        Returns:
            A hex string representation of the public key
        """
        hexkey = self.public_key.to_string().encode("hex")
        return self.key_prefix.encode("hex") + hexkey.upper()

    def to_address(self):
        """
        This method will convert the public key to a bitcoin address.

        Returns:
            A bitcoin address for the public key
        """
        sha256digest = hashlib.sha256(str(self)).digest()
        ripemd160 = hashlib.new('ripemd160')
        ripemd160.update(sha256digest)
        ripemd160_digest = ripemd160.digest()

        # Prepend the version info
        ripemd160_digest = '\x00' + ripemd160_digest

        # Calc checksum
        checksum = hashlib.sha256(ripemd160_digest).digest()
        checksum = hashlib.sha256(checksum).digest()
        checksum = checksum[:4]

        # Append checksum
        address = ripemd160_digest + checksum
        address_bignum = int('0x' + address.encode('hex'), 16)
        return '1' + b58encode(address_bignum)

    def __repr__(self):
        return "<PublicKey address=[%s]>" % self.to_address()

    def __eq__(self, other):
        return self.to_hex() == other.to_hex()

    def __str__(self):
        """
        This method will convert the public key to
        a string representation.

        Returns:
            A string representation of the public key
        """
        return self.key_prefix + self.public_key.to_string()


class PrivateKey(object):
    """
    This is a representation for Bitcoin private keys. In this
    class you'll find methods to import/export keys from multiple
    formats. Use a hex string representation to construct a new PublicKey
    or use the clas methods to import from another format.
    """
    wif_prefix = '\x80'

    def __init__(self, hexkey=None):
        """
        Construct a new PrivateKey object, based optionally on an existing
        hex representation.

        Args:
            hexkey: The key in hex string format.  If one isn't
            provided, a new private key will be generated.
        """
        if hexkey:
            stringkey = hexkey.decode("hex")
            self.private_key = \
                ecdsa.SigningKey.from_string(stringkey, curve=ecdsa.SECP256k1)
        else:
            self.private_key = \
                ecdsa.SigningKey.generate(curve=ecdsa.SECP256k1)

    @classmethod
    def from_string(klass, stringkey):
        """
        This method will create a new Private Key using
        the specified string data.

        Args:
            stringkey: The key in string format

        Returns:
            A new PrivateKey
        """
        return klass(stringkey.encode("hex"))

    @classmethod
    def from_wif(klass, wifkey):
        """
        This method will create a new PrivateKey from a
        WIF format string.

        Args:
            wifkey: The private key in WIF format

        Returns:
            A new PrivateKey
        """
        hexkey = "%x" % b58decode(wifkey)
        checksum = hexkey[(-4 * 2):].decode("hex")
        key = hexkey[:(-4 * 2)].decode("hex")

        shafirst = hashlib.sha256(key).digest()
        shasecond = hashlib.sha256(shafirst).digest()

        if shasecond[:4] != checksum:
            raise KeyDecodeError("Invalid checksum for the address.")

        return klass(key[1:].encode("hex"))

    def to_hex(self):
        """
        This method will convert the Private Key to
        a hex string representation.

        Returns:
            Hex string representation of this PrivateKey
        """
        hexkey = self.private_key.to_string().encode("hex")
        return hexkey.upper()

    def to_wif(self):
        """
        This method will export the Private Key to
        WIF (Wallet Import Format).

        Returns:
            The PrivateKey in WIF format.
        """
        extendedkey = self.wif_prefix + str(self)
        shafirst = hashlib.sha256(extendedkey).digest()
        shasecond = hashlib.sha256(shafirst).digest()
        checksum = shasecond[:4]
        extendedkey = extendedkey + checksum
        key_bignum = int('0x' + extendedkey.encode('hex'), 16)
        return b58encode(key_bignum)

    def to_address(self):
        """
        Convert to public key and then get the public address for that key.
        """
        return self.get_public_key().to_address()

    def sign(self, data):
        """Digest and then sign the data."""
        digest = hashlib.sha256(hashlib.sha256(data).digest()).digest()
        sig = self.private_key.sign_digest(digest, sigencode=ecdsa.util.sigencode_der)
        # 01 is hashtype
        return sig + '\01'

    def get_public_key(self):
        """
        This method will create a new PublicKey based on this PrivateKey.

        Returns:
            A new PublicKey
        """
        return PublicKey.from_private_key(self)

    def __eq__(self, other):
        return self.to_hex() == other.to_hex()

    def __str__(self):
        """
        This method will convert the PrivateKey to
        a string representation.
        """
        return self.private_key.to_string()

    def __repr__(self):
        return "<PrivateKey hexkey=[%s]>" % self.to_hex()
