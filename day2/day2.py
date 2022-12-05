import os
filename = os.path.join(os.path.dirname(__file__), "input.txt")
f = open(filename, "r")
input = f.read().splitlines()
f.close()

value_map_a = {'A': {'X': '4', 'Y': '8', 'Z': '3'}, 'B': {
    'X': '1', 'Y': '5', 'Z': '9'}, 'C': {'X': '7', 'Y': '2', 'Z': '6'}}


def result(strategy, value_map):
    opp_choice = strategy[0]
    play_choice = strategy[2]
    return value_map[opp_choice][play_choice]


my_score_a = 0
for game in input:
    my_score_a += int(result(game, value_map_a))

# Part A solution
print(my_score_a)

# Part B
value_map_b = {'A': {'X': '3', 'Y': '4', 'Z': '8'}, 'B': {
    'X': '1', 'Y': '5', 'Z': '9'}, 'C': {'X': '2', 'Y': '6', 'Z': '7'}}

my_score_b = 0
for game in input:
    my_score_b += int(result(game, value_map_b))

# Part B solution
print(my_score_b)
