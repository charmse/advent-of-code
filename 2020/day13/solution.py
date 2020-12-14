""" Day 13: Shuttle Search """

from sympy.ntheory.modular import solve_congruence


def part_one(target, buses):
    buses = [b[1] for b in buses]
    buses = list(map(int, list(filter(lambda x: x != 'x', buses))))
    remainders = list(map(lambda b: target % b, buses))
    closest = buses[remainders.index(max(remainders))]
    time_to_wait = (target - max(remainders) + closest) - target
    return closest * time_to_wait


def part_two(buses):
    # Takes too long
    # count = 0
    # bdict = {}
    # for b in buses:
    #    if b != 'x':
    #        bdict[b] = count
    #    count += 1
    # bkeys = list(map(int, list(bdict.keys())))
    # bvals = list(bdict.values())
    # for i in range(0, bkeys[0]*10000000000000000, bkeys[0]):
    #     flag = True
    #     for k, v in zip(bkeys[1:], bvals[1:]):
    #         n = i - (i % k) + k
    #         if n - i != v:
    #             flag = False
    #     if flag:
    #         return i
    return solve_congruence(*buses)[0]


def read_lines(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        lines = list(map(str.strip, file.readlines()))
        target = int(lines[0])
        buses = [(-i, int(x)) for i, x in enumerate(lines[1].split(',')) if x != 'x']
        return target, buses


def main():
    """ fetch input, perform both parts, and print results"""

    # Read example input
    ex_target, ex_buses = read_lines('ex.txt')

    # Read input
    target, buses = read_lines('in.txt')

    ## Part 1
    print(part_one(ex_target, ex_buses))
    print(part_one(target, buses))

    ## Part 2
    print(part_two(ex_buses))
    print(part_two(buses))

    return 0


if __name__ == "__main__":
    main()
