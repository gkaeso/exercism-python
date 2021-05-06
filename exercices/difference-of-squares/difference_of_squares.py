import itertools


def square_of_sum(number):
    return sum(range(1, number+1)) ** 2


def sum_of_squares(number):
    return sum(x*x for x in range(1, number+1))


def difference_of_squares(number):
    # calculate directly the result without taking into account the squared number (x2, y2...) 
    return sum([int(x) * int(y) for x, y in itertools.permutations(range(1, number+1), r=2)])
