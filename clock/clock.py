class Clock(object):
    total: int

    def __init__(self, hour: int, minute: int):
        self.total = (hour * 60 + minute) % 1440

        if self.total < 0:
            self.total += 1440

    def __repr__(self) -> str:
        return "{:0>2}:{:0>2}".format(self.hours, self.minutes)

    def __eq__(self, other: 'Clock') -> bool:
        return self.total == other.total

    def __add__(self, minutes: int) -> 'Clock':
        return Clock(0, self.total + minutes)

    def __sub__(self, minutes: int) -> 'Clock':
        return Clock(0, self.total - minutes)

    @property
    def hours(self) -> int:
        return self.total // 60

    @property
    def minutes(self) -> int:
        return self.total % 60
