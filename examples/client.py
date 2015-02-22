from coinbits.client import BitcoinClient
from coinbits.protocol.serializers import GetBlocks


class MyClient(BitcoinClient):
    def message_received(self, message_header, message):
        print "Got a message:", message_header.command, message
        super(MyClient, self).message_received(message_header, message)

    def send_message(self, message):
        print "Sending a message:", str(message)
        super(MyClient, self).send_message(message)

    def connected(self):
        hash = int('00000000000000000f69e991ee47a3536770f5d452967ec7edeb8d8cb28f9f28', 16)
        gh = GetBlocks([hash])
        self.send_message(gh)

    def handle_inv(self, message_header, message):
        print "Got some inventory:", message

MyClient("bitcoin.sipa.be").loop()
