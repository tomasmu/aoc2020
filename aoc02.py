#input
import os
file = os.path.basename(__file__).replace('.py', '.txt')
input = open(file).read().splitlines()

#format
array = input

#puzzle 1
import re
def is_valid(string):
    [min, max, char, password] = re.split(r"-|: |\s", string)
    [min, max] = [int(min), int(max)]
    count = password.count(char)
    return count >= min and count <= max

answer1 = sum(is_valid(n) for n in array)
print(answer1)

#puzzle 2
def is_valid2(string):
    [min, max, char, password] = re.search(r"^(\d+)-(\d+) ([a-z]): ([a-z]+)", string).groups()
    [min, max] = [int(min), int(max)]
    return (password[min - 1] == char) ^ (password[max - 1] == char)

answer2 = sum(is_valid2(n) for n in array)
print(answer2)
