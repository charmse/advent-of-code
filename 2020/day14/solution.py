""" Day 14: Docking Data """

from collections import Counter
from copy import copy
from itertools import product


class Mem:
    def __init__(self, l):
        self.loc = int(l.split('[')[1].split(']')[0])
        self.val = '{0:036b}'.format(int(l.split('=')[1].strip()))


class Mask:
    def __init__(self, l):
        self.val = l.split('=')[1].strip()


def part_one(data):
    mem = dict()
    mask = ''.rjust(36, 'X')
    for d in data:
        if 'X' in d.val:
            mask = d.val
            continue
        mem[d.loc] = int(''.join([v if m == 'X' else m for m, v in zip(mask, d.val)]), 2)
    return sum(list(mem.values()))


def part_two(data):
    mem = dict()
    mask = ''.rjust(36, 'X')
    for d in data:
        if 'X' in d.val:
            mask = d.val
            continue
        val = '{0:036b}'.format(int(d.loc))
        address = ['1' if m == '1' else v for m, v in zip(mask, val)]
        address = ['X' if m == 'X' else a for m, a in zip(mask, address)]
        x_locs = [i for i, ltr in enumerate(address) if ltr == 'X']
        for c in product(['0', '1'], repeat = Counter(address)['X']):
            a = copy(address)
            for x, i in zip(x_locs, c):
                a[x] = i
            mem[''.join(a)] = int(d.val, 2)
    return sum(list(mem.values()))


with open('in.txt', 'r', encoding='utf-8') as file:
    ls = list(map(str.strip, file.readlines()))
    data = [Mem(l) if l[:3] == 'mem' else Mask(l) for l in ls]
    print(part_one(data))
    print(part_two(data))
