""" Day 16: Ticket Translation """

from itertools import permutations
import math


def p1(fields, tickets):
    fs = [vs for n, vs in fields]
    error = []
    for ticket in tickets:
        for t in ticket:
            valid = [f[2] <= t <= f[3] or f[0] <= t <= f[1] for f in fs]
            if True not in valid:
                error.append(t)
    return error

def remove_similar(fields, perms, valid):
    new_perms = []
    print(valid)
    for perm in perms:
        add = True
        for f, p, v in zip(fields, perm, valid):
            if f == p and not v:
                add = False
                break
        print(add)
        if add:
            new_perms.append(perms)
    return new_perms

def p2(fields, tickets):
    bad = p1(fields, tickets[1:])
    ts = list(filter(lambda t: not(any(b in t for b in bad)), tickets[1:]))
    names = [n for n, vs in fields]
    vals = [vs for n, vs in fields]
    perms = permutations(vals)
    while True:
        for fs in perms:
            all_t = True
            for vs in ts:
                valid = [f[0] <= v <= f[1] or f[2] <= v <= f[3] for f, v in zip(fs, vs)]
                if not all(valid):
                    all_t = False
                    break
            if all_t:
                order = [names[vals.index(o)] for o in fs]
                return math.prod([tickets[0][i] if order[i].startswith('depature') else 1 for i in range(len(order))])
            else:
                perms = remove_similar(fs, perms, valid)
                print(perms)
                break


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
