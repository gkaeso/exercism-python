def classify(number):
    return _classify(number) if number != 1 else 'deficient'


def _classify(number) -> str:
    classif: str

    aliquot: int = _aliquot(number)
    if aliquot > number:
        classif = 'abundant'
    elif aliquot < number:
        classif = 'deficient'
    else:
        classif = 'perfect'

    return classif


def _factor_gen(number):
    yield 1                         # always a divisor
    for n in range(2, int(number ** 0.5) + 1):
        if number % n == 0:         # is a divisor
            yield n
            if n * n != number:     # is a divisor and not the square root
                yield number // n


def _aliquot(number) -> int:
    if number < 1: raise ValueError('invalid number')
    return sum(_factor_gen(number))
