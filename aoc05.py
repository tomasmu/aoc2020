# input
import re
import os
file = os.path.basename(__file__).replace('.py', '.txt')
input = open(file).read().splitlines()

# format
array = input

# puzzle 1
def find_pos(low, high, chars):
    if len(chars) == 0:
        return low
    if re.match("F|L", chars[0]):
        return find_pos(low, low + int((high - low) / 2), chars[1:])
    if re.match("B|R", chars[0]):
        return find_pos(low + int((high - low) / 2 + 0.5), high, chars[1:])

def get_seat(chars):
    return 8 * find_pos(0, 127, chars[0:7]) + find_pos(0, 7, chars[7:])

answer1 = max(get_seat(chars) for chars in array)
print(answer1)

# puzzle 2
seats = sorted(get_seat(chars) for chars in array)
answer2 = next(i + 1 for i, j in zip(seats, seats[1:]) if j-i > 1)
print(answer2)
