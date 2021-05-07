def steps(number):
    if number <= 0:
        raise ValueError('invalid input')

    step_nb: int = 0

    while number != 1:
        if number % 2:
            number = 3 * number + 1
        else:
            number /= 2

        step_nb += 1

    return step_nb
