import os
from time import perf_counter

t1_start = perf_counter()
filename = os.path.join(os.path.dirname(__file__), "input.txt")
f = open(filename, "r")
input = f.read().splitlines()
f.close()

input_stacks = input[0:8]
instructions = input[10:]


def parse_instructions():
    global stacks
    global instructions_short
    instructions_short = []
    stacks = list([] for i in range(1, 10))

    # Flip the input stacks into 2D list
    for row in input_stacks:
        blocks = [row[i:i+4] for i in range(0, len(row)+1, 4)]
        for (idx, block) in enumerate(blocks):
            if block[1] != ' ':
                stacks[idx].insert(0, block[1])
    for instruction in instructions:
        parsed_inst = [int(x) for x in instruction.split() if x.isdigit()]
        instructions_short.append(parsed_inst)


def move_blocks(n, start, stop):

    # Pop blocks from original stack
    selected_stack = stacks[start-1]
    blocks_in_transit = [selected_stack.pop() for block in selected_stack[-n:]]

    # Append to new stack
    for block in blocks_in_transit:
        stacks[stop-1].append(block)


def solve_a():
    parse_instructions()
    for n, start, stop in instructions_short:
        move_blocks(n, start, stop)
    solution = ''
    for stack in stacks:
        solution += stack[-1]
    return solution


print("Part A solution:", solve_a())


def batch_move_blocks(n, start, stop):

    # Pop blocks from original stack
    selected_stack = stacks[start-1]
    blocks_in_transit = [selected_stack.pop() for block in selected_stack[-n:]]

    # Append to new stack in reverse order
    blocks_in_transit.reverse()
    for block in blocks_in_transit:
        stacks[stop-1].append(block)


def solve_b():
    parse_instructions()
    for n, start, stop in instructions_short:
        batch_move_blocks(n, start, stop)
    solution = ''
    for stack in stacks:
        solution += stack[-1]
    return solution


print("Part B solution:", solve_b())
t1_stop = perf_counter()
print("Solution found in:", (t1_stop-t1_start).__round__(5), "s")
