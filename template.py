# imports
import collections
import functools
import os
import re

# input
file = os.path.basename(__file__).replace('.py', '_input.txt')
input = open(file).read()

# format
if re.search('\n\n', input):
    array = input.split('\n\n')
    #array = [arr.splitlines() for arr in input.split('\n\n')]
else:
    array = input.splitlines()

# puzzle 1

answer1 = array
print(answer1)

# puzzle 2

answer2 = ''
print(answer2)
