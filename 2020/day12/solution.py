""" Day 12: Rain Risk """

class Ship:
    def __init__(self):
        self.deg_sign = {'R': 1, 'L': -1}
        self.dir = ['N', 'E', 'S', 'W']
        self.facing = {'N': False, 'E': True, 'S': False, 'W': False}
        self.state = {'N': 0, 'E': 0, 'S': 0, 'W': 0}
        self.curr = lambda : list(self.facing.keys())[list(self.facing.values()).index(True)]

    def move(self, ins):
        if ins[0] == 'R' or ins[0] == 'L':
            self.steer(ins[0], int(ins[1:]))
        elif ins[0] == 'F':
            self.update(self.curr(), int(ins[1:]))
        else:
            self.update(ins[0] , int(ins[1:]))

    def steer(self, dir, deg):
        curr = self. curr()
        curr_index = self.dir.index(self.curr())
        new_index = (curr_index + self.deg_sign[dir] * int(deg/90)) % 4
        new = self.dir[new_index]
        self.facing[new] = True
        self.facing[curr] = False

    def update(self, dir, units):
        self.state[dir] += units

    def manhattan_dist(self):
        s = self.state
        return abs(s['E']-s['W']) + abs(s['N']-s['S'])


def part_one(ins):
    ship = Ship()
    for i in ins:
        ship.move(i)
    return ship.manhattan_dist()


def part_two(ins):
    return 0


def main():
    """ fetch input, perform both parts, and print results"""

    # Read example input
    with open('./ex.txt', 'r', encoding='utf-8') as file:
        ex_ins = list(map(str.strip, file.readlines()))

    # Read input
    with open('./in.txt', 'r', encoding='utf-8') as file:
        ins = list(map(str.strip, file.readlines()))

    ## Part 1
    print(part_one(ex_ins))
    print(part_one(ins))

    ## Part 2
    print(part_two(ex_ins))
    print(part_two(ins))

    return 0


if __name__ == "__main__":
    main()

