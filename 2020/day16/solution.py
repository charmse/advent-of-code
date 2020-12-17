""" Day 16: Ticket Translation """

from itertools import permutations
import numpy as np


def p1(fields, tickets):
    fs = [vs for n, vs in fields]
    error = []
    for ticket in tickets:
        for t in ticket:
            valid = [f[2] <= t <= f[3] or f[0] <= t <= f[1] for f in fs]
            if True not in valid:
                error.append(t)
    return error


def print_dict(d):
    cols = list(map(list, zip(*list(d.values()))))
    print(f'\t'.expandtabs(20), end='')
    for c in cols:
        print(sum(c), end=' ')
    print(f'\t\n'.expandtabs(20))
    for k in d.keys():
         print(f'{k}:\t'.expandtabs(20), end='')
         print(*d[k], end='\t\t')
         print(sum(d[k]))


def p2(fields, tickets):
    bad = p1(fields, tickets[1:])
    ts = list(filter(lambda t: not(any(b in t for b in bad)), tickets[1:]))
    tts = list(map(list, zip(*ts)))
    names = [n for n, vs in fields]
    vals = [vs for n, vs in fields]
    d = dict()
    for n, v in zip(names, vals):
        valid = []
        for c in tts:
            f = 1
            for r in c:
                if not v[0] <= r <= v[1] and not v[2] <= r <= v[3]:
                    f = 0
                    break
            valid.append(f)
        d[n] = valid
    print_dict(d)
    return 1



def parse(l):
    name, vals = l.split(':')
    vals = vals.strip().split('or')
    vals = vals[0].strip() + '-' + vals[1].strip()
    return (name, [int(i) for i in vals.strip().split('-')])


with open('in.txt', 'r', encoding='utf-8') as file:
    ls = list(map(str.strip, file.readlines()))
    fields = [parse(l) for l in ls[:ls.index('')]]
    tickets = [list(map(int, l.split(','))) for l in [ls[ls.index('')+2]] + ls[ls.index('')+5:]]
    print(sum(p1(fields, tickets[1:])))
    print(p2(fields, tickets))
