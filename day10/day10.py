import os
from time import perf_counter

t1_start = perf_counter()
filename = os.path.join(os.path.dirname(__file__), "input.txt")


def parse_input():
    with open(filename) as f:
        input = []
        for line in f.readlines():
            line = line.strip()
            if line == 'noop':
                input.append((line, 0))
            else:
                x = line.split(' ')
                input.append((x[0], int(x[1])))
    # Reverse the order to use pop() later
    input.reverse()
    return input


# Literally only necessary to shut the linter up
class Cache(object):
    def __init__(self, inst, val):
        self.inst = inst
        self.val = val
        self.time = 2 if inst == 'addx' else 1

class CPU(object):
    reg = 1
    cycle = 0
    signal_strengths = []
    cached_inst = None
    line = ''
    screen = []
    def __init__(self, instructions):
        self.instructions = instructions

    def tick(self):
        self.cycle += 1
        # Get a new instruction if we don't have one yet
        if not self.cached_inst:
            (inst, val) = self.instructions.pop()
            self.cached_inst = Cache(inst, val)
        # During cycle
        if self.cycle in range(20, 221, 40):
            self.signal_strengths.append(self.cycle * self.reg)
        pixel = (self.cycle - 1) % 40
        if pixel == 0: line = ''
        if self.reg - 1 <= pixel <= self.reg + 1:
            self.line += '#'
        else:
            self.line += '.'
        if pixel == 39: 
            self.screen.append(self.line)
            self.line = ''
        if self.cached_inst.time == 1:
            self.reg += self.cached_inst.val
            del self.cached_inst
        else:
            self.cached_inst.time -= 1

def solve_a():
    input = parse_input()
    cpu = CPU(input)
    while cpu.instructions or cpu.cached_inst:
        cpu.tick()
    return sum(cpu.signal_strengths)


print('Part A solution:', solve_a())


def solve_b():
    input = parse_input()
    cpu2 = CPU(input)
    while cpu2.instructions or cpu2.cached_inst:
        cpu2.tick()
    for line in cpu2.screen[:6]: print(line)
        
print("Part B solution:")
solve_b()