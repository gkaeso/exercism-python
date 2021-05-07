class Luhn:
    def __init__(self, card_num):
        self.number: str = card_num.replace(' ', '')

    def valid(self):
        if not self.number.isdigit() or len(self.number) < 2:
            return False

        total: int = 0
        for i, d in enumerate(self.number[::-1]):  # self.number[::-1] to start from the right
            val = int(d)

            if i % 2 == 1:
                val = 2 * int(val)
                if val > 9: val -= 9
            total += val

        return total % 10 == 0
