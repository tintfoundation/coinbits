Installation
==================

The easiest (and best) way to install coinbits is through `pip <http://www.pip-installer.org/>`_::

  $ pip install coinbits
      

.. include:: quick_example.rst

Sending a Transaction
=====================
Creating a transaction and sending it on the network is pretty straightforward.  All you need to know is the private key that will be "sending" the money, the receipient's address, and the output transaction to use as the input for this transaction.  Here's an example that sends 2M Satoshis after connecting to the P2P network:

.. literalinclude:: ../examples/sendmoney.py

Running Tests
=============

To run tests::

  $ trial coinbits

