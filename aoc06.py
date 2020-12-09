# input
import collections
import os
file = os.path.basename(__file__).replace('.py', '_input.txt')
input = open(file).read()

# format
array = input.split('\n\n')

# puzzle 1
answers = [line.split() for line in array]
answer_groups = [[list(b) for b in a] for a in answers]

answer1 = sum(len(set().union(*(set(a) for a in g))) for g in answer_groups)
print(answer1)

# puzzle 2
def flatten_array(arr): return [x for xs in arr for x in xs]

answer2 = sum(list(collections.Counter(flatten_array(g)).values()).count(len(g)) for g in answer_groups)
print(answer2)
