import os
from time import perf_counter
t1_start = perf_counter()
filename = os.path.join(os.path.dirname(__file__), "input.txt")

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
            if len(set(buffer)) == 4:
                return idx+1


print("Part A solution: ", solve_a())


def solve_b():
    buffer = []
    for idx, i in enumerate(input):
        buffer.insert(0, i)
        if len(buffer) > 14:
            buffer.pop()
            if len(set(buffer)) == 14:
                return idx+1


print("Part B solution: ", solve_b())
t1_stop = perf_counter()
print("Solution reached in:", round(t1_stop-t1_start, 5), 's')
