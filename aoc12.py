# imports
import collections
import functools
import itertools
import math
import os
import re

# input
file = os.path.basename(__file__).replace('.py', '_example.txt')
file = os.path.basename(__file__).replace('.py', '_input.txt')
raw_input = open(file).read()
print("input:", file)

if re.search('\n\n', raw_input):
    puzzle = raw_input.split('\n\n')
else:
    puzzle = raw_input.splitlines()

puzzle = [(x[0], int(x[1:])) for x in puzzle]

# puzzle 1
move_table = { 'N': (0, 1), 'S': (0, -1), 'E': (1, 0), 'W': (-1, 0) }
rotate_table = { 'L': -1, 'R': 1 }
def move_boaty_boat(puzzle):
    angle_table = { 0: move_table['E'], 90: move_table['S'], 180: move_table['W'], 270: move_table['N'] }
    #todo: look up vectors in python
    x, y, angle = 0, 0, 0
    for action, value in puzzle:
        if action in move_table:
            dx, dy = move_table[action]
            x += dx * value
            y += dy * value
        if action in rotate_table:
            angle = (angle + rotate_table[action] * value) % 360
        if action == 'F':
            dx, dy = angle_table[angle]
            x += dx * value
            y += dy * value
    return abs(x) + abs(y)

answer1 = move_boaty_boat(puzzle)
print(answer1)

#slightly simplified math library
def rotate_clockwise(x, y, a):
    a = (a + 360) % 360
    cos_a = { 0: 1, 90: 0, 180: -1, 270: 0 }[a]
    sin_a = { 0: 0, 90: 1, 180: 0, 270: -1 }[a]
    return (x*cos_a + y*sin_a, y*cos_a - x*sin_a)

# puzzle 2
def move_boaty_waypoint(puzzle):
    x, y = 0, 0
    wx, wy = 10, 1
    for action, value in puzzle:
        if action in move_table:
            dx, dy = [d * value for d in move_table[action]]
            wx += dx
            wy += dy
        elif action in rotate_table:
            angle = rotate_table[action] * value
            wx, wy = rotate_clockwise(wx, wy, angle)
        elif action == 'F':
            x += wx * value
            y += wy * value
    return abs(x) + abs(y)

answer2 = move_boaty_waypoint(puzzle)
print(answer2)
