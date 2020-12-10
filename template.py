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

# puzzle 1

answer1 = puzzle
print(answer1)

# puzzle 2

answer2 = ''
print(answer2)
