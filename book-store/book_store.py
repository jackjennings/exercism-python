from collections import Counter


DISCOUNTS = {0: 0, 1: 0, 2: 0.05, 3: 0.10, 4: 0.20, 5: 0.25}


def calculate_total(books):
    counts = Counter(books)
    total = 0

    while counts:
        group = frozenset(counts.elements())
        total += price(group, discount(group, default=0.25))
        counts -= Counter(group)

    return total


def discount(items, default):
    count = len(items)
    return DISCOUNTS[count] if count in DISCOUNTS else default


def price(items, discount):
    subtotal = len(items) * 800
    return subtotal - int(subtotal * discount)
