# imports
import collections
import functools
import itertools
import os
import re

# input
file = os.path.basename(__file__).replace('.py', '_input.txt')
raw_input = open(file).read()

if re.search('\n\n', raw_input):
    puzzle = raw_input.split('\n\n')
else:
    puzzle = raw_input.splitlines()

puzzle = [int(n) for n in puzzle]

# puzzle 1
def find_nonsummable_number(array, preamble_len):
    for i in range(preamble_len, len(array)):
        preamble = array[i - preamble_len:i]
        pairs = itertools.combinations(preamble, 2)
        next_number = array[i]
        if all(a + b != next_number for a, b in pairs):
            return next_number
    return None

answer1 = find_nonsummable_number(puzzle, 25)
print(answer1)

# puzzle 2
def contiguous_set(array, answer):
    for length in range(2, len(array) + 1):
        arr_sum = sum(array[0:length])
        for i in range(len(array) - length):
            if arr_sum == answer:
                arr = array[i:i+length]
                return min(arr) + max(arr)
            arr_sum -= array[i]
            arr_sum += array[i+length]
    return None

answer2 = contiguous_set(puzzle, answer1)
print(answer2)
