def grep(pattern, filepaths, flags=""):
    options = flags.split(" ")
    printLineNumbers = "-n" in options
    caseInsensitive = "-i" in options
    printFilenames = "-l" in options
    matchEntireLine = "-x" in options
    inverted = "-v" in options

    matches = []

    matcher = equals if matchEntireLine else search
    pattern = pattern.lower() if caseInsensitive else pattern

    for filepath in filepaths:
        with open(filepath, "r") as file:
            for number, line in enumerate(file.readlines(), start=1):
                content = line.lower() if caseInsensitive else line
                matched = matcher(pattern, content)

                if (inverted and not matched) or (not inverted and matched):
                    if printFilenames:
                        matches.append("{}\n".format(filepath))
                        break
                    else:
                        prefixes = []

                        if len(filepaths) > 1:
                            prefixes.append(filepath)

                        if printLineNumbers:
                            prefixes.append(str(number))

                        prefix = "{}:".format(":".join(prefixes)) if prefixes else ""

                        matches.append("{}{}".format(prefix, line))

    return "".join(matches)


def search(pattern, text):
    return pattern in text


def equals(pattern, text):
    return pattern == text.rstrip()
