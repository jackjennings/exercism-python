import math
from collections import namedtuple


class ComplexNumber(namedtuple("ComplexNumber", ["real", "imaginary"])):
    def __add__(self, other):
        (a, b), (c, d) = self, other

        return ComplexNumber((a + c), (b + d))

    def __mul__(self, other):
        (a, b), (c, d) = self, other

        return ComplexNumber((a * c - b * d), (b * c + a * d))

    def __sub__(self, other):
        (a, b), (c, d) = self, other

        return ComplexNumber((a - c), (b - d))

    def __truediv__(self, other):
        (a, b), (c, d) = self, other

        return ComplexNumber(
            (a * c + b * d) / (c ** 2 + d ** 2), (b * c - a * d) / (c ** 2 + d ** 2)
        )

    def __abs__(self):
        return math.sqrt(self.real ** 2 + self.imaginary ** 2)

    def __eq__(self, other):
        (a, b), (c, d) = self, other

        return a == c and b == d

    def __repr__(self):
        return f"<ComplexNumber {self.real} {self.imaginary}>"

    def conjugate(self):
        return ComplexNumber(self.real, -self.imaginary)

    def exp(self):
        return ComplexNumber(
            math.exp(self.real) * math.cos(self.imaginary),
            math.exp(self.real) * math.sin(self.imaginary),
        )
