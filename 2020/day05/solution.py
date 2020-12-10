""" Day 5: Binary Boarding """

import math
import time

def get_seat_id(line):
    r1 = 0
    r2 = 127
    c1 = 0
    c2 = 7
    for c in line:
        dist_r = (r2 - r1)/2
        dist_c = (c2 - c1)/2
        if c == 'F':
            r2 = r2 - math.floor(dist_r)
        if c == 'B':
            r1 = r1 + math.ceil(dist_r)
        if c == 'L':
            c2 = c2 - math.ceil(dist_c)
        if c == 'R':
            c1 = c1 + math.floor(dist_c)
    return (r1 * 8) + c2

def main():
    """ fetch input, time and call both parts, and print results"""

    # Read Input
    with open('./in.txt', 'r', encoding='utf-8') as file:
        lines = list(map(str.strip, file.readlines()))

    #Find all seat_ids
    seat_ids = list(map(get_seat_id, lines))

    ## Part 1
    print(f'Highest seat ID: {max(seat_ids)}')

    ## Part 2
    for s in sorted(seat_ids):
        if s + 1 not in seat_ids and s + 2 in seat_ids:
            my_seat = s+1
    print(f'My seat ID: {my_seat}')

if __name__ == "__main__":
    main()

