#input
import os
import math

file = os.path.basename(__file__).replace('.py', '_input.txt')
input = open(file).read().splitlines()

#format
array = input

#puzzle 1
answer1 = sum(array[n][n * 3 % len(array[n])] == "#" for n in range(len(array)))
print (answer1)

#puzzle 2
steps = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
def count_trees(step):
    col_step, row_step = step
    rows = range(0, len(array), row_step)
    cols = range(0, int(col_step/row_step * len(array) + 0.5), col_step)
    return sum(array[row][col % len(array[row])] == "#" for row, col in zip(rows, cols))

answer2 = math.prod(map(count_trees, steps))
print (answer2)
