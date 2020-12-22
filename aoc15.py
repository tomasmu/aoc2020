# imports
import collections
import os
import numpy
import functools
import itertools
import re
import math

# input
file = os.path.basename(__file__).replace('.py', '_example.txt')
file = os.path.basename(__file__).replace('.py', '_input.txt')
raw_input = open(file).read()
print('input:', file)

if re.search('\n\n', raw_input):
    puzzle = raw_input.split('\n\n')
else:
    puzzle = raw_input.splitlines()

# puzzle 1
numbers = [int(n) for n in puzzle[0].split(',')]

def get_nth_number(numbers, n):
    history = {n: i + 1 for i, n in enumerate(numbers)}
    prev = numbers[-1]
    for t in range(len(numbers), n):
        current = t - history.get(prev, t)
        history[prev] = t
        prev = current
    return current

answer1 = get_nth_number(numbers, 2020)
print(answer1)

# puzzle 2
answer2 = get_nth_number(numbers, 30_000_000)
print(answer2)
