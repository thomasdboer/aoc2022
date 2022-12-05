from time import perf_counter

t1_start = perf_counter()
f = open("input.txt", "r")
input = f.read().split("\n\n")
f.close()

# Strip trailing newline
last_element = input.pop().rstrip()
input.append(last_element)

# Process strings into lists of ints


def get_calories_lists():
    elves = []
    for elf in input:
        if elf.__contains__("\n"):
            elves.append([int(x) for x in elf.split("\n")])
        else:
            elves.append([int(elf)])
    return elves

# Sum calories per elf


def sum_calories(elves):
    elves_cal = []
    for calories_list in elves:
        cal_total = 0
        for item in calories_list:
            cal_total += item
        elves_cal.append(cal_total)
    return elves_cal


def solve_a():
    cal_lists = get_calories_lists()
    totals = sum_calories(cal_lists)
    return max(totals)


print("Part A solution: ", solve_a())

# Part B


def solve_b():
    cal_lists = get_calories_lists()
    totals = sum_calories(cal_lists)
    totals.sort(reverse=True)
    return sum(totals[0:3])


print("Part B solution: ", solve_b())
t1_stop = perf_counter()
print("Solution found in:", (t1_stop-t1_start).__round__(5), "s")
