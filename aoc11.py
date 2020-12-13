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
print('input:', file)

if re.search('\n\n', raw_input):
    puzzle = raw_input.split('\n\n')
else:
    puzzle = raw_input.splitlines()

puzzle = [list(row) for row in puzzle]

# puzzle 1
def print_puzzle(puzzle, text='printing'):
    print(f'{text}\n', '\n'.join([''.join(row) for row in puzzle]), sep = '')

STEPS = [(dr, dc) for dr, dc in itertools.product([0, 1, -1], repeat = 2) if dr != 0 or dc != 0]
def count_adjacent(matrix, row, col, char):
    count = 0
    for dr, dc in STEPS:
        r = row + dr
        c = col + dc
        if r >= 0 and c >= 0 and r < len(matrix) and c < len(matrix[r]) and matrix[r][c] == char:
            count += 1
    return count

EMPTY = 'L'
OCCUPIED = '#'
def get_new_matrix(matrix, count_method, occupied_limit):
    new_matrix = [list(row) for row in matrix]
    for r in range(len(puzzle)):
        for c in range(len(puzzle[r])):
            if matrix[r][c] == EMPTY and count_method(matrix, r, c, OCCUPIED) == 0:
                new_matrix[r][c] = OCCUPIED
            elif matrix[r][c] == OCCUPIED and count_method(matrix, r, c, OCCUPIED) >= occupied_limit:
                new_matrix[r][c] = EMPTY
    return new_matrix

def matrix_equals(left, right):
    return ''.join([''.join(row) for row in left]) == ''.join([''.join(row) for row in right])

def seating_process(matrix, count_method, occupied_limit):
    new_matrix = get_new_matrix(matrix, count_method, occupied_limit)
    while not matrix_equals(matrix, new_matrix):
        matrix = new_matrix
        new_matrix = get_new_matrix(matrix, count_method, occupied_limit)
    return sum(col == OCCUPIED for row in new_matrix for col in row)

answer1 = seating_process(puzzle, count_adjacent, 4)
print(answer1)

# puzzle 2
def count_sighted(matrix, row, col, char):
    count = 0
    for dr, dc in STEPS:
        r = row + dr
        c = col + dc
        while r >= 0 and c >= 0 and r < len(puzzle) and c < len(puzzle[r]):
            if matrix[r][c] == char:
                count += 1
                break
            if matrix[r][c] == EMPTY:   #empty seats apparently blocks the view and doesn't count
                break
            r += dr
            c += dc
    return count

answer2 = seating_process(puzzle, count_sighted, 5)
print(answer2)
