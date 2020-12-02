""" Day 1: Report Repair """

import time


def find_pair(numbers):
    """ dumb function to find pair that sum to 2020 """
    for i in numbers:
        difference = 2020 - i
        if difference in numbers:
            return (i, difference)
    return (0, 0)


def main():
    """ fetch input, time and call find_pair and print results"""
    # Read Input
    with open('./in.txt', 'r', encoding='utf-8') as file:
        numbers = list(map(int, file.readlines()))
    print(f'Input: {input}\n')

    # Find pair
    print('Finding pair...')
    begin = time.time()
    pair = find_pair(numbers)
    time.sleep(1)
    time_taken = time.time() - begin

    # Print results and solution
    print(f'Pair: {numbers}')
    print(f'Solution: {pair[0]*pair[1]}')
    print(f'Time took: {time_taken}')


if __name__ == "__main__":
    main()

