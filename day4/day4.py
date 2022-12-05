import os
filename = os.path.join(os.path.dirname(__file__), "input.txt")
f = open(filename, "r")
input = f.read().splitlines()
f.close()

# Parse input
assignments = []
for pair in input:
    section_range = []
    elf_assignment = pair.split(',')
    for sections in elf_assignment:
        (x, y) = sections.split('-')
        section_range.append((int(x), int(y)))
    assignments.append(section_range)

# Helper function
def range_encapsulates(xmin, xmax, ymin, ymax):
    return (xmin <= ymin and xmax >= ymax) or (ymin <= xmin and ymax >= xmax)

# Solve
counter_a = 0
for assignment in assignments:
    min_a = assignment[0][0]
    max_a = assignment[0][1]
    min_b = assignment[1][0]
    max_b = assignment[1][1]
    if range_encapsulates(min_a, max_a, min_b, max_b):
        counter_a += 1

# Solution Part A
print("Solution Part A:", counter_a)

# Part B
# All pairs that have any overlap at all

# Helper function
def range_overlaps(xmin, xmax, ymin, ymax):
    x, y = set(range(xmin, xmax+1)), set(range(ymin, ymax+1))
    return bool(x.intersection(y))

# Solve
counter_b = 0
for assignment in assignments:
    min_a = assignment[0][0]
    max_a = assignment[0][1]
    min_b = assignment[1][0]
    max_b = assignment[1][1]
    if range_overlaps(min_a, max_a, min_b, max_b):
        counter_b += 1

# Solution part B
print("Solution Part B:", counter_b)
