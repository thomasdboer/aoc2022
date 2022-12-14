import os
from time import perf_counter
import uuid

t1_start = perf_counter()
filename = os.path.join(os.path.dirname(__file__), "input.txt")

class Node(object):
    def __init__(self, name, size, parent=None):
        self.id = uuid.uuid4()
        self.name = str(name)
        self.size = int(size)
        self.parent = parent
        self.children = []

    def add_leafsize(self, filesize_leaf: int):
        self.size += filesize_leaf
        if self.parent is not None:
            self.parent.add_leafsize(filesize_leaf)
            
            
def read_input():
    f = open(filename, "r")
    input = [line.replace("\n", " ").strip()
             for line in f.read().split("$")][1:]
    f.close()
    return input


def parse_tree(input):

    folders = []
    current_node = Node("", 0)
    for line in input:
        # Read instructions until node
        command = line.split(" ")

        match line:

            case _ as line if 'cd /' in line:
                current_node = Node('/', 0)
                folders.append(current_node)

            case _ as line if 'cd ..' in line and current_node.parent is not None:
                current_node = current_node.parent

            case _ as line if command[0] == 'cd' and command[1] != '..':
                id = next(
                    (id for (x, id) in current_node.children if x == command[1]))
                current_node = next(
                    x for x in folders if x.id == id
                )

            case _ as line if 'ls' in line:
                assert current_node is not None
                leaf_size = sum([int(y) for y in command if y.isdigit()])
                current_node.add_leafsize(leaf_size)

                # Add node for every dir, set parent
                dirs = [command[idx+1]
                        for idx, x in enumerate(command) if x == 'dir']
                for dir in dirs:
                    child_node = Node(dir, 0, current_node)
                    folders.append(child_node)
                    current_node.children.append(
                        (child_node.name, child_node.id))

    return folders


def get_input():
    input = read_input()
    return parse_tree(input)


def solve_a():
    folders = get_input()
    qualifying_folders = [x.size for x in folders if x.size <= 100000]
    return sum(qualifying_folders)


print("Part A solution:", solve_a())


def solve_b():
    filesystem_size = 70000000
    update_size = 30000000
    folders = get_input()
    root = next((x for x in folders if x.name == '/'))
    
    # Calculate required space
    free_space = filesystem_size - root.size
    required_space = update_size - free_space

    # Find smallest single folder that satisfies criteria
    qualifying_folders = [x.size for x in folders if x.size >= required_space]
    return min(qualifying_folders)
t1_stop = perf_counter()

print("Part B solution:", solve_b())
print("Solution reached in:", round(t1_stop-t1_start, 5), 's')
