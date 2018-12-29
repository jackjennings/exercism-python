def transform(legacy_data):
    output = {}

    for score, letters in legacy_data.items():
        for letter in letters:
            output[letter.lower()] = score

    return output
