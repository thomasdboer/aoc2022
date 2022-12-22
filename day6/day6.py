import os
from multiprocessing import Pool
from time import perf_counter
t1_start = perf_counter()
filename = os.path.join(os.path.dirname(__file__), "extra.txt")

def read_input():
    f = open(filename, "r")
    input = f.read().rstrip('\n')
    f.close()
    return input


def solve_a():
    input = read_input()
    buffer = []
    # O(i)
    for idx, i in enumerate(input):
        # insert() and pop() are O(1)
        buffer.insert(0, i)
        if len(buffer) > 94:
            buffer.pop()
            if len(set(buffer)) == 94:
                return idx+1


# print("Part A solution: ", solve_a())

def find_packet(j):    
    input = read_input()
    buffer = []
    for idx, i in enumerate(input):
        buffer.insert(0, i)
        if len(buffer) > j:
            buffer.pop()
            if len(set(buffer)) == j:
                return idx+1 if idx > 1 else 1

def solve_b():
    total = 0
    with Pool() as pool:
        for result in pool.map(find_packet, range(1,95)):
            total += result  # type: ignore
    return total


if __name__=="__main__":
    print("Part B solution: ", solve_b())
    t1_stop = perf_counter()
    print("Solution reached in:", round(t1_stop-t1_start, 5), 's')
