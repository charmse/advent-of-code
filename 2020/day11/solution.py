""" Day 11: Seating System """

from collections import Counter as ctr
from collections import defaultdict as ddict
import copy


def count(grid):
    count = 0
    for row in grid:
        count += ctr(row)['#']
    return count


def nearest_seat(grid, i, j, r, c, pss):
    if pss == True:
        return grid[i+r][j+c]
    while len(grid) > i+r > -1 and len(grid[i]) > j+c > -1:
        if r == c == 0:
            return grid[i+r][j+c]
        if grid[i+r][j+c] != '.':
            return grid[i+r][j+c]
        if r < 0:
            r -= 1
        elif r > 0:
            r += 1
        if c < 0:
            c -= 1
        elif c > 0:
            c += 1
    return 'L'


def nbs(i, j, grid, pss):
    nbs = ddict(tuple)
    vals = [-1, 0, 1]
    for r in vals:
        if len(grid) > i+r > -1:
            for c in vals:
                if len(grid[i]) > j+c > -1:
                    nbs[(r, c)] = nearest_seat(grid, i, j, r, c, pss)
    nbs[(0, 0)] = '-'
    return nbs


def step(grid, threshold, pss):
    new_grid = copy.deepcopy(grid)
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            num_occ = ctr(nbs(i, j, grid, pss).values())['#']
            if grid[i][j] == 'L' and num_occ == 0:
                new_grid[i][j] = '#'
            elif grid[i][j] == '#' and num_occ >= threshold:
                new_grid[i][j] = 'L'
    return new_grid


def part_one(grid):
    num_occ = 0
    prev_occ = -1
    while num_occ != prev_occ:
        prev_occ = num_occ
        grid = step(grid, 4, True)
        num_occ = count(grid)
    return num_occ


def part_two(grid):
    num_occ = 0
    prev_occ = -1
    while num_occ != prev_occ:
        prev_occ = num_occ
        grid = step(grid, 5, False)
        num_occ = count(grid)
    return num_occ


def main():
    """ fetch input, perform both parts, and print results"""

    # Read example input
    with open('./ex.txt', 'r', encoding='utf-8') as file:
        ex_grid = list(map(list, map(str.strip, file.readlines())))

    # Read input
    with open('./in.txt', 'r', encoding='utf-8') as file:
        grid = list(map(list, map(str.strip, file.readlines())))

    ## Part 1
    print(part_one(ex_grid))
    print(part_one(grid))

    ## Part 2
    print(part_two(ex_grid))
    print(part_two(grid))

    return 0


if __name__ == "__main__":
    main()

