Quick Example
=============
Coinbits includes a basic client example for interacting on the peer-to-peer network.  Here's an example of a client that extends :py:mod:`~coinbits.client.BitcoinClient` and requests information on a block hash:

.. literalinclude:: ../examples/client.py

The :py:mod:`~coinbits.client.BitcoinClient.connected` method will be called as soon as the client has connected and finished handshaking.  The :py:mod:`~coinbits.protocol.serializers` module contains all of the messages that can be serialized on the network, like the :py:mod:`~coinbits.protocol.serializers.GetBlocks` message command (described `here <https://en.bitcoin.it/wiki/Protocol_specification#getblocks>`_).  In this case, the send_message and message_received methods have been overwritten just for debugging.  The handle_inv method is an example of the method dispatch - any message command type can have an associated handle_* method that will be called whenever a message of that type is received.
