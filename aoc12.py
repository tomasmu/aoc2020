# imports
import collections
import functools
import itertools
import math
import numpy
import os
import re

# input
file = os.path.basename(__file__).replace('.py', '_example.txt')
file = os.path.basename(__file__).replace('.py', '_input.txt')
raw_input = open(file).read()
print("input:", file)

#format
if re.search('\n\n', raw_input):
    puzzle = raw_input.split('\n\n')
else:
    puzzle = raw_input.splitlines()

puzzle = [(x[0], int(x[1:])) for x in puzzle]

# puzzle 1
move_table = {
    'N': numpy.array([0, 1]),
    'S': numpy.array([0, -1]),
    'E': numpy.array([1, 0]),
    'W': numpy.array([-1, 0])
}
rotate_table = {
    'L': -1,
    'R': 1
}
def move_boaty_boat(puzzle):
    angle_table = {
        0: move_table['E'],
        90: move_table['S'],
        180: move_table['W'],
        270: move_table['N']
    }
    coordinate = numpy.array([0, 0])
    angle = 0
    for action, value in puzzle:
        if action in move_table:
            coordinate += value * move_table[action]
        if action in rotate_table:
            angle = (angle + rotate_table[action] * value) % 360
        if action == 'F':
            coordinate += value * angle_table[angle]
    return sum(abs(n) for n in coordinate)

answer1 = move_boaty_boat(puzzle)
print(answer1)

# puzzle 2
#slightly simplified math library
def rotate_clockwise(coordinate, a):
    a = (a + 360) % 360
    cos_a = { 0: 1, 90: 0, 180: -1, 270: 0 }[a]
    sin_a = { 0: 0, 90: 1, 180: 0, 270: -1 }[a]
    rotation_cw = [[cos_a, sin_a], [-sin_a, cos_a]]
    return rotation_cw @ coordinate

def move_boaty_waypoint(puzzle):
    coordinate = numpy.array([0, 0])
    waypoint = numpy.array([10, 1])
    for action, value in puzzle:
        if action in move_table:
            waypoint += value * move_table[action]
        elif action in rotate_table:
            waypoint = rotate_clockwise(waypoint, value * rotate_table[action])
        elif action == 'F':
            coordinate += value * waypoint
    return sum(abs(n) for n in coordinate)

answer2 = move_boaty_waypoint(puzzle)
print(answer2)
