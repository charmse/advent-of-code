""" Day 12: Rain Risk """


class Ship:
    def __init__(self):
        self.deg_sign = {'R': 1, 'L': -1}
        self.dir = ['N', 'E', 'S', 'W']
        self.facing = {'N': False, 'E': True, 'S': False, 'W': False}
        self.state = {'N': 0, 'E': 0, 'S': 0, 'W': 0}
        self.waypoint = {'N': 1, 'E': 10, 'S': 0, 'W': 0}

    def curr(self):
        return list(self.facing.keys())[list(self.facing.values()).index(True)]

    def move(self, ins):
        if ins[0] == 'R' or ins[0] == 'L':
            self.steer(ins[0], int(ins[1:]))
        elif ins[0] == 'F':
            self.update(self.curr(), int(ins[1:]))
        else:
            self.update(ins[0], int(ins[1:]))

    def steer(self, dir, deg):
        curr = self. curr()
        curr_index = self.dir.index(self.curr())
        new_index = (curr_index + self.deg_sign[dir] * int(deg/90)) % 4
        new = self.dir[new_index]
        self.facing[new] = True
        self.facing[curr] = False

    def update(self, dir, units):
        self.state[dir] += units

    def move2(self, ins):
        if ins[0] == 'R' or ins[0] == 'L':
            self.rotate_waypt(ins[0], int(ins[1:]))
        elif ins[0] == 'F':
            self.move_to_waypt(int(ins[1:]))
        else:
            self.update_waypt(ins[0], int(ins[1:]))

    def rotate_waypt(self, dir, deg):
        times = int(deg/90)
        for n in range(times):
            n = self.waypoint['N']
            for i in range(1, len(self.waypoint)):
                last = self.waypoint[self.dir[self.deg_sign[dir]*i]]
                self.waypoint[self.dir[self.deg_sign[dir]*i]] = n
                n = last
            self.waypoint['N'] = n

    def update_waypt(self, dir, units):
        self.waypoint[dir] += units

    def move_to_waypt(self, units):
        self.state['N'] += units * self.waypoint['N']
        self.state['E'] += units * self.waypoint['E']
        self.state['S'] += units * self.waypoint['S']
        self.state['W'] += units * self.waypoint['W']

    def manhattan_dist(self):
        s = self.state
        return abs(s['E']-s['W']) + abs(s['N']-s['S'])


def part_one(ins):
    ship = Ship()
    for i in ins:
        ship.move(i)
    return ship.manhattan_dist()


def part_two(ins):
    ship = Ship()
    for i in ins:
        ship.move2(i)
    return ship.manhattan_dist()


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
