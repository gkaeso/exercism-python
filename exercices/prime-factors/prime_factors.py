def factors(value):
    factor_lst: list[int] = []

    factor = 2
    while value > 1:
        if value % factor == 0:
            factor_lst.append(factor)
            value //= factor
            factor = 2
        else:
            factor += 1

    return factor_lst
