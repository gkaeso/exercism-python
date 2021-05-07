def square(number):
    if not 0 < number < 65: raise ValueError('invalid number')
    return 2 ** (number-1)


def total():
    # proof
    # x-1 = 2^0 + 2^1 + ... + 2^n
    # x = 2 (2^0) + 2^1 + ... + 2^n
    # x = 2 (2^1) + 2^2 + ... + 2^n
    # ...
    # x = 2 (2^n) = 2^(n+1)
    return 2 ** 64 - 1  # max square = 63 (64 squares from 0 to 63)
