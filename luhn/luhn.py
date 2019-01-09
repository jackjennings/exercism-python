from string import whitespace


WHITESPACE_FILTER = dict.fromkeys(map(ord, whitespace))


class Luhn(object):
    def __init__(self, card_number):
        self.card_number = card_number.translate(WHITESPACE_FILTER)

    def is_valid(self):
        try:
            return len(self.card_number) >= 2 and self.checksum == 0
        except ValueError as e:
            return False

    @property
    def card_numbers(self):
        return [int(d) for d in list(self.card_number)]

    @property
    def checksum(self):
        return sum(self.digits) % 10

    @property
    def digits(self):
        return [Digit(l, i) for i, l in enumerate(reversed(self.card_numbers))]


class Digit(object):
    def __init__(self, base, index):
        self.base = base
        self.index = index

    def __radd__(self, other):
        return self.value + other

    @property
    def multiplier(self):
        return self.index % 2 + 1

    @property
    def value(self):
        return self._clamp(self.base * self.multiplier)

    def _clamp(self, value):
        if value > 9:
            return value - 9
        else:
            return value
