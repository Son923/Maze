#!/usr/bin/env python3
import sys
import heapq


# class represents graph
class Grid():
    def __init__(self, width, height):
        self.gems = []      # list of '!'
        self.coins = []     # list of 'o'
        self.width = width
        self.height = height
        self.walls = []     # list of '#'
        self.players = []

    def in_bounds(self, id):
        (x, y) = id
        return 0 <= x < self.width and 0 <= y < self.height

    # get passable positions
    def passable(self, id):
        return id not in self.walls

    # get viable move around id
    def neighbors(self, id):
        (x, y) = id
        results = [(x + 1, y), (x, y - 1), (x - 1, y), (x, y + 1)]
        results = filter(self.in_bounds, results)
        results = filter(self.passable, results)
        return results

    def cost(self, from_node, tonode):
        return 1 if tonode in self.gems else 5 if tonode in self.coins \
            else 45 if tonode in self.players else 50


# Class
class PriorityQueue:
    def __init__(self):
        self.elements = []

    def empty(self):
        return len(self.elements) == 0

    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        return heapq.heappop(self.elements)[1]


def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def a_star_search(graph, start, goal):
    frontier = PriorityQueue()
    frontier.put(start, 0)
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0

    while not frontier.empty():
        current = frontier.get()

        if current == goal:
            break

        for next in graph.neighbors(current):
            new_cost = cost_so_far[current] + graph.cost(current, next)
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost + heuristic(goal, next)
                frontier.put(next, priority)
                came_from[next] = current
    return came_from, cost_so_far


def reconstruct_path(came_from, start, goal):
    current = goal
    path = []
    while current != start:
        path.append(current)
        current = came_from[current]
    path.reverse()  # optional
    return path


def reconstruct(graph, start, goal):
    came_from, cost_so_far = a_star_search(graph, start, goal)
    return reconstruct_path(came_from, start, goal)


# get the maze as a graph, rewards and gems from the VM
def parse_maze():
    # parse the maze
    maze = []
    coins = []
    gems = []
    walls = []
    players = []
    line = sys.stdin.readline()
    current_y = 0
    # main_player
    a_x = 0
    a_y = 0

    while line != "\n":     # check if last line of maze
        current_x = 0
        row_maze_list = []
        for char in line:
            if char != '\n':
                row_maze_list.append(char)
                if char == main_player:     # position of main player
                    a_x = current_x
                    a_y = current_y
                elif char == 'o':   # position of 'o'
                    coins.append((current_x, current_y))
                elif char == '!':   # position of '!'
                    gems.append((current_x, current_y))
                elif char == '#':   # position of '#' and 'players'
                    walls.append((current_x, current_y))
                elif char.isupper():    # position of other players
                    players.append((current_x, current_y))
            current_x += 1
        maze.append(row_maze_list)
        line = sys.stdin.readline()     # read next line of the maze
        current_y += 1

    # create a graph from maze, move to
    maze_graph = Grid(len(maze[0]), len(maze))
    maze_graph.walls = walls
    maze_graph.gems = gems
    maze_graph.coins = coins
    maze_graph.players = players

    move_to_nearest(maze_graph, (a_x, a_y), gems + coins)


# Move mechanic
def move(start, end):
    start_x, start_y = start
    end_x, end_y = end

    if start_x > end_x:
        return "LEFT"
    elif start_x < end_x:
        return "RIGHT"
    elif start_y > end_y:
        return "UP"
    else:
        return "DOWN"


def move_to_nearest(graph, start, goals):
    paths = []
    for goal in goals:  # create a list of viable paths
        paths.append(reconstruct(graph, start, goal))
    path = min(paths, key=lambda current_path: len(current_path))
    print("MOVE " + move(start, path[0]) + '\n')


# Init protocol
sys.stdin.readline()    # HELLO
print("I AM Son\n")
sys.stdin.readline()    # \n
string = sys.stdin.readline()    # YOU ARE <LETTER>
main_player = string.split(' ')[2].strip('\n')
print("OK\n")
sys.stdin.readline()    # \n
sys.stdin.readline()    # MAZE

s = 0    # first condition of s
while s is not None:    # Check if EOF
    parse_maze()
    s = sys.stdin.readline()  # read next line after maze
