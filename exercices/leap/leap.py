def leap_year(year):
    is_leap: bool = False

    if year % 4 == 0:
        if year % 100 != 0:
            is_leap = True
        elif year % 400 == 0:
            is_leap = True

    return is_leap
