class PhoneNumber:
    def __init__(self, number):
        self.number = ''.join(digit for digit in number if digit.isnumeric())
        self._validate()

    def _validate(self) -> None:
        if len(self.number) == 10:
            if self.number[3] in ('0', '1'):
                raise ValueError('exchange code 0 and 1 not accepted')
            if self.number[0] in ('0', '1'):
                raise ValueError('country code 0 and 1 not accepted')
        elif len(self.number) == 11:
            if self.number[0] == '1':
                self.number = self.number[1:]
            else:
                raise ValueError('country code does not start with 1')
            if self.number[3] in ('0', '1'):
                raise ValueError('exchange code 0 and 1 not accepted')
            if self.number[0] in ('0', '1'):
                raise ValueError('country code 0 and 1 not accepted')
        else:
            raise ValueError('invalid number')

    @property
    def area_code(self) -> str:
        return self.number[:3]

    def pretty(self) -> str:
        return f'({self.number[:3]})-{self.number[3:6]}-{self.number[6:]}'
