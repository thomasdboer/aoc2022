import os
filename = os.path.join(os.path.dirname(__file__), "input.txt")
f = open(filename, "r")
input = f.read().splitlines()
f.close()

value_map = {'A': {'X': '4', 'Y': '8', 'Z': '3'}, 'B': {'X': '1', 'Y': '5', 'Z': '9'}, 'C': {'X': '7', 'Y': '2', 'Z': '6'}}
def result(strategy):
    opp_choice = strategy[0]
    play_choice = strategy[2]
    return value_map[opp_choice][play_choice]

my_score = 0
for game in input:
    my_score += int(result(game))
print(my_score)
