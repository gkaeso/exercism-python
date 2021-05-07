def trinary(string):
    return sum(int(digit) * (3 ** power) for power, digit in enumerate(reversed(string))) if all(int(d) < 3 for d in string) else 0
