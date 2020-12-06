# input
import os
file = os.path.basename(__file__).replace('.py', '.txt')
input = open(file).read().splitlines()

# format
array = input

# puzzle 1
def get_seat(chars):
    return int(chars.replace("F", "0").replace("L", "0").replace("B", "1").replace("R", "1"), 2)

answer1 = max(get_seat(chars) for chars in array)
print(answer1)

# puzzle 2
seats = set(get_seat(chars) for chars in array)
answer2 = (set(range(min(seats), max(seats) + 1)) - seats).pop()
print(answer2)
