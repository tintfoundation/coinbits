from cStringIO import StringIO
from .serializers import *
from .exceptions import NodeDisconnectException
import os


class MyClient(BitcoinClient):
    """This class implements all the protocol rules needed
    for a client to stay up in the network. It will handle
    the handshake rules as well answer the ping messages."""

    def handshake(self):
        """This method will implement the handshake of the
        Bitcoin protocol. It will send the Version message."""
        version = Version()
        self.send_message(version)

    def handle_version(self, message_header, message):
        """This method will handle the Version message and
        will send a VerAck message when it receives the
        Version message.

        :param message_header: The Version message header
        :param message: The Version message
        """
        verack = VerAck()
        self.send_message(verack)

    def handle_ping(self, message_header, message):
        """This method will handle the Ping message and then
        will answer every Ping message with a Pong message
        using the nonce received.

        :param message_header: The header of the Ping message
        :param message: The Ping message
        """
        pong = Pong()
        pong.nonce = message.nonce
        self.send_message(pong)
