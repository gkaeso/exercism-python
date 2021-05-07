def decode(string):
    decoded: list[str] = []

    number: str = ''
    for char in string:
        if char.isnumeric():
            number += char
        else:
            if not number:
                number = '1'
            decoded.append(int(number) * char)
            number = ''

    return ''.join(decoded)


def encode(string):
    def _format(char, char_nb) -> str:
        return f'{char_nb}{char}' if char_nb > 1 else f'{char}'

    encoded: list[str] = []

    if string == '':
        encoded.append('')
    else:
        char, char_nb = string[0], 0
        for c in string:
            if c == char:
                char_nb += 1
            else:
                encoded.append(_format(char, char_nb))
                char, char_nb = c, 1

        encoded.append(_format(char, char_nb))

    return ''.join(encoded)
