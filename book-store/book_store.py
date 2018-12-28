from collections import Counter

DISCOUNTS = {0: 0, 1: 0, 2: 0.05, 3: 0.10, 4: 0.20, 5: 0.25}


def calculate_total(books):
    counts = Counter(books)
    total = 0

    while counts:
        remaining = set(counts.elements())
        discount = DISCOUNTS[len(remaining)]
        subtotal = len(remaining) * 800

        total += subtotal - int(subtotal * discount)
        counts -= Counter(remaining)

    return total
