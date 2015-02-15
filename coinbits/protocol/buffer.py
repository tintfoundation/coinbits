import os
from cStringIO import StringIO

from coinbits.protocol.serializers import MessageHeaderSerializer, getSerializer


class ProtocolBuffer(object):
    def __init__(self):
        self.buffer = StringIO()
        self.header_size = MessageHeaderSerializer.calcsize()

    def write(self, data):
        self.buffer.write(data)

    def receive_message(self):
        """This method will attempt to extract a header and message.
        It will return a tuple of (header, message) and set whichever
        can be set so far (None otherwise).
        """
        # Calculate the size of the buffer
        self.buffer.seek(0, os.SEEK_END)
        buffer_size = self.buffer.tell()

        # Check if a complete header is present
        if buffer_size < self.header_size:
            return (None, None)

        # Go to the beginning of the buffer
        self.buffer.reset()

        message_model = None
        message_header_serial = MessageHeaderSerializer()
        message_header = message_header_serial.deserialize(self.buffer)
        total_length = self.header_size + message_header.length

        # Incomplete message
        if buffer_size < total_length:
            self.buffer.seek(0, os.SEEK_END)
            return (message_header, None)

        payload = self.buffer.read(message_header.length)
        remaining = self.buffer.read()
        self.buffer = StringIO()
        self.buffer.write(remaining)
        payload_checksum = MessageHeaderSerializer.calc_checksum(payload)

        # Check if the checksum is valid
        if payload_checksum != message_header.checksum:
            raise RuntimeError("Bad message checksum")

        deserializer = getSerializer(message_header.command)
        message_model = deserializer.deserialize(StringIO(payload))

        return (message_header, message_model)
