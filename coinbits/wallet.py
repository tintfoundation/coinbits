from hashlib import sha256

from protocoin.scripts import pay_to_pubkey_hash


class Wallet(object):
    def __init__(self, private_key):
        # private_key is a BitcoinPrivateKey
        self.private_key = private_key
        self.public_key = private_key.generate_public_key()
        self.address = self.public_key.to_address()

    def make_standard_tx(self, output, destination, amount, fee=10000):
        txin = TxIn()
        txin.previous_output = outpoint
        txin.signature_script = pay_to_pubkey_hash(self.address)

        txout = TxOut()
        txout.value = amount - fee
        txout.pk_script = pay_to_pubkey_hash(destination)

        tx = Tx()
        tx.version = 1
        tx.tx_in.append(txin)
        tx.tx_out.append(txout)

        raw = TxSerializer().serialize(tx).encode('hex') + "01000000"
        sig = self.private_key.sign(raw.decode('hex'))

        s = VariableStringField()
        s.parse(sig)
        txin.signature_script = s.serialize()

        s = VariableStringField()
        s.parse(pub.to_hex().decode('hex'))
        txin.signature_script += s.serialize()

        tx.tx_in = [txin]

        return TxSerializer().serialize(tx).encode('hex')





key = BitcoinPrivateKey('3C07AA429758984536F9C456E35B9853717FA482243B684FA40BED386E81F2FE')
wallet = Wallet(key)

outpoint = OutPoint()
outpoint.out_hash = int("40ba42f2df16b7c03a83bfd98874e29dd923b9908746e316f737f9108c02770d", 16)
outpoint.index = 0

tx = wallet.make_standard_tx(output, '14nDSrM8RoqCXXW95pq4BEnBHLDgSj87bD', 2000000)
