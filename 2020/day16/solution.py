""" Day 16: Ticket Translation """

from collections import defaultdict


def solve(fields, tickets):
    ts = []
    for t in tickets:
        valid = True
        for f, t in zip(fields, t):
            print(f)
            print(t)
            a = f[0] <= t <= f[1] or f[2] <= t <= f[3]
            print(a)
            if not(f[0] <= t <= f[1] or f[2] <= t <= f[3]):
                valid = False
                break
        ts.append(valid)
    print(ts)
    return 1

def parse(l):
    name, vals = l.split(':')
    vals = vals.strip().split('or')
    vals = vals[0].strip() + '-' + vals[1].strip()
    return [int(i) for i in vals.strip().split('-')]

with open('ex.txt', 'r', encoding='utf-8') as file:
    ls = list(map(str.strip, file.readlines()))
    fields = [parse(l) for l in ls[:ls.index('')]]
    tickets = [list(map(int, l.split(','))) for l in [ls[ls.index('')+2]] + ls[ls.index('')+5:]]
    print(solve(fields, tickets))
