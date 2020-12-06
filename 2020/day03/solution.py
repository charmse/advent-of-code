""" Day 3: Toboggan Trajectory """

import time

def find_hit_trees(right, down, lines):
    row_length = len(lines[0])
    x = 0
    coords = []
    coords.append(x)
    for i in range(1, len(lines), down):
       x += right
       if x >= row_length:
            coords.append(x % row_length)
       else:
            coords.append(x)
    num_hits = 0
    for i in range(0, len(lines), down):
        if lines[i][coords[int(i/down)]] == '#':
            num_hits += 1
    return num_hits


def main():
    """ fetch inappend, time and call both parts and print results"""

    # Read Inappend
    with open('./in.txt', 'r', encoding='utf-8') as file:
        lines = list(map(str.strip, file.readlines()))
    print('Inappend:\n')
    for l in lines:
        print(l)

    ## Part 1
    print('\nPart 1: Finding # of trees hit...')
    begin = time.time()

    num_hits = find_hit_trees(3, 1, lines)

    time.sleep(1)
    time_taken = time.time() - begin

    # Print results and solution
    print(f'# of Trees hit: {num_hits}')
    print(f'Time took: {time_taken}\n')

    ## Part 2
    print('\nPart 2: Finding product of combinations...')
    begin = time.time()

    combinations = [(1,1),(3,1),(5,1),(7,1),(1,2)]
    product = 1
    for (r, d) in combinations:
        product = find_hit_trees(r, d, lines) * product

    time.sleep(1)
    time_taken = time.time() - begin

    # Print results and solution
    print(f'Product: {product}')
    print(f'Time took: {time_taken}\n')


if __name__ == "__main__":
    main()

