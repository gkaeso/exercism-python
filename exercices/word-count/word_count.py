import re


def count_words(sentence):
    words: list[str] = [match.group(0) for match in re.finditer(r"[a-z0-9]+(['][a-z]+)?", sentence.lower())]
    word_occurrences: dict[str, int] = {word: 0 for word in words}
    for word in words:
        word_occurrences[word] += 1

    return word_occurrences
