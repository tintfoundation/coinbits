# Python Bitcoin Peer to Peer Library
[![Build Status](https://secure.travis-ci.org/8468/coinbits.png?branch=master)](https://travis-ci.org/8468/coinbits)
[![Docs Status](https://readthedocs.org/projects/coinbits/badge/?version=latest)](http://coinbits.readthedocs.org)

**Documentation can be found at [coinbits.readthedocs.org](http://coinbits.readthedocs.org/).**

This library provides the basic serialization / deserialization code necessary to operate as a peer on the Bitcoin network.  Many utilities are provided to help with buffering input, creating transactions, and key management.

This library could be used to do any of the following things easily:
 * To create a full Peer node that accepts and validates transactions, stores blocks, and responds to inventory requests
 * To query blocks from nodes on the network
 * To map the bitcoin network, asking each peer for a list of peers, then those peers for peers, etc.

Basically, anything that requires interaction on the P2P network could utilize this library.
