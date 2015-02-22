import random


def nonce():
    """
    Return a random int between 0 and (2^32)-1
    """
    return random.randint(0, 4294967295)
