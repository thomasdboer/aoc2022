import os
import string
from time import perf_counter

t1_start = perf_counter()
filename = os.path.join(os.path.dirname(__file__), "input.txt")
f = open(filename, "r")
input = f.read().splitlines()
f.close()

# Value function
valueMap = {char: val for (val, char) in enumerate(
    string.ascii_letters, start=1)}


# Helper function using sets because why not
def matchcompartments(comp1, comp2):
    return ''.join(set(comp1).intersection(set(comp2)))

# Find every letter present in both compartments


def find_duplicates():
    duplicates = []
    for rucksack in input:
        slice = int(len(rucksack)/2)
        compartment1 = rucksack[:slice]
        compartment2 = rucksack[slice:]
        duplicates.append(matchcompartments(compartment1, compartment2))
    return duplicates


# Solve
def calculate_priority(characters):
    sum_priority = 0
    for char in characters:
        sum_priority += valueMap[char]
    return sum_priority


def solve_a():
    duplicates = find_duplicates()
    return calculate_priority(duplicates)


# Part A solution
print("Solution Part A:", solve_a())

# Part B


def find_badges():
    groups = [input[i:i+3] for i in range(0, len(input), 3)]
    badges = []
    for group in groups:
        badge = ""
        for char in group[0]:
            if char in group[1] and char in group[2]:
                badge = char
        badges.append(badge)
    return badges


def solve_b():
    badges = find_badges()
    return calculate_priority(badges)


print("Solution Part B:", solve_b())
t1_stop = perf_counter()
print("Solution found in:", (t1_stop-t1_start).__round__(5), "s")
