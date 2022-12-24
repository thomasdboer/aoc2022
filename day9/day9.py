import os
from time import perf_counter

t1_start = perf_counter()
filename = os.path.join(os.path.dirname(__file__), "input.txt")

class Node(object):
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        self.visited = set([(x, y)])

def parse_instructions():
    instructions = []
    with open(filename) as f:
        instructions = [(x.split(' ')[0], int(x.split(' ')[1].rstrip())) for x in f.readlines()]
    instructions.reverse()
    return instructions

def step_head(dir, head):
    match dir:
        case 'R':
            head.x += 1
        case 'L':
            head.x -= 1
        case 'U':
            head.y += 1
        case 'D':
            head.y -= 1
    head.visited.add((head.x, head.y))

def step_tail(head, tail):
    dist_x = abs(head.x - tail.x)
    dist_y = abs(head.y - tail.y) 
    if dist_x == 1 and dist_y == 1:
        # Head and tail are diagonally adjacent, no need to move
        return
    elif dist_x == 0 and dist_y == 1 or dist_x == 1 and dist_y == 0:
        # Head and tail are directly adjacent, no need to move
        return
    elif head.x == tail.x and head.y == tail.y:
        # Head and tail are overlapping, no need to move
        return
    elif dist_x > 1 and dist_y == 0:
        # Head and tail are within one step of each other, move horizontally or vertically
        tail.x += 1 if head.x > tail.x else -1
        tail.y += 1 if head.y > tail.y else -1
    else:
        # Head and tail are more than one step apart, move diagonally
        tail.x += 1 if head.x > tail.x else -1
        tail.y += 1 if head.y > tail.y else -1
    tail.visited.add((tail.x, tail.y))


def solve_a():
    head = Node(0, 0)
    tail = Node(0, 0)
    instructions = parse_instructions()
    while len(instructions) > 0:
        (dir, num) = instructions.pop()
        print(dir, num)
        (print(head.x, head.y))
        for i in range(num):
            step_head(dir, head)
            step_tail(head, tail)
        print(tail.visited)
    return len(tail.visited)

print(solve_a())

def solve_b():
    nodes = [Node(0,0) for i in range(10)]
    instructions = parse_instructions()
    while len(instructions) > 0:
        (dir, num) = instructions.pop()
        for i in range(num):
            step_head(dir, nodes[0])
            for (idx, node) in enumerate(nodes[1:], 1):
                step_tail(nodes[idx-1], node)
    return len(nodes[-1].visited)

print(solve_b())