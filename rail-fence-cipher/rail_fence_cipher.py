from typing import List


def encode(message: str, rails: int) -> str:
    letters = list(message)

    return "".join(letters[i] for i in sequence(len(letters), rails))


def decode(encoded_message: str, rails: int) -> str:
    letters = list(encoded_message)
    output = [""] * len(letters)

    for i, x in enumerate(sequence(len(letters), rails)):
        output[x] = letters[i]

    return "".join(output)


def sequence(length: int, rails: int) -> List[int]:
    rows: List[List[int]] = [[] for _ in range(rails)]

    for i in range(length):
        rail = (rails - 1) - abs((rails - 1) - i % ((rails - 1) * 2))
        rows[rail].append(i)

    return [i for row in rows for i in row]
