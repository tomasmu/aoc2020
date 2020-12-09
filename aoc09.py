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
    for i in range(len(array) - preamble_len):
        preamble = array[i:i+preamble_len]
        next_number = array[i+preamble_len]
        #pairs = [(a, b) for i, a in enumerate(preamble) for j, b in enumerate(preamble[i+1:])]
        pairs = itertools.combinations(preamble, 2)
        is_not_summable = all(a + b != next_number for a, b in pairs)
        if is_not_summable:
            return next_number
    return None

answer1 = find_nonsummable_number(puzzle, 25)
print(answer1)

# puzzle 2
def find_contiguous_set(array, answer):
    for i in range(len(array)):
        for length in range(2, len(array) - i):
            arr = array[i:i+length]
            arr_sum = sum(arr)
            if arr_sum > answer:
                break
            if arr_sum == answer:
                return arr
    return ['err', 'or']

contiguous_set = find_contiguous_set(puzzle, answer1)

answer2 = min(contiguous_set) + max(contiguous_set)
print(answer2)
