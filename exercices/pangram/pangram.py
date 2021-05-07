import re
import string


def is_pangram(sentence):
    only_letters: str = re.sub(r"[^a-z]", "", sentence.lower())
    return len(set(list(only_letters))) == len(string.ascii_lowercase)
