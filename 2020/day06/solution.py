""" Day 6: Custom Customs """

import time


def get_groups(lines):
    group = []
    groups = []
    for line in lines:
        if line == '':
            groups.append(group)
            group = []
        else:
            group.append(line)
    groups.append(group)
    return groups


def part_one(groups):
    total = 0
    for group in groups:
        questions_answered = set(''.join(group))
        total += len(questions_answered)
    return total


def part_two(groups):
    total = 0
    for group in groups:
        questions = set('abcdefghijklmnopqrstuvwxyz')
        for member in group:
            questions = questions.intersection(set(member))
        total += len(questions)
    return total


def main():
    """ fetch input, perform both parts, and print results"""

    # Read Input
    with open('./in.txt', 'r', encoding='utf-8') as file:
        lines = list(map(str.strip, file.readlines()))
        groups = get_groups(lines)

    print('Input:\n')
    for group in groups:
        print(f'{group}')
    print('\nFinding solutions...\n')

    ## Part 1
    begin = time.time()
    total = part_one(groups)
    time.sleep(1)
    time_taken = time.time() - begin

    # Print results and solution
    print(f'Total number of yes\'s: {total}')
    print(f'Time took: {time_taken}\n')

    ## Part 2
    begin = time.time()
    total = part_two(groups)
    time.sleep(1)
    time_taken = time.time() - begin

    # Print results and solution
    print(f'Total of all same questions answered by groups: {total}')
    print(f'Time took: {time_taken}\n')

if __name__ == "__main__":
    main()

