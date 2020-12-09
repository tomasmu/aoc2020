# input
import os
import re
file = os.path.basename(__file__).replace('.py', '.txt')
input = open(file).read()

# format
array = input.splitlines()

# puzzle 1, first solution
def get_pos(arr, chars):
    if len(chars) == 0:
        return arr[0]
    if re.match("F|L", chars[0]):
        return get_pos(arr[:int(len(arr)/2)], chars[1:])
    if re.match("B|R", chars[0]):
        return get_pos(arr[int(len(arr)/2):], chars[1:])

def get_seat_array(chars):
    rows = [n for n in range(128)]
    cols = [n for n in range(8)]
    return 8 * get_pos(rows, chars[0:7]) + get_pos(cols, chars[7:])

# puzzle 1, after realising input represents binary numbers
def get_seat(chars):
    return int(chars.replace("F", "0").replace("L", "0").replace("B", "1").replace("R", "1"), 2)

answer1 = max(map(get_seat, array))
print(answer1)

# puzzle 2
seats = set(get_seat(chars) for chars in array)
answer2 = (set(range(min(seats), max(seats) + 1)) - seats).pop()
print(answer2)
