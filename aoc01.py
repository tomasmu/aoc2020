#input
import os
import itertools
import math

file = os.path.basename(__file__).replace('.py', '_input.txt')
input = open(file).read().splitlines()

#format
array = [int(n) for n in input]

#puzzle 1
answer1 = next(math.prod(c) for c in itertools.combinations(array, 2) if sum(c) == 2020)
print (answer1)

#puzzle 2
answer2 = next(math.prod(c) for c in itertools.combinations(array, 3) if sum(c) == 2020)
print (answer2)
