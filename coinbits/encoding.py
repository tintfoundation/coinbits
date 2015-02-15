from collections import deque
from hashlib import sha256

BASE58_DIGITS = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'

def ones_prefix_length(s):    
    c = 0
    ls = deque(s)
    while ls and ls.popleft() == '1':
        c += 1
    return c

def base58_decode(s):
    result = 0
    for c in s:
        result = result * 58 + BASE58_DIGITS.index(c)
    return result    

def base256_encode(n):
    result = ''
    while n > 0:
        result = chr(n % 256) + result
        n /= 256
    return result

def base58_check_decode(s):
    ones = ones_prefix_length(s)
    s = base256_encode(base58_decode(s))
    result = '\0' * ones + s[:-4]
    checksum = sha256(sha256(result).digest()).digest()[0:4]
    assert(checksum == s[-4:])
    return result[1:]

def base58_encode(n):
    result = ''
    while n > 0:
        n, rem = divmod(n, 58)
        result = BASE58_DIGITS[rem] + result
    return result
