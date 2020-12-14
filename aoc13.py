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

# puzzle 1
start_time = int(puzzle[0])
buses_with_id = [int(b) for b in puzzle[1].split(',') if b != 'x']

def get_next_bus_arrival(start_time, id):
    return (math.ceil(start_time / id) * id, id)

bus_arrivals = [get_next_bus_arrival(start_time, b) for b in buses_with_id]
next_time, next_id = min(bus_arrivals)

answer1 = next_id * (next_time - start_time)
print(answer1)

# puzzle 2
all_buses = puzzle[1].split(',')
index_bus = [(i, int(bus)) for i, bus in enumerate(all_buses) if bus != 'x']

def get_consecutive_bus_time(index_bus):
    bus_factor = 1      #high bus factor in this project
    t = 0
    for i, bus in index_bus:
        while (t + i) % bus != 0:
            t += bus_factor
        bus_factor *= bus
    return t

answer2 = get_consecutive_bus_time(index_bus)
print(answer2)
