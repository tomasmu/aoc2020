# imports
import collections
import functools
import itertools
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

puzzle = [int(n) for n in puzzle]

# puzzle 1
def find_nonsummable_number(array, preamble_len):
    for i in range(preamble_len, len(array)):
        preamble = array[i - preamble_len:i]
        #pairs = [(a, b) for i, a in enumerate(preamble) for j, b in enumerate(preamble[i+1:])]
        pairs = itertools.combinations(preamble, 2)
        next_number = array[i]
        if not any(a + b == next_number for a, b in pairs):
            return next_number
    return None

answer1 = find_nonsummable_number(puzzle, 25)
print(answer1)

# puzzle 2
def contiguous_set(array, answer):
    for i in range(len(array)):
        for j in range(i+2, len(array)):
            arr = array[i:j]
            arr_sum = sum(arr)
            if arr_sum > answer:
                break
            if arr_sum == answer:
                return min(arr) + max(arr)
    return ['err', 'or']

answer2 = contiguous_set(puzzle, answer1)
print(answer2)
