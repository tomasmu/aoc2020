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
    *init, prev = numbers
    seen_times = dict((n, i) for i, n in enumerate(init))
    for t in range(len(init), n - 1):
        if prev not in seen_times:
            next_ = 0
        else:
            next_ = t - seen_times[prev]
        seen_times[prev] = t
        prev = next_
    return next_

answer1 = get_nth_number(numbers, 2020)
print(answer1)

# puzzle 2
answer2 = get_nth_number(numbers, 30_000_000)
print(answer2)
