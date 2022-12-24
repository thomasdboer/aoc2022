import os
from time import perf_counter
import math

t1_start = perf_counter()
filename = os.path.join(os.path.dirname(__file__), "input.txt")


class Grid(object):
    cells = []

    def __init__(self, grid: list[list[int]]) -> None:
        self.cells = grid

    # Not related to Tree as a data structure
    # Cell values refer to trees
    def get_tree(self, x, y):
        return self.cells[y][x]

    def dist_y(self, x, y, reverse):
        height = self.get_tree(x, y)
        column = [row[x] for row in self.cells[:y]] if reverse else [row[x] for row in self.cells[y+1:]]
        if reverse: column.reverse()
        y_dist = next((idx for idx, tree in enumerate(column, 1) if tree >= height), len(column))
        return y_dist

    def dist_x(self, x, y, reverse):
        height = self.get_tree(x, y)
        row = self.cells[y][:x] if reverse else self.cells[y][x+1:]
        if reverse: row.reverse()
        x_dist = next((idx for idx, tree in enumerate(row, 1) if tree >= height), len(row))
        return x_dist

    
    def get_scenic_score(self, x, y):
        return [self.dist_x(x, y, True), self.dist_x(x, y, False),
         self.dist_y(x, y, True), self.dist_y(x, y, False)]
        


def parse_input():
    grid = []
    with open(filename) as file:
        grid = [[int(y) for y in list(x.rstrip())] for x in file.readlines()]
    return grid

# Only used for part A. Does not use Grid object.


def find_visible_trees(input_grid):
    visibility = []

    for (row_idx, row) in enumerate(input_grid):
        visibility.append([False] * len(row))

        for (col_idx, column) in enumerate(row):
            # Search laterally, first left then right
            visible_x = [x for x in row[:col_idx] if x >= column] == [] or [
                x for x in row[col_idx+1:] if x >= column] == []

            # Search vertically, first down then up
            visible_y = [x for x in input_grid[row_idx+1:] if x[col_idx] >= column] == [] or [
                x for x in input_grid[:row_idx] if x[col_idx] >= column] == []

            visibility[row_idx][col_idx] = visible_x or visible_y
    return visibility


def solve_a():
    grid = parse_input()
    visibility = find_visible_trees(grid)
    visible_row = [row.count(True) for row in visibility]
    return ''.join("Part A solution: ", sum(visible_row))


print(solve_a())


def solve_b():
    grid = Grid(parse_input())
    scoremap = []
    for (y, row) in enumerate(grid.cells):
        row_scenicscores = []
        for (x, tree) in enumerate(row):
            if 0 < x < len(row) - 1 and 0 < y < len(grid.cells) - 1:
                scores = grid.get_scenic_score(x, y)
                treescore = 1
                for score in scores:
                    treescore *= score
            else: treescore = 0
            row_scenicscores.append(treescore)
        scoremap.append(row_scenicscores)
    return ''.join("Part B solution: max([max(b) for b in [x for x in scoremap]]")


t1_stop = perf_counter()
print("Solution reached in: ", round((t1_stop - t1_start), 5), "s")
