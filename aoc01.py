#input
import os
file = os.path.basename(__file__).replace('.py', '.txt')
input = open(file).read().splitlines()

#format
array = [int(n) for n in input]

#puzzle 1
answer1 = next(i*j for i in array for j in array if i+j == 2020)
print (answer1)

#puzzle 2
answer2 = next(i*j*k for i in array for j in array for k in array if i+j+k == 2020)
print (answer2)
