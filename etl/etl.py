from typing import Dict, List


def transform(legacy_data: Dict[int, List[str]]) -> Dict[str, int]:
    output = {}

    for score, letters in legacy_data.items():
        for letter in letters:
            output[letter.lower()] = score

    return output
