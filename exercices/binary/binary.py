def parse_binary(binary_string):
    if not all(char in ('0', '1') for char in binary_string):
        raise ValueError('invalid binary number')
    return sum(int(digit) * (2 ** power) for power, digit in enumerate(reversed(binary_string)))
