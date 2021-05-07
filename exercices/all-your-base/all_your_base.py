def _to_base(base, number) -> list[int]:
    output: list[int] = []

    while number > 0:
        output.append(number % base)
        number //= base

    return list(reversed(output)) if output else [0]


def _from_base(base, digits) -> int:
    return sum(digit * (base ** power) for power, digit in enumerate(reversed(digits)))


def rebase(input_base, digits, output_base):
    if input_base < 2 or output_base < 2:
        raise ValueError('invalid base')
    elif not all(input_base > d >= 0 for d in digits):
        raise ValueError('invalid digits')
    return _to_base(output_base, _from_base(input_base, digits))
