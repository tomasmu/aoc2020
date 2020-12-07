#input
import os
file = os.path.basename(__file__).replace('.py', '.txt')
input = open(file).read().splitlines()

#format
#todo: split on \n\n instead?
array = input

answer_current = []
answers = []
for line in array:
    if (line == ''):
        answers.append(answer_current)
        answer_current = []
    else:
        answer_current.append(line)
answers.append(answer_current)

answer_groups = [[list(b) for b in a] for a in answers]

#puzzle 1
answer1 = sum(len(set().union(*(set(a) for a in g))) for g in answer_groups)
print (answer1)

#puzzle 2
import collections
flatten_array = lambda arr: [x for xs in arr for x in xs]

answer2 = sum(list(collections.Counter(flatten_array(g)).values()).count(len(g)) for g in answer_groups)
print (answer2)
