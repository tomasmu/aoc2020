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

puzzle = sorted(int(n) for n in puzzle)
puzzle = [0, *puzzle, max(puzzle) + 3]

# puzzle 1
differences = [b - a for a, b in zip(puzzle, puzzle[1:])]

answer1 = differences.count(1) * differences.count(3)
print(answer1)

# puzzle 2
def count_paths(array, dictionary = {}):
    if len(array) <= 1:
        return 1
    if array[0] in dictionary:
        return dictionary[array[0]]
    else:
        indices = [i for i in range(1, 4) if i < len(array) and array[i] - array[0] <= 3]
        dictionary[array[0]] = sum(count_paths(array[i:]) for i in indices)
        return dictionary[array[0]]

answer2 = count_paths(puzzle)
print(answer2)
