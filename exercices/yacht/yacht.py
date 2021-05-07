YACHT, ONES, TWOS, THREES, FOURS, FIVES, SIXES, FULL_HOUSE, FOUR_OF_A_KIND, LITTLE_STRAIGHT, BIG_STRAIGHT, CHOICE = range(12)


def _get_score_for_number(dice, category) -> int:
    """This functions returns the score for categories from ONES to SIXES."""
    return sum(d for d in dice if d == category)


def _get_score_four_of_a_kind(dice) -> int:
    dice = sorted(dice)

    value: int = 0
    if len(set(dice)) == 1:         # four of a kind
        value = sum(dice[1:])
    elif len(set(dice)) == 2:
        if dice[0] != dice[1]:      # four of a kind
            value = sum(dice[1:])
        elif dice[3] != dice[4]:    # four of a kind
            value = sum(dice[:4])

    return value


def score(dice, category):
    score_value: int

    if category == YACHT:
        score_value = 50 if all(d == dice[0] for d in dice) else 0
    elif category in (ONES, TWOS, THREES, FOURS, FIVES, SIXES):
        score_value = _get_score_for_number(dice, category)
    elif category == FULL_HOUSE:
        score_value = sum(dice) if len(set(dice)) == 2 and (dice[1] != dice[2] or dice[2] != dice[3]) else 0
    elif category == FOUR_OF_A_KIND:
        score_value = _get_score_four_of_a_kind(dice)
    elif category == LITTLE_STRAIGHT:
        score_value = 30 if set(dice) == {1, 2, 3, 4, 5} else 0
    elif category == BIG_STRAIGHT:
        score_value = 30 if set(dice) == {2, 3, 4, 5, 6} else 0
    elif category == CHOICE:
        score_value = sum(dice)
    else:
        raise ValueError('invalid category')

    return score_value
