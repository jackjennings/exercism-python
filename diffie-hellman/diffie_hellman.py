import secrets


def private_key(p):
    return randbetween(2, p)


def public_key(p, g, private):
    return g**private % p


def secret(p, public, private):
    return public**private % p


def randbetween(x, y):
    return secrets.randbelow(y - x) + x
