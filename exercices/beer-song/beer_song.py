def main_paragraph(bottle_nb):
    bottle: str = f'{bottle_nb} bottles' if bottle_nb > 1 else '1 bottle'
    line_one: str = f'{bottle} of beer on the wall, {bottle} of beer.'

    bottle_minus_one: str
    if bottle_nb-1 == 0:
        bottle_minus_one = 'no more bottles'
    elif bottle_nb-1 == 1:
        bottle_minus_one = '1 bottle'
    else:
        bottle_minus_one = f'{bottle_nb-1} bottles'
    line_two: str = f'Take one down and pass it around, {bottle_minus_one} of beer on the wall.'

    line_two_last: str = f'Take it down and pass it around, no more bottles of beer on the wall.'

    return [line_one, line_two if bottle_nb > 1 else line_two_last]


def last_paragraph():
    return [
        'No more bottles of beer on the wall, no more bottles of beer.',
        'Go to the store and buy some more, 99 bottles of beer on the wall.'
    ]


def recite(start, take=1):
    song: list[str] = []
    bottle_nb: int = start

    for i in range(take):
        if i != 0: song.append('')

        if (remaining_bottles := bottle_nb-i) >= 1:
            song.extend(main_paragraph(remaining_bottles))
        else:
            song.extend(last_paragraph())

    return song

print(recite(start=2, take=3))

[
    '2 bottles of beer on the wall, 2 2 bottles of beer.',
    'Take one down and pass it around, 1 bottle of beer on the wall.',
    '',
    '1 bottle of beer on the wall, 1 1 bottle of beer.',
    'Take it down and pass it around, no more bottles of beer on the wall.',
    '',
    'No more bottles of beer on the wall, no more bottles of beer.',
    'Go to the store and buy some more, 99 bottles of beer on the wall.']

[
    "2 bottles of beer on the wall, 2 bottles of beer.",
    "Take one down and pass it around, 1 bottle of beer on the wall.",
    "",
    "1 bottle of beer on the wall, 1 bottle of beer.",
    "Take it down and pass it around, no more bottles of beer on the wall.",
    "",
    "No more bottles of beer on the wall, no more bottles of beer.",
    "Go to the store and buy some more, 99 bottles of beer on the wall.",
]