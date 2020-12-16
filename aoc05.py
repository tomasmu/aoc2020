import os
import re

# input
file = os.path.basename(__file__).replace('.py', '_input.txt')
input = open(file).read()

puzzle = input.splitlines()

# puzzle 1
def get_seat(chars):
    return int(re.sub('F|L', '0', re.sub('B|R', '1', chars)), 2)

answer1 = max(map(get_seat, puzzle))
print(answer1)

# puzzle 2
taken_seats = set(get_seat(chars) for chars in puzzle)
all_seats = set(range(min(taken_seats), max(taken_seats) + 1))

answer2 = all_seats.difference(taken_seats).pop()
print(answer2)
