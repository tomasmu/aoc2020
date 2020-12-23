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
# file = os.path.basename(__file__).replace('.py', '_input.txt')
raw_input = open(file).read()
print('input:', file)

if re.search('\n\n', raw_input):
    puzzle = raw_input.split('\n\n')
else:
    puzzle = raw_input.splitlines()

#if cube is active and 2 <= neighbors_active <= 3 -> remain active, else inactive
#if cube is inactive neighbors_active=3 -> become active, else inactive

# puzzle 1
ACTIVE = '#'
#INACTIVE = '.'
DIMENSIONS = 3
NUMBER_OF_CYCLES = 6
STEPS = [step for step in itertools.product([0, 1, -1], repeat=DIMENSIONS) if any(s != 0 for s in step)]
pocket_dimension = { (xi, yi, 0) for yi, y in enumerate(puzzle) for xi, x in enumerate(y) if x == ACTIVE }

#todo: can i generalize this and use it for day 11?

def print_dimension(dimension):
    zs = {d[2] for d in dimension}
    print("todo: print x,y for zs", zs)

print_dimension(pocket_dimension)

def count_neighbors(coordinate, pocket_dimension):
    s = {tuple(map(sum, zip(coordinate, step))) for step in STEPS} & pocket_dimension
    return len(s)

def get_axes_thing(pocket_dimension, func):
    return func((d[i] for d in pocket_dimension for i in range(DIMENSIONS)))

def get_new_set(pocket_dimension):
    new_active = [c for c in pocket_dimension if 2 <= count_neighbors(c, pocket_dimension) <= 3]
    min_coordinates = get_axes_thing(pocket_dimension, min)
    max_coordinates = get_axes_thing(pocket_dimension, max)
    inactive = todo
    pass

#cycle
def apply_cycle(pocket_dimension, number_of_cycles):
    for i in range(number_of_cycles):
        pass

get_new_set(pocket_dimension)

answer1 = len(pocket_dimension)
print(answer1)

# puzzle 2

answer2 = ''
print(answer2)
