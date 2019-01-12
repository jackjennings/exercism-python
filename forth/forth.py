class StackUnderflowError(Exception):
    pass


def evaluate(input_data):
    stack = []

    commands = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide,
        "dup": duplicate,
        "drop": drop,
        "swap": swap,
        "over": over,
    }

    while input_data:
        commands, stack, input_data = execute(commands, stack, input_data)

    return stack


def execute(commands, stack, lines):
    if not lines:
        return stack

    line, *lines = lines

    if line[0] == ":":
        keyword, procedure = line[2:-2].split(None, 1)

        return define(commands, keyword, procedure), stack, lines
    else:
        return commands, append(commands, stack, line), lines


def append(commands, stack, line):
    tokens = [s.lower() for s in line.split()]

    for token in tokens:
        if token in commands:
            stack = run(commands, stack, token)
        elif token.isdigit():
            stack = stack + [int(token)]
        else:
            raise ValueError("undefined token: {}".format(token))

    return stack


def run(commands, stack, token):
    try:
        return commands[token](stack)
    except ValueError:
        raise StackUnderflowError("not enough values to use {}".format(token))


def define(commands, keyword, procedure):
    if keyword.isdigit():
        raise ValueError("function keyword cannot be a digit: {}".format(keyword))

    return {
        **commands,
        keyword.lower(): lambda stack: append(commands, stack, procedure),
    }


# COMMANDS


def add(stack):
    *stack, x, y = stack
    return stack + [x + y]


def subtract(stack):
    *stack, x, y = stack
    return stack + [x - y]


def multiply(stack):
    *stack, x, y = stack
    return stack + [x * y]


def divide(stack):
    *stack, x, y = stack
    return stack + [x // y]


def duplicate(stack):
    *stack, x = stack
    return stack + [x, x]


def drop(stack):
    *stack, _ = stack
    return stack


def swap(stack):
    *stack, x, y = stack
    return stack + [y, x]


def over(stack):
    *stack, x, y = stack
    return stack + [x, y, x]
