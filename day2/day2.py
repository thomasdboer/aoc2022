import os
from time import perf_counter

t1_start = perf_counter()
filename = os.path.join(os.path.dirname(__file__), "input.txt")
f = open(filename, "r")
input = f.read().splitlines()
f.close()

value_map_a = {'A': {'X': 4, 'Y': 8, 'Z': 3}, 'B': {
    'X': 1, 'Y': 5, 'Z': 9}, 'C': {'X': 7, 'Y': 2, 'Z': 6}}
value_map_b = {'A': {'X': 3, 'Y': 4, 'Z': 8}, 'B': {
    'X': 1, 'Y': 5, 'Z': 9}, 'C': {'X': 2, 'Y': 6, 'Z': 7}}

# Calculate player score based on objects chosen by players
def game_result(strategies, value_map):
    opp_choice = strategies[0]
    player_choice = strategies[2]
    return value_map[opp_choice][player_choice]

def solve_a():
    my_score = 0
    for game in input:
        my_score += game_result(game, value_map_a)
    return my_score

# Part A solution
print("Part A solution:", solve_a())

# Part B
def solve_b():
    my_score = 0
    for game in input:
        my_score += game_result(game, value_map_b)
    return my_score

# Part B solution
print("Part B solution:", solve_b())
t1_stop = perf_counter()
print("Solution found in:", (t1_stop-t1_start).__round__(5), "s")