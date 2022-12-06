import os
from time import perf_counter

t1_start = perf_counter()
filename = os.path.join(os.path.dirname(__file__), "input.txt")
f = open(filename, "r")

markers = []


def markindex(idx):
    markers.append(idx)


def is_marker(buffer):
    marker_packet = True
    for idx, char in enumerate(buffer):
        if buffer[idx+1:].__contains__(char) or len(buffer) < 4:
            marker_packet = False
    return marker_packet


def read_input_stream():
    input = f.read().rstrip('\n')
    f.close()
    buffer = []
    for idx, i in enumerate(input):
        # Use insert() and pop() for O(1) time
        buffer.insert(0, i)
        if is_marker(buffer):
            # Mark index
            markindex(idx+1)

        if (len(buffer) > 3):
            buffer.pop()


def solve_a():
    read_input_stream()
    return markers[0]


print("Part A solution: ", solve_a())
t1_stop = perf_counter()
print("Solution reached in: ", t1_stop-t1_start)
