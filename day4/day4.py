import os
from time import perf_counter
t1_start = perf_counter()
filename = os.path.join(os.path.dirname(__file__), "input.txt")
f = open(filename, "r")
input = f.read().splitlines()
f.close()

# Parse input
def parse_inputs():
    global assignments
    assignments = []
    for pair in input:
        section_range = []
        elf_assignment = pair.split(',')
        for sections in elf_assignment:
            (x, y) = sections.split('-')
            section_range.append((int(x), int(y)))
        assignments.append(section_range)

# Helper function
def get_min_max(assignment):
    min_a = assignment[0][0]
    max_a = assignment[0][1]
    min_b = assignment[1][0]
    max_b = assignment[1][1]
    return min_a, max_a, min_b, max_b

# Helper function
def range_encapsulates(xmin, xmax, ymin, ymax):
    return (xmin <= ymin and xmax >= ymax) or (ymin <= xmin and ymax >= xmax)

# Solve
def solve_a():
    parse_inputs()
    counter = 0
    for assignment in assignments:
        min_a, max_a, min_b, max_b = get_min_max(assignment)
        if range_encapsulates(min_a, max_a, min_b, max_b):
            counter += 1
    return counter


# Solution Part A
print("Solution Part A:", solve_a())

# Part B
# Helper function
def range_overlaps(xmin, xmax, ymin, ymax):
    x, y = set(range(xmin, xmax+1)), set(range(ymin, ymax+1))
    return bool(x.intersection(y))

# Solve
def solve_b():
    parse_inputs()
    counter = 0
    for assignment in assignments:
        min_a, max_a, min_b, max_b = get_min_max(assignment)
        if range_overlaps(min_a, max_a, min_b, max_b):
            counter += 1
    return counter


# Solution part B
print("Solution Part B:", solve_b())
t1_stop = perf_counter()
print("Solution found in:", (t1_stop-t1_start).__round__(5), "s")
