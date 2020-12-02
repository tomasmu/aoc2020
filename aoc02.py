#input
import os
file = os.path.basename(__file__).replace('.py', '.txt')
input = open(file).read().splitlines()

#format
array = input

#puzzle 1
import re
def isValid(string):
    [min, max, char, password] = re.split(r"-|: |\s", string)
    [min, max] = [int(min), int(max)]
    count = password.count(char)
    return count >= min and count <= max

result1 = sum(int(isValid(n)) for n in array)
print(result1)

#puzzle 2
def isValid2(string):
    [min, max, char, password] = re.split(r"-|: |\s", string)
    [min, max] = [int(min), int(max)]
    return (password[min - 1] == char) ^ (password[max - 1] == char)

result2 = sum(int(isValid2(n)) for n in array)
print(result2)
