#!/usr/bin/env python3
import sys

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
    # maze = sys.stdin.readline()
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
            current_x += 1
        maze_list.append(row_maze_list)
        print(row_maze_list, file=sys.stderr)
        line = sys.stdin.readline()
        current_y += 1
    return maze_list, (a_x, a_y)


# solve the maze
def solve_maze(maze, pos_a):
    print(pos_a, file=sys.stderr)
    print(maze) # print move


maze, pos_a = get_maze()
solve_maze(maze, pos_a)
