# Python Bitcoin Peer to Peer Library
[![Build Status](https://secure.travis-ci.org/8468/coinbits.png?branch=master)](https://travis-ci.org/8468/coinbits)
[![Docs Status](https://readthedocs.org/projects/coinbits/badge/?version=latest)](http://coinbits.readthedocs.org)

**Full documentation can be found at [coinbits.readthedocs.org](http://coinbits.readthedocs.org/).**

This library provides the basic serialization / deserialization code necessary to operate as a peer on the Bitcoin network.  Many utilities are provided to help with buffering input, creating transactions, and key management.

This library could be used to do any of the following things easily:
 * To create a full Peer node that accepts and validates transactions, stores blocks, and responds to inventory requests
 * To query blocks from nodes on the network
 * To map the bitcoin network, asking each peer for a list of peers, then those peers for peers, etc.

Basically, anything that requires interaction on the P2P network could utilize this library.

## Installation

```
pip install coinbits
```

## Usage
There is a basic client implementation that can be easily extended to provide basic interactions on the P2P network.  The example below will connect to the network and then, on connection, get a block for inspection.

```python
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
        block = '00000000000000000f69e991ee47a3536770f5d452967ec7edeb8d8cb28f9f28'
        gh = GetBlocks([ int(block, 16) ])
        self.send_message(gh)

    def handle_inv(self, message_header, message):
        print "Got some inventory:", message

# connect, and then run a processing loop
MyClient("bitcoin.sipa.be").loop()
```

Check out the examples folder for other examples.

## Running Tests
This example uses the unit test runner with [Twisted](https://twistedmatrix.com), but you can use anything capable of running UnitTest tests.  To run tests:

```
pip install twisted
trial coinbits
```

## Thanks
Thanks to Christian S. Perone who provided the basis for this project, [Protocoin](https://github.com/perone/protocoin).  Coinbits is a fork and revamp of that project.
