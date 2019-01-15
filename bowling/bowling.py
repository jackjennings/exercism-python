class BowlingGame(object):
    def __init__(self):
        self._frames = [BowlingFrame(1)]

    def roll(self, pins):
        if self.is_complete:
            raise IndexError("cannot add rolls to a complete game")

        self._frames = self._frames[0:-1] + self._frames[-1].add(pins)

    def score(self):
        if not self.is_complete:
            raise IndexError("game must be complete before scoring")

        total = 0

        for i, f in enumerate(self._frames):
            next = [roll for frame in self._frames[i + 1 :] for roll in frame.rolls]
            total += f.base_score + sum(next[0 : f.number_of_bonus_rolls])

        return total

    @property
    def is_complete(self):
        return len(self._frames) is 10 and self._frames[-1].is_complete


class BowlingFrame(object):
    def __init__(self, number, rolls=()):
        self._number = number
        self.rolls = rolls

        for pins in self.rolls:
            PinValueError.validate(pins)

        FrameValueError.validate(self.rolls)

    def __len__(self):
        return len(self.rolls)

    def __repr__(self):
        return f"<BowlingFrame #{self._number} {self.rolls}>"

    def add(self, pins):
        if self.is_complete:
            return [self, BowlingFrame(self._number + 1, (pins,))]
        else:
            return [BowlingFrame(self._number, (*self.rolls, pins))]

    @property
    def base_score(self):
        return sum(self.rolls)

    @property
    def is_complete(self):
        return len(self) == self.potential_number_of_rolls

    @property
    def is_last_frame(self):
        return self._number is 10

    @property
    def is_spare(self):
        return sum(self.rolls[:2]) == 10

    @property
    def is_strike(self):
        return sum(self.rolls[:1]) is 10

    @property
    def number_of_extra_rolls(self):
        if self.is_last_frame:
            return self.number_of_bonus_rolls
        else:
            return 0

    @property
    def number_of_bonus_rolls(self):
        if self.is_strike:
            return 2
        elif self.is_spare:
            return 1
        else:
            return 0

    @property
    def number_of_base_rolls(self):
        if self.is_strike:
            return 1
        else:
            return 2

    @property
    def potential_number_of_rolls(self):
        return self.number_of_base_rolls + self.number_of_extra_rolls


class PinValueError(ValueError):
    @classmethod
    def validate(cls, pins):
        if pins < 0 or pins > 10:
            raise cls(pins)

    def __init__(self, pins):
        super().__init__(
            "Roll cannot be {}, it must be between 0 and 10, inclusive".format(pins)
        )


class FrameValueError(ValueError):
    @classmethod
    def validate(cls, rolls):
        if len(rolls) is 0:
            return

        remaining_pins = 10 - sum(rolls[:-1]) % 10
        latest_roll = rolls[-1]

        if remaining_pins < latest_roll:
            raise cls(remaining_pins, latest_roll)

    def __init__(self, remaining_pins, roll):
        super().__init__(
            "Next rolls cannot be more than {}, got {}".format(remaining_pins, roll)
        )
