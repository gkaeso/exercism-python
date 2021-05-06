def response(hey_bob):
    res: str

    hey_bob = hey_bob.strip()

    if hey_bob.isupper() and hey_bob.endswith('?'):
        res = "Calm down, I know what I'm doing!"
    elif hey_bob.isupper():
        res = "Whoa, chill out!"
    elif hey_bob.endswith('?'):
        res = "Sure."
    elif hey_bob == '':
        res = "Fine. Be that way!"
    else:
        res = "Whatever."

    return res
