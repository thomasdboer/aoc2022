f = open("input.txt", "r")
input = f.read().split("\n\n")
f.close()

# Strip trailing newline
last_element = input.pop().rstrip()
input.append(last_element)

# Process strings into lists of ints
elves = []
for elf in input:
    if elf.__contains__("\n"):
        elves.append([int(x) for x in elf.split("\n")])
    else:
        elves.append([int(elf)])

# Sum calories per elf
elves_cal = []
for calories_list in elves:
    cal_total = 0
    for item in calories_list:
        cal_total += item
    elves_cal.append(cal_total)

print("Part A solution: ", max(elves_cal))

# Part B
top_elves = elves_cal
top_elves.sort(reverse=True)
print("Part B solution: ", sum(top_elves[0:3]))