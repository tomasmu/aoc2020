#input
import os
file = os.path.basename(__file__).replace('.py', '_input.txt')
input = open(file).read()

#format
array = input.splitlines()

#puzzle 1
instructions = [line.split() for line in array]
instructions = list(map(lambda op_arg: (op_arg[0], int(op_arg[1])), instructions))

def get_value_at_loop(instructions):
    i = 0
    visited = set()
    accumulator = 0
    while i not in visited:
        visited.add(i)
        op, arg = instructions[i]
        if op == 'acc':
            accumulator += arg
        elif op == 'jmp':
            i += (arg - 1)
        i += 1
    return accumulator

answer1 = get_value_at_loop(instructions)
print (answer1)

#puzzle 2
def get_value(instructions):
    i = 0
    visited = set()
    accumulator = 0
    while i < len(instructions):
        if i in visited:
            return None
        visited.add(i)
        op, arg = instructions[i]
        if op == 'acc':
            accumulator += arg
        elif op == 'jmp':
            i += (arg - 1)
        i += 1
    return accumulator

def do_stuff(instructions):
    translate = { 'jmp': 'nop', 'nop': 'jmp' }
    for i in range(len(instructions)):
        if instructions[i][0] not in translate:
            continue
        instructions[i] = (translate[instructions[i][0]], instructions[i][1])
        result = get_value(instructions)
        if result != None:
            return result
        instructions[i] = (translate[instructions[i][0]], instructions[i][1])

answer2 = do_stuff(instructions)
print (answer2)
