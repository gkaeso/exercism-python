def _is_anagram(word, candidate):
    return candidate != word and sorted(candidate) == sorted(word)


def find_anagrams(word, candidates):
    return [c for c in candidates if _is_anagram(word.upper(), c.upper())]
