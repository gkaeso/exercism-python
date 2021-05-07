from collections.abc import Iterable


def flatten(iterable):
    flattened: list = []

    for item in iterable:
        if isinstance(item, Iterable):
            flattened.extend(flatten(item))
        elif item is not None:
            flattened.append(item)

    return flattened
