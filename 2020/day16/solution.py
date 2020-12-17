""" Day 16: Ticket Translation """

from collections import defaultdict


def invalid(fields, tickets):
    error = []
    for ticket in tickets:
        for t in ticket:
            valid = [f[2] <= t <= f[3] or f[0] <= t <= f[1] for f in fields]
            if True not in valid:
                error.append(t)
    return error

def solve(fields, tickets):
    bad = invalid(fields, tickets[1:])
    ts = list(filter(lambda t: not(any(b in t for b in bad)), tickets[1:]))
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
    print(sum(invalid(fields, tickets[1:])))
    print(solve(fields, tickets))
