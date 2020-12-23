# imports
import collections
import functools
import itertools
import math
import numpy
import os
import re

# input
file = os.path.basename(__file__).replace('.py', '_example.txt')
file = os.path.basename(__file__).replace('.py', '_input.txt')
raw_input = open(file).read()
print('input:', file)

if re.search('\n\n', raw_input):
    puzzle = raw_input.split('\n\n')
else:
    puzzle = raw_input.splitlines()

ticket_fields = puzzle[0].splitlines()
my_ticket = [int(n) for n in puzzle[1].splitlines()[1].split(',')]
nearby_tickets = [[int(n) for n in line.split(',')] for line in puzzle[2].splitlines()[1:]]

# puzzle 1
field_dicts = []
for ticket_field in ticket_fields:
    pattern = r'^(?P<field>.+): (?P<min1>\d+)-(?P<max1>\d+) or (?P<min2>\d+)-(?P<max2>\d+)$'
    match = re.search(pattern, ticket_field)
    if not match:
        assert False
    field_dict = {k: int(v) if v.isdigit() else v for k, v in match.groupdict().items()}
    field_dicts.append(field_dict)

def field_dict_validator(n, d):
    is_valid = d['min1'] <= n <= d['max1'] or d['min2'] <= n <= d['max2']
    return is_valid

def number_validator(n, field_dicts):
    is_valid = any(field_dict_validator(n, d) for d in field_dicts)
    return is_valid

answer1 = sum([n for nearby_ticket in nearby_tickets for n in nearby_ticket if not number_validator(n, field_dicts)])
print(answer1)

# puzzle 2
def ticket_validator(ticket, field_dicts):
    return all(number_validator(n, field_dicts) for n in ticket)

valid_tickets = [ticket for ticket in nearby_tickets if ticket_validator(ticket, field_dicts)]

#todo: there has to be a better way
field_name_cols_dict = { d['field']: set() for d in field_dicts }
for d in field_dicts:
    for col in range(len(valid_tickets[0])):
        is_valid_column = all(field_dict_validator(ticket[col], d) for ticket in valid_tickets)
        if is_valid_column:
            field_name_cols_dict[d['field']].add(col)

field_sets = sorted([(k, v) for k, v in field_name_cols_dict.items()], key=lambda x: len(x[1]))
field_id_dict = dict()
for i, x in enumerate(field_sets):
    a, b = field_sets[i]
    c = b.pop()
    field_id_dict[a] = c
    for j in range(i, len(field_sets)):
        field_sets[j] = [field_sets[j][0], field_sets[j][1].difference({c})]

departure_field_ids = [v for k, v in field_id_dict.items() if k.startswith('departure')]

answer2 = math.prod(my_ticket[i] for i in departure_field_ids)
print(answer2)
