class Clock:
    def __init__(self, hour, minute):
        self.total: int = hour * 60 + minute    # in minutes

    def __repr__(self):
        hour, minute = (self.total // 60) % 24, self.total % 60
        return '{:02d}:{:02d}'.format(hour, minute)

    def __eq__(self, other):
        return repr(self) == repr(other)

    def __add__(self, minutes: int):
        self.total += minutes
        return self

    def __sub__(self, minutes: int):
        self.total -= minutes
        return self
