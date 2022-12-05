import os
import string
filename = os.path.join(os.path.dirname(__file__), "input.txt")
f = open(filename, "r")
input = f.read().splitlines()
f.close()

# Helper function
def matchcompartments(comp1, comp2):
    for char in comp1:
        if char in comp2:
            return char

# Parse input
duplicates = []
for rucksack in input:
    slice = int(len(rucksack)/2)
    compartment1 = rucksack[:slice]
    compartment2 = rucksack[slice:]
    duplicates.append(matchcompartments(compartment1, compartment2))

valueMap = {char: val for (val, char) in enumerate(
    string.ascii_letters, start=1)}

# Solve
def calculate_priority(characters):
    sum_priority = 0
    for char in characters:
        sum_priority += valueMap[char]
    return sum_priority


# Part A solution
print("Solution Part A:", calculate_priority(duplicates))

# Part B
groups = [input[i:i+3] for i in range(0, len(input), 3)]
badges = []
for group in groups:
    badge = ""
    for char in group[0]:
        if char in group[1] and char in group[2]:
            badge = char
    badges.append(badge)

print("Solution Part B:", calculate_priority(badges))
