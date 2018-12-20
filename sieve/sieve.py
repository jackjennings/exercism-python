def sieve(limit):
    """
    sieve returns prime numbers up to and including the given limit,
    using the Sieve of Eratosthenes
    """

    grains = range(2, limit + 1)
    multiples = []
    primes = []

    for grain in grains:
        if grain not in multiples:
            primes.append(grain)
            multiples.extend(range(grain, limit + 1, grain))

    return primes
