from coinbits.encoding import base58_check_decode


def pay_to_pubkey_hash(key):
    """
    76       A9             14
    OP_DUP OP_HASH160    Bytes to push

    89 AB CD EF AB BA AB BA AB BA AB BA AB BA AB BA AB BA AB BA   88         AC
                     Data to push                     OP_EQUALVERIFY OP_CHECKSIG
    """
    h = '76a914' + base58_check_decode(key).encode('hex') + '88ac'
    return h.decode('hex')
