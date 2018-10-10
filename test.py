#!/usr/bin/env python3
import sys
import heapq

offsets = ((0, 1), (0, -1), (-1, 0), (1, 0))

sys.stdin.readline() # skip hello
print("I AM Son\n")
sys.stdin.readline()
print("OK\n")
sys.stdin.readline()
sys.stdin.readline()
sys.stdin.readline()

class PriorityQueue:
    def __init__(self):
        self.elements = []

    def empty(self):
        return len(self.elements) == 0

    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        return heapq.heappop(self.elements)[1]


# get the maze from the VM
def get_maze():
    maze_list = []
    all_node = []
    line = sys.stdin.readline()
    current_y = 0
    a_x = 0
    a_y = 0
    while line != "\n":
        current_x = 0
        row_maze_list = []
        for char in line:
            if char != '\n':
                row_maze_list.append(char)
                if char == 'A':
                    a_x = current_x
                    a_y = current_y
                if char != 'A' and char != '#':
                    all_node.append([current_x, current_y])
            current_x += 1
        maze_list.append(row_maze_list)
        print(row_maze_list, file=sys.stderr)
        line = sys.stdin.readline()
        current_y += 1
    return maze_list, (a_x, a_y), all_node


# check neighbors for viable node around A
def get_neighbors(all_node, pos_a):
    viable_neighbors = []
    for offset in offsets:
        neighbor = [pos_a[0] + offset[0], pos_a[1] + offset[1]]
        if neighbor in all_node:
            viable_neighbors.append(neighbor)
    return viable_neighbors

def solve_maze(neighbors, pos_a):
    frontier = PriorityQueue()
    frontier.put(pos_a)
    came_from = {}
    came_from(pos_a) = None

    while not frontier.empty():
        current = frontier.get()
        for next in neighbors:
            if next not in came_from:
                frontier.put(next)
                came_from(next) = pos_a

    return came_from



maze, pos_a, all_node = get_maze()
neighbors = get_neighbors(all_node, pos_a)
print(pos_a, file=sys.stderr)
print(neighbors, file=sys.stderr)

