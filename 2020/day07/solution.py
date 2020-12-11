""" Day 7: Handy Haversacks """

import functools
import time

def get_bag_set(line):
    line = line[:-1]
    (bag, set_) = line.split('contain')
    get_name = lambda x, i, j: x.split()[i] + x.split()[j]
    bag = get_name(bag, 0, 1)
    inside = list(map(str.strip, set_.split(',')))
    inside_ = set(map(lambda x: get_name(x, 1, 2), inside))
    return (bag, inside_)

def fix_name(name):
    if name[-1] == 's':
        return name[:-1]
    else:
        return name

def fix_number(number):
    if number == 'no':
        return 1
    else:
        return number

def get_bag_set_with_number(line):
    line = line[:-1]
    (bag, set_) = line.split('contain')
    get_name = lambda x, i, j: x.split()[i] + x.split()[j]
    bag = get_name(bag, 0, 1)
    inside = list(map(str.strip, set_.split(',')))
    inside_ = set(map(lambda x: (fix_number(x.split()[0]), fix_name(get_name(x, 1, 2))), inside))
    return (bag, inside_)

def find_bag(item, bag_sets_with_number):
    for (bag, set_) in bag_sets_with_number:
        if item == bag:
            return (bag, set_)
    return ()

def get_bag(name, bag_set):
    for bag in bag_set:
        if bag[0] == name:
            return bag
    return ()


def calculate(item, bag_set):
    if item[1] == 'otherbag':
        return 1
    sum = 0
    bag = get_bag(item[1], bag_set)
    for b in bag[1]:
        print(b[0])
        print(calculate(b, bag_set))
        sum += (b[0] * calculate(b, bag_set))
    return sum

def main():
    """ fetch input, perform both parts, and print results"""

    # Read Input
    with open('./in.txt', 'r', encoding='utf-8') as file:
        lines = list(map(str.strip, file.readlines()))
        bag_sets = list(map(get_bag_set, lines))
        bag_sets_with_number = list(map(get_bag_set_with_number, lines))

    print('Input:\n')
    for b in bag_sets:
        print(f'{b}')
    print('\nFinding solutions...\n')

    ## Part 1
    begin = time.time()

    target = 'shinygold'
    contain_target = set()
    old_lenth = -1
    while old_lenth != len(contain_target):
        old_lenth = len(contain_target)
        for (bag, set_) in bag_sets:
            if target in set_ or len(set_.intersection(contain_target)) != 0:
                contain_target.add(bag)

    time.sleep(1)
    time_taken = time.time() - begin

    # Print results and solution
    print(f'Part 1: {len(contain_target)}')
    print(f'Time took: {time_taken}\n')

    ## Part 2
    begin = time.time()

    # Get shinygold bag tuple
    gold_bag = []
    for item in bag_sets_with_number:
        bag = item[0]
        set_ = item[1]
        if bag == target:
            gold_bag.append(item)
            bag_sets_with_number.remove(item)
            break


    # Get tree of bags
    old_bag = []
    while len(old_bag) != len(gold_bag):
        old_bag = gold_bag
        for (bag, items) in gold_bag:
            for (n, item) in items:
                if item != 'otherbag':
                    gold_bag.append(find_bag(item, bag_sets_with_number))

    for bag in gold_bag:
       print(bag)

    # Calculate solution
    solution = calculate((1, target), gold_bag)

    time.sleep(1)
    time_taken = time.time() - begin

    # Print results and solution
    print(f'Part 2: {solution}')
    print(f'Time took: {time_taken}\n')

if __name__ == "__main__":
    main()

