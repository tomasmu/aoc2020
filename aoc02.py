import re
import os

# input
file = os.path.basename(__file__).replace('.py', '.txt')
input = open(file).read()

# format
array = input.splitlines()

# puzzle 1
def is_valid_password(string):
    [min_max, char, password] = re.split(r":?\s", string)
    [min, max] = map(int, min_max.split('-'))
    return min <= password.count(char) <= max

answer1 = sum(map(is_valid_password, array))
print(answer1)

# puzzle 2
def is_valid_password_2(string):
    [min_max, char, password] = re.search(r"^(\d+-\d+) (\w): (\w+)", string).groups()
    [min, max] = [int(n) - 1 for n in min_max.split('-')]
    return (password[min] == char) ^ (password[max] == char)

answer2 = sum(map(is_valid_password_2, array))
print(answer2)
