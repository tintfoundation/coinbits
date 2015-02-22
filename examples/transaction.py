from coinbits.txns.keys import PrivateKey
from coinbits.txns.wallet import Teller
from coinbits.protocol.serializers import OutPoint, TxSerializer

# build a teller that will spend from the given private key
key = PrivateKey('e1385343f7ea362b0de7e5772a6c766d44ce4bf69e1380381630bf1892c638d5')
teller = Teller(key)

# now, specify the Transaction hash and output index to use for this transaction
outpoint = OutPoint()
outpoint.out_hash = int("8ed9e37a3c585ad2b28ebc9a7a76ff0bf250bd4a1d19cb42f8d29d62da8d3e67", 16)
outpoint.index = 0

# pay 2M Satoshis to 1wYiNC2EERnKPWP7QbvWGEfNprtHg1bsz
tx = teller.make_standard_tx(outpoint, '1wYiNC2EERnKPWP7QbvWGEfNprtHg1bsz', 2000000)

# print the Transaction
print TxSerializer().serialize(tx).encode('hex')
