from coinbits.client import BitcoinClient
from coinbits.txns.keys import PrivateKey
from coinbits.txns.wallet import Teller
from coinbits.protocol.serializers import OutPoint


class MyClient(BitcoinClient):
    def connected(self):
        # build a teller that will spend from the given private key
        key = PrivateKey('e1385343f7ea362b0de7e5772a6c766d44ce4bf69e1380381630bf1892c638d5')
        teller = Teller(key)

        # specify the origin transaction hash and output index to use for this transaction's input
        hexouthash = '8ed9e37a3c585ad2b28ebc9a7a76ff0bf250bd4a1d19cb42f8d29d62da8d3e67'
        outpoint = OutPoint()
        outpoint.out_hash = int(hexouthash, 16)
        outpoint.index = 0

        # pay 2M Satoshis to 1wYiNC2EERnKPWP7QbvWGEfNprtHg1bsz
        tx = teller.make_standard_tx(outpoint, '1wYiNC2EERnKPWP7QbvWGEfNprtHg1bsz', 2000000)

        print "New transaction's hash:", tx.calculate_hash()
        self.send_message(tx)

    def handle_inv(self, message_header, message):
        print "Got some inventory:", message
        for txn in message.inventory:
            print txn

MyClient("bitcoin.sipa.be").loop()
