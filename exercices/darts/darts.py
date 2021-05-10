from math import sqrt


def score(x, y) -> int:
    value: int = 0
    
    distance_from_origin: float = sqrt(x ** 2 + y ** 2)

    if distance_from_origin <= 1.0:
        value = 10
    elif distance_from_origin <= 5.0:
        value = 5
    elif distance_from_origin <= 10.0:
        value = 1

    return value
