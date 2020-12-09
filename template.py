# imports
import collections
import functools
import itertools
import math
import os
import re

# input
file = os.path.basename(__file__).replace('.py', '_input.txt')
raw_input = open(file).read()

def format_input(array):
    if re.search('\n\n', array):
        return array.split('\n\n')
    else:
        return array.splitlines()

puzzle = format_input(raw_input)

# puzzle 1

answer1 = puzzle
print(answer1)

# puzzle 2

answer2 = ''
print(answer2)
