""" Day 15: Rambunctious Recitation """

from collections import defaultdict


def solve(ns, nth):
    spoken = defaultdict(list)
    [spoken[ns[i]].append(i) for i in range(len(ns))]
    last = ns[-1]
    for i in range(len(ns), nth):
        last = spoken[last][-1] - spoken[last][-2] if len(spoken[last]) > 1 else 0
        spoken[last].append(i)
    return last


with open('in.txt', 'r', encoding='utf-8') as file:
    ns = list(map(int, file.read().strip().split(',')))
    print(solve(ns, 2020))
    print(solve(ns, 30000000))
