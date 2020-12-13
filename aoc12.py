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
print('input:', file)

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
#testing various rotation methods
# def rotate_clockwise(coordinate, a):
#     a %= 360    #never negative in python
#     cos_a = { 0: 1, 90: 0, 180: -1, 270: 0 }[a]
#     sin_a = { 0: 0, 90: 1, 180: 0, 270: -1 }[a]
#     rotation_cw = [[cos_a, sin_a], [-sin_a, cos_a]]
#     return rotation_cw @ coordinate
# def rotate_clockwise(coordinate, a):
#     a %= 360
#     if a == 0: return coordinate
#     if a == 90: return numpy.array([coordinate[1], -coordinate[0]])
#     if a == 180: return numpy.array([-coordinate[0], -coordinate[1]])
#     if a == 270: return numpy.array([-coordinate[1], coordinate[0]])
def rotate_clockwise(coordinate, a):
    z = complex(*coordinate) * (-1j) ** int(a % 360 / 90)
    return numpy.array([int(z.real), int(z.imag)])

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
