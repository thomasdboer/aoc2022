import os
from time import perf_counter
t1_start = perf_counter()
filename = os.path.join(os.path.dirname(__file__), "input.txt")


markers = []


def markindex(idx):
    return (idx)


def is_marker(buffer, size):
    if len(set(buffer)) == size:
        return True


def read_input():
    global input
    f = open(filename, "r")
    input = f.read().rstrip('\n')
    f.close()


def solve_a():
    read_input()
    buffer = []
    # O(i)
    for idx, i in enumerate(input):
        # insert() and pop() are O(1)
        buffer.insert(0, i)
        if len(buffer) > 4:
            buffer.pop()
            if is_marker(buffer, 4):
                return idx+1


print("Part A solution: ", solve_a())
t1_stop = perf_counter()


def solve_b():
    buffer = []
    for idx, i in enumerate(input):
        buffer.insert(0, i)
        if len(buffer) > 14:
            buffer.pop()
            if is_marker(buffer, 14):
                return idx+1


print("Part B solution: ", solve_b())

print("Solution reached in: ", t1_stop-t1_start)
