#!/usr/bin/env python3
import sys

offsets = ((0, 1), (0, -1), (-1, 0), (1, 0))

sys.stdin.readline()
print("I AM Son\n")
sys.stdin.readline()
print("OK\n")
sys.stdin.readline()
sys.stdin.readline()
sys.stdin.readline()


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


# check neighbors
def get_neighbors(all_node, pos_a):
    viable_neighbors = []
    for offset in offsets:
        neighbor = [pos_a[0] + offset[0], pos_a[1] + offset[1]]
        if neighbor in all_node:
            viable_neighbors.append(neighbor)
    return viable_neighbors

# solve the maze
def solve_maze(maze, pos_a):
    print(pos_a, file=sys.stderr)
    print(all_node, file=sys.stderr)
    print(maze) # print move


maze, pos_a, all_node = get_maze()
neighbors = get_neighbors(all_node, pos_a)
print(neighbors, file=sys.stderr)
solve_maze(maze, pos_a)
