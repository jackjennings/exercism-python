class CustomSet(object):
    def __init__(self, elements=[]):
        self._cache = {}

        for element in elements:
            self.add(element)

    def add(self, element):
        self._cache[element] = 0

    def intersection(self, other):
        return CustomSet(f for f in self if f in other)

    def isdisjoint(self, other):
        return not any(f in other for f in self)

    def isempty(self):
        return len(self) == 0

    def issubset(self, other):
        return self.isempty() or all(f in other for f in self)

    def __add__(self, other):
        return CustomSet([*self, *other])

    def __contains__(self, element):
        return element in self._cache

    def __eq__(self, other):
        return len(self) == len(other) and self.issubset(other)

    def __iter__(self):
        return iter(self._cache.keys())

    def __len__(self):
        return len(self._cache.keys())

    def __repr__(self):
        return f"<CustomSet {list(self._cache.keys())}>"

    def __sub__(self, other):
        return CustomSet(f for f in self if f not in other)
