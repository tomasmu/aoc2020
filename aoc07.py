#input
import os
import re
file = os.path.basename(__file__).replace('.py', '_input.txt')
input = open(file).read()

#format
array = input.splitlines()
rules = dict()
for arr in array:
    arr = arr.strip(' .').replace(' no ', ' 0 ').replace(' bags', ' bag')
    match = re.search(r'(?P<parent>.+) contain (?P<children>.*)', arr)
    parent = match.group('parent')
    children = match.group('children').split(', ')
    rules[parent] = children

#puzzle 1
def get_parents_containing(color):
    return [parent for parent, bags in rules.items() for bag in bags if re.search(color, bag)]

def find_parents(parents, acc = []):
    for bag in parents:
        contains = get_parents_containing(bag)
        acc.extend(contains)
        find_parents(contains)
    return acc

containing_gold = find_parents(['shiny gold bag'])
answer1 = len(set(containing_gold))
print (answer1)

#puzzle 2
def containing(color):
    if color == 'other bag':
        return 0
    count_name = [(int(count), name) for count, name in [bag.split(' ', 1) for bag in rules[color]]]
    return sum(count + count * containing(name) for count, name in count_name)

answer2 = containing('shiny gold bag')
print (answer2)
