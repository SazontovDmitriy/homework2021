import copy

A = 'acc'
J = 'jmp'
N = 'nop'


def run(instructions: list) -> [bool, int]:
    accumulator = 0
    visited = [False for _ in instructions]
    ix = 0
    while (0 <= ix < len(instructions)) and (not visited[ix]):
        visited[ix] = True
        operation, arg = instructions[ix]
        if operation == A:
            accumulator += arg
            ix += 1
        elif operation == J:
            ix += arg
        elif operation == N:
            ix += 1

    is_terminated = ix == len(instructions)
    return is_terminated, accumulator


def p1(instructions):
    _, accumulator = run(instructions)
    return accumulator


def p2(instructions):
    for ix, instruction in enumerate(instructions):
        operation, arg = instruction
        if operation in (N, J):
            instructions_copy = copy.deepcopy(instructions)
            instructions_copy[ix][0] = J if operation == N else N
    return 0


def extract_data(lines: list) -> list:
    instructions = []
    for line in lines:
        operation, arg = line.split(' ')
        instructions.append([operation, int(arg)])

    return instructions


with open('input.txt') as f:
    inputs = [
        line
        for line in f.read().splitlines()
    ]
    print(p2(extract_data(inputs)))



