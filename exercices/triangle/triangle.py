import itertools


def _is_triangle(sides):
    return all(s > 0 for s in sides) and all(s1 + s2 > s3 for s1, s2, s3 in itertools.permutations(sides))


def equilateral(sides):
    return _is_triangle(sides) and all(s == sides[0] for s in sides)


def isosceles(sides):
    return _is_triangle(sides) and (sides[0] == sides[1] or sides[0] == sides[2] or sides[1] == sides[2])


def scalene(sides):
    return _is_triangle(sides) and not isosceles(sides)
