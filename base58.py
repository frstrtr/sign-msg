from collections import deque

BASE58 = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'


def encode(n, syms):
    base = len(syms)
    digits = deque()
    while n:
        n, r = divmod(n, base)
        digits.appendleft(syms[r])
    return ''.join(digits)


def b58encode(n):
    return encode(n, BASE58)


def decode(n, syms):
    base = len(syms)
    lookup = {e:i for i, e in enumerate(syms)}
    result = 0
    for char in n:
        result *= base
        result += lookup[char]
    return result


def b58decode(n):
    return decode(n, BASE58)


def test():
    n_ = '5HueCGU8rMjxEXxiPuD5BDku4MkFqeZyd4dZ1jvhTVqvbTLvyTJ'
    n = 0x800C28FCA386C7A227600B2FE50B7CAE11EC86D3BF1FBE471BE89827E19D72AA1D507A5B8D
    assert b58encode(n) == n_
    assert b58decode(n_) == n

if __name__ == '__main__':
    test()
