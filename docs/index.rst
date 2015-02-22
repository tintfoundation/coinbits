Coinbits Documentation
======================

.. note ::
    This library assumes you have a working familiarity with the `Bitcoin Protocol <https://en.bitcoin.it/wiki/Protocol_specification>`_.

Coinbits provides the basic serialization / deserialization code necessary to operate as a peer on the Bitcoin network.  Many utilities are provided to help with buffering input, creating transactions, and key management.

This library could be used to do any of the following things easily:

 * To create a full Peer node that accepts and validates transactions, stores blocks, and responds to inventory requests
 * To query blocks from nodes on the network
 * To map the bitcoin network, asking each peer for a list of peers, then those peers for peers, etc.

Basically, anything that requires interaction on the P2P network could utilize this library.

.. include:: quick_example.rst

Getting Started
===============
.. toctree::
   :maxdepth: 3
   :titlesonly:

   intro
   source/modules
   
	      
Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
