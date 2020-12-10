""" Day _: _ """

import time

def main():
    """ fetch input, perform both parts, and print results"""

    # Read Input
    with open('./in.txt', 'r', encoding='utf-8') as file:
        lines = list(map(str.strip, file.readlines()))

    print('Input:\n')
    for l in lines:
        print(f'{l}')
    print('\nFinding solutions...\n')

    ## Part 1
    begin = time.time()

    part_one = 1

    time.sleep(1)
    time_taken = time.time() - begin

    # Print results and solution
    print(f'Part 1: {part_one}')
    print(f'Time took: {time_taken}\n')

    ## Part 2
    begin = time.time()

    part_two = 2

    time.sleep(1)
    time_taken = time.time() - begin

    # Print results and solution
    print(f'Part 2: {part_two}')
    print(f'Time took: {time_taken}\n')

if __name__ == "__main__":
    main()

