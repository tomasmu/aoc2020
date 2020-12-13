# input
import functools
import os
file = os.path.basename(__file__).replace('.py', '_input.txt')
input = open(file).read()

# format
array = input.split('\n\n')
puzzle = [line.split() for line in array]

# puzzle 1
answer1 = sum(len(set().union(*group)) for group in puzzle)
print(answer1)

# puzzle 2
answer2 = sum(len(set(first).intersection(*rest)) for first, *rest in puzzle)
print(answer2)
