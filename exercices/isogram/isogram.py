import re


def is_isogram(string):
    only_letters: str = re.sub(r"[^a-z]", "", string.lower())
    return len(only_letters) == len(set(list(only_letters)))
