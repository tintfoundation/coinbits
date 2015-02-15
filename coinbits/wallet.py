from coinbits.scripts import pay_to_pubkey_hash
from coinbits.protocol.serializers import TxIn, TxOut, Tx, TxSerializer
from coinbits.protocol.fields import VariableStringField


class Wallet(object):
    def __init__(self, private_key):
        # private_key is a BitcoinPrivateKey
        self.private_key = private_key
        self.public_key = private_key.generate_public_key()
        self.address = self.public_key.to_address()

    def make_standard_tx(self, output, destination, amount, fee=10000):
        txin = TxIn()
        txin.previous_output = output
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
        s.parse(self.public_key.to_hex().decode('hex'))
        txin.signature_script += s.serialize()

        tx.tx_in = [txin]

        return TxSerializer().serialize(tx).encode('hex')
