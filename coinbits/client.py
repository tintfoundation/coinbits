import socket

from coinbits.protocol.exceptions import NodeDisconnectException
from coinbits.protocol.buffer import ProtocolBuffer
from coinbits.protocol.serializers import Version, VerAck, Pong


class BitcoinClient(object):
    """
    The base class for a Bitcoin network client.  This class
    will handle the initial handshake and responding to pings.
    """

    coin = "bitcoin"

    def __init__(self, peerip, port=8333):
        self.buffer = ProtocolBuffer()

        # connect
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((peerip, port))

        # send our version
        self.send_message(Version())

    def handle_version(self, message_header, message):
        """
        This method will handle the Version message and
        will send a VerAck message when it receives the
        Version message.

        Args:
            message_header: The Version message header
            message: The Version message
        """
        self.send_message(VerAck())

    def handle_ping(self, message_header, message):
        """This method will handle the Ping message and then
        will answer every Ping message with a Pong message
        using the nonce received.

        Args:
            message_header: The header of the Ping message
            message: The Ping message
        """
        pong = Pong()
        pong.nonce = message.nonce
        self.send_message(pong)

    def handle_message_header(self, message_header, payload):
        """
        This method will be called for every message before the
        message payload deserialization.

        Args:
            message_header: The message header
            payload: The payload of the message
        """
        pass

    def send_message(self, message):
        """
        This method will serialize the message using the
        appropriate serializer based on the message command
        and then it will send it to the socket stream.

        :param message: The message object to send
        """
        self.socket.sendall(message.get_message(self.coin))

    def loop(self):
        """
        This is the main method of the client, it will enter
        in a receive/send loop.
        """

        while True:
            data = self.socket.recv(1024 * 8)

            if len(data) <= 0:
                raise NodeDisconnectException("Node disconnected.")

            self.buffer.write(data)
            message_header, message = self.buffer.receive_message()

            if message_header is not None:
                self.handle_message_header(message_header, data)

            if not message:
                continue

            handle_func_name = "handle_" + message_header.command
            handle_func = getattr(self, handle_func_name, None)
            if handle_func:
                handle_func(message_header, message)
