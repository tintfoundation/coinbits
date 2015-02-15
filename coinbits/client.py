from coinbits.protocol.exceptions import NodeDisconnectException
from coinbits.protocol.buffer import ProtocolBuffer


class BitcoinClient(object):
    """The base class for a Bitcoin network client, this class
    implements utility functions to create your own class.

    :param socket: a socket that supports the makefile()
                   method.
    """

    coin = "bitcoin"

    def __init__(self, socket):
        self.socket = socket
        self.buffer = ProtocolBuffer()

    def close_stream(self):
        """This method will close the socket stream."""
        self.socket.close()

    def handle_message_header(self, message_header, payload):
        """This method will be called for every message before the
        message payload deserialization.

        :param message_header: The message header
        :param payload: The payload of the message
        """
        pass

    def send_message(self, message):
        """This method will serialize the message using the
        appropriate serializer based on the message command
        and then it will send it to the socket stream.

        :param message: The message object to send
        """
        self.socket.sendall(message.get_message(self.coin))

    def loop(self):
        """This is the main method of the client, it will enter
        in a receive/send loop."""

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
