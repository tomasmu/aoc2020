import collections
import os
import numpy
import functools
import itertools
import re
import math

# input
file = os.path.basename(__file__).replace('.py', '_example.txt')
file = os.path.basename(__file__).replace('.py', '_input.txt')
raw_input = open(file).read()
print('input:', file)

if re.search('\n\n', raw_input):
    puzzle = raw_input.split('\n\n')
else:
    puzzle = raw_input.splitlines()

instructions = []
for instruction in puzzle:
    op, value = instruction.split(' = ')
    if op != 'mask':
        op = int(re.search(r'(?P<op>\d+)', op).group('op'))
        value = int(value)
    instructions.append((op, value))

# puzzle 1
def apply_mask(value, mask):
    erasing_bitmask = int(mask.replace('X', '1'), 2)
    overwriting_bitmask = int(mask.replace('X', '0'), 2)
    return value & erasing_bitmask | overwriting_bitmask

def run_initialization(instructions):
    memory = dict()
    for instruction in instructions:
        x, value = instruction
        if x == 'mask':
            mask = value
        else:
            memory[x] = apply_mask(value, mask)
    return sum(memory.values())

answer1 = run_initialization(instructions)
print(answer1)

# puzzle 2
def get_floating_array(address, floating_bits):
    if len(floating_bits) == 0:
        return [address]
    else:
        bit_index, *tail = floating_bits
        return functools.reduce(lambda a, c: a + get_floating_array(address | c, tail), [0, 1 << bit_index], [])

def memory_address_decoder(address, mask):
    erasing_bitmask = int(mask.replace('0', '1').replace('X', '0'), 2)
    overwriting_bitmask = int(mask.replace('X', '0'), 2)
    base_address = address & erasing_bitmask | overwriting_bitmask

    floating_bit_indices = [i for i, bit in enumerate(mask[::-1]) if bit == 'X']
    floating_addresses = get_floating_array(base_address, floating_bit_indices)

    return floating_addresses

def run_initialization_emulator(instructions):
    memory = dict()
    for instruction in instructions:
        x, value = instruction
        if x == 'mask':
            mask = value
        else:
            for address in memory_address_decoder(x, mask):
                memory[address] = value
    return sum(memory.values())

answer2 = run_initialization_emulator(instructions)
print(answer2)
