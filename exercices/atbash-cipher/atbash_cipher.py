from string import ascii_lowercase


BLOCK_SIZE = 5


def _cipher(text):
    translation_table = str.maketrans(ascii_lowercase, ascii_lowercase[::-1])
    return ''.join([c.translate(translation_table) for c in text.replace(' ', '').lower() if c.isalnum()])


def encode(plain_text):
    encoded = _cipher(plain_text)
    return ' '.join(encoded[i:i + BLOCK_SIZE] for i in range(0, len(encoded), BLOCK_SIZE))


def decode(ciphered_text):
    return _cipher(ciphered_text)
