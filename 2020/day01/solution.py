""" Day 1: Report Repair """

import time
from absl import app
from absl import flags

FLAGS = flags.FLAGS

flags.DEFINE_integer('sum', 2020, 'sum of pairs in list to find solution for')

def part_one(numbers):
    """ dumb function to find pair that sum to 2020 """
    for i in numbers:
        if FLAGS.sum - i in numbers:
            return (i, FLAGS.sum - i)
    return (0, 0)



def part_two(numbers):
    """ dumb function to find three numbers that sum to 2020 """
    for i in numbers:
        j_start = 1
        for j in numbers[j_start:]:
            if FLAGS.sum - i - j in numbers[j_start + 1:]:
                return (i, j, FLAGS.sum - i - j)
        j_start += 1
    return (0, 0, 0)


def main(argv):
    """ fetch input, time and call both parts and print results"""

    # Read Input
    with open('./in.txt', 'r', encoding='utf-8') as file:
        numbers = list(map(int, file.readlines()))
    print(f'Input: {numbers}\n')

    # part 1
    print('Finding pair...')
    begin = time.time()
    pair = part_one(numbers)
    time.sleep(1)
    time_taken_1 = time.time() - begin

    # Print results and solution
    print(f'Part 1 Pair: {pair}')
    print(f'Part 1 Solution: {pair[0]*pair[1]}')
    print(f'Time took in part 1: {time_taken_1}\n')

    # part 2
    print('Finding triple...')
    begin = time.time()
    triple = part_two(numbers)
    time.sleep(1)
    time_taken_2 = time.time() - begin

    # Print results and solution
    print(f'Part 2 triple: {triple}')
    print(f'Part 2 Solution: {triple[0]*triple[1]*triple[2]}')
    print(f'Time took in part 2: {time_taken_2}\n')

if __name__ == "__main__":
    app.run(main)
