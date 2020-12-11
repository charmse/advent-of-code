""" Day 7: Handy Haversacks """

# Part 1 Helpers
def get_bag_set(line):
    """ Tuple of bag and contents """
    line = line[:-1]
    (bag, set_) = line.split('contain')
    get_name = lambda x, i, j: x.split()[i] + x.split()[j]
    bag = get_name(bag, 0, 1)
    inside = list(map(str.strip, set_.split(',')))
    inside_ = set(map(lambda x: get_name(x, 1, 2), inside))
    return (bag, inside_)


def get_bag(name, bag_set):
    """ Get bag and its contents in list of bags """
    for bag in bag_set:
        if bag[0] == name:
            return bag
    return ()


# Part 2 Helpers
def fix_name(name):
    """ Remove plural ending """
    if name[-1] == 's':
        return name[:-1]
    else:
        return name


def fix_number(number):
    """ Convert number to int or return 1 in no """
    if number == 'no':
        return 0
    else:
        return int(number)


def get_bag_set_with_number(line):
    """ Get tuple of bag and contents with number """
    (bag, set_) = line[:-1].split('contain')
    bag = bag.split()[0] + bag.split()[1]
    inside = list(map(str.strip, set_.split(',')))
    inside_ = set(map(lambda x: (fix_number(x.split()[0]), fix_name(x.split()[1] + x.split()[2])), inside))
    return (bag, inside_)


def get_bag_(item, bag_sets_with_number):
    """ Get bag and its contents in list of bags """
    for (bag, set_) in bag_sets_with_number:
        if item == bag:
            return (bag, set_)
    return ()


def calculate(item, bag_set):
    """ Calculate the number of bags in target bag """
    if item[1] == 'otherbag':
        return 0
    sum = 0
    bag = get_bag(item[1], bag_set)
    for b in bag[1]:
        sum += (b[0] * calculate(b, bag_set))
    return sum + 1


# Main
def main():
    """ fetch input, perform both parts, and print results"""

    # Read Input
    with open('./in.txt', 'r', encoding='utf-8') as file:
        lines = list(map(str.strip, file.readlines()))
        bag_sets = list(map(get_bag_set, lines))
        bag_sets_with_number = list(map(get_bag_set_with_number, lines))

    target = 'shinygold'

    ## Part 1
    contain_target = set()
    old_lenth = -1
    while old_lenth != len(contain_target):
        old_lenth = len(contain_target)
        for (bag, set_) in bag_sets:
            if target in set_ or len(set_.intersection(contain_target)) != 0:
                contain_target.add(bag)

    # Print solution
    print(len(contain_target))


    ## Part 2
    # Get tree of bags
    target_list = [get_bag_(target, bag_sets_with_number)]
    old_list = []
    while len(old_list) != len(target_list):
        old_list = target_list
        for (bag, items) in target_list:
            for _, item in items:
                if item != 'otherbag':
                    target_list.append(get_bag_(item, bag_sets_with_number))

    # Get unique bags
    bag_list = []
    for bag in target_list:
        if bag not in bag_list:
            bag_list.append(bag)

    # Calculate solution
    print(calculate((1, target), bag_list) -1)

if __name__ == "__main__":
    main()
