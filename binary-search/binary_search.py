from typing import List


def binary_search(list_of_numbers: List[int], number: int) -> int:
    if not list_of_numbers:
        raise ValueError("{} not found".format(number))

    index = len(list_of_numbers) // 2
    candidate = list_of_numbers[index]

    if candidate == number:
        return index
    elif candidate < number:
        return index + 1 + binary_search(list_of_numbers[index+1:], number)
    else:
        return binary_search(list_of_numbers[0:index], number)
