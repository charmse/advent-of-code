""" Day 9: Encoding Error """

import itertools


def part_one(ns, pre):
    for i in range(len(ns[pre:])):
        if i + pre >= len(ns):
            break
        pre_ns = ns[i:i+pre]
        rest = ns[pre+i:]
        combos = list(map(lambda x: x[0] + x[1], itertools.combinations(pre_ns, 2)))
        if rest[0] not in combos:
            return rest[0]
            break


def part_two(ns, pre):
    invalid_n = part_one(ns, pre)
    for r in range(2, 20):
        for i in range(len(ns)):
            n = ns[i:i+r]
            if sum(n) == invalid_n:
                return max(n) + min(n)
    return invalid_n


def main():
    """ fetch input, perform both parts, and print results"""

    # Read Input
    with open('./ex.txt', 'r', encoding='utf-8') as file:
        ex_lines = list(map(int, map(str.strip, file.readlines())))

    # Read Input
    with open('./in.txt', 'r', encoding='utf-8') as file:
        lines = list(map(int, map(str.strip, file.readlines())))


    ## Part 1
    print(part_one(ex_lines, 5))
    print(part_one(lines, 25))


    ## Part 2
    print(part_two(ex_lines, 5))
    print(part_two(lines, 25))


if __name__ == "__main__":
    main()

