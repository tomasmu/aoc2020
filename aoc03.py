#input
import os
file = os.path.basename(__file__).replace('.py', '.txt')
input = open(file).read().splitlines()

#format
array = input

#puzzle 1
answer1 = sum(array[n][n * 3 % len(array[n])] == "#" for n in range(len(array)))
print (answer1)

#puzzle 2
import functools
steps = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
def count_trees(x, y):
    return sum(array[a][b % len(array[a])] == "#" for a, b in zip(range(0, len(array), y), range(0, x * len(array), x)))

answer2 = functools.reduce(lambda product, step: product * count_trees(*step), steps, 1)
print (answer2)
