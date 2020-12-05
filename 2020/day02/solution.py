""" Day 2: Password Philosophy """

import functools
import time
from absl import app
from absl import flags

FLAGS = flags.FLAGS

flags.DEFINE_integer('sum', 2020, 'sum of pairs in list to find solution for')

class Password:
    """ Class to represent rules and password """
    def __init__(self, min, max, letter, password):
        self.min = min
        self.max = max
        self.letter = letter
        self.password = password

    def print(self):
        print(f'Min: {self.min}, Max: {self.max}, Letter: {self.letter}, Password: {self.password}')

    def is_valid_part_one(self):
        """ Is valid if it contains the letter between min and max times"""
        letter_count = 0
        for let in self.password:
            if let == self.letter:
                letter_count += 1
        if self.min <= letter_count <= self.max:
            return True
        return False

    def is_valid_part_two(self):
        """ Is valid if it contains the letter exists in one or both of the locations specified"""
        length = len(self.password)
        if self.min >= length or self.max > length:
            return False
        letter_at_min = self.password[self.min - 1]
        letter_at_max = self.password[self.max - 1]

        if letter_at_min == self.letter and letter_at_max != self.letter:
            return True
        if letter_at_min != self.letter and letter_at_max == self.letter:
            return True
        return False


def map_to_password(line):
    """ convert lines to Password object """
    space_split = line.split(' ')
    min_max_split = space_split[0].split('-')
    min = int(min_max_split[0])
    max = int(min_max_split[1])
    letter = space_split[1][0]
    password = space_split[2].rstrip()
    return Password(min, max, letter, password)


def main(argv):
    """ fetch input, time and call both parts and print results"""

    # Read Input
    with open('./in.txt', 'r', encoding='utf-8') as file:
        p_list = list(map(map_to_password, file.readlines()))
    print('Input:\n')
    # for password in p_list:
        # password.print()

    ## Part 1
    print('Part 1: Finding vaild passwords...')
    begin = time.time()
    valid_passwords = list(filter(lambda v: v, map(lambda p: p.is_valid_part_one(), p_list)))
    time.sleep(1)
    time_taken = time.time() - begin

    # Print results and solution
    print(f'Number of valid passwords: {len(valid_passwords)}')
    print(f'Time took: {time_taken}')
    print()

    ## Part 2
    print('Part 2: Finding vaild passwords...')
    begin = time.time()
    valid_passwords = list(filter(lambda v: v, map(lambda p: p.is_valid_part_two(), p_list)))
    time.sleep(1)
    time_taken = time.time() - begin

    # Print results and solution
    print(f'Number of valid passwords: {len(valid_passwords)}')
    print(f'Time took: {time_taken}')


if __name__ == "__main__":
    app.run(main)

