from string import whitespace


class Luhn(object):
    def __init__(self, card_number):
        self.card_number = card_number

    def is_valid(self):
        try:
            return len(self.sanitized_card_number) >= 2 and self.checksum == 0
        except ValueError as e:
            return False

    @property
    def checksum(self):
        return sum(Digit(l, i) for i, l in enumerate(reversed(self.digits))) % 10

    @property
    def digits(self):
        return [int(d) for d in list(self.sanitized_card_number)]

    @property
    def sanitized_card_number(self):
        return self.card_number.translate(dict.fromkeys(map(ord, whitespace)))


class Digit(object):
    def __init__(self, value, index):
        self.value = value
        self.index = index

    def __radd__(self, other):
        return self._clamp(self.value * self._multiplier(self.index)) + other

    def _multiplier(self, index):
        return index % 2 + 1

    def _clamp(self, value):
        if value > 9:
            return value - 9
        else:
            return value
