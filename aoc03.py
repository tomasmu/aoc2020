#input
import os
file = os.path.basename(__file__).replace('.py', '.txt')
input = open(file).read().splitlines()

#format
array = input

#puzzle 1
import functools
answer1 = functools.reduce(
    lambda acc, cur: acc + int(array[cur][cur * 3 % len(array[cur])] == "#"),
    range(len(array)),
    0)
print (answer1)

#puzzle 2
import operator
steps = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
def countTrees(row, col):
    return functools.reduce(
        lambda acc, cur: acc + int(array[cur[0]][cur[1] % len(array[cur[0]])] == "#"),
        zip(range(0, len(array), col), range(0, row * len(array), row)),
        0)

answer2 = functools.reduce(operator.mul, map(lambda x: countTrees(*x), steps))
print (answer2)
