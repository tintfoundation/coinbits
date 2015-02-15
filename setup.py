#!/usr/bin/env python
from setuptools import setup, find_packages
from coinbits import version

setup(
    name="coinbits",
    version=version,
    description="A Python library for bitcoin peer to peer communication",
    author="Brian Muller",
    author_email="bamuller@gmail.com",
    license="MIT",
    url="http://github.com/8468/coinbits",
    packages=find_packages(),
    requires=['ecdsa'],
    install_requires=['ecdsa>=0.13']
)
