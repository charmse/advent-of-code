""" Day 10: Adapter Array """

import collections


def part_one(ns):
    one = 0
    three = 0
    for i, j in zip(ns, ns[1:]):
        if j - i == 3:
            three += 1
        elif j - i == 1:
            one += 1
    return one*three


def part_two(ns):
    paths = collections.defaultdict(int)
    paths[0] = 1
    for i in range(1, len(ns)):
        for j in range(i)[::-1]:
            if ns[i] - ns[j] > 3:
                break
            paths[i] += paths[j]
    return paths[len(ns)-1]


def main():
    """ fetch input, perform both parts, and print results"""

    # Read Input
    with open('./ex.txt', 'r', encoding='utf-8') as file:
        ex_ns = list(map(int, map(str.strip, file.readlines())))
        ex_ns = [0] + sorted(ex_ns) + [max(ex_ns) + 3]

    # Read Input
    with open('./in.txt', 'r', encoding='utf-8') as file:
        ns = list(map(int, map(str.strip, file.readlines())))
        ns = [0] + sorted(ns) + [max(ns) + 3]

    print(ns[1:-1])

    ## Part 1
    print(part_one(ex_ns))
    print(part_one(ns))


    ## Part 2
    print(part_two(ex_ns))
    print(part_two(ns))


if __name__ == "__main__":
    main()

