import re


def abbreviate(words):
    return ''.join([w[0] for w in re.findall(r"[A-Z]+", words.upper()) if w != "S"])
