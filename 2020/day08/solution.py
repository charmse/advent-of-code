""" Day 8: _ """

class Operation:
    def __init__(self, line):
        _ = line.strip().split()
        self.type = _[0]
        self.val = int(_[1])
        # if _[1][0] == '+':
         #   self.val = int(_[1][1:])

    def __str__(self):
        return f'{self.type}, {self.val}'


def part_one(ops):
    """ Part 1 """
    acc = 0
    i = 0
    history = []
    ended = False
    while True:
        if i == len(ops):
            ended = True
            break

        op = ops[i]
        if op in history:
            break

        if op.type == 'acc':
            acc += op.val
            i += 1
        elif op.type == 'jmp':
            i += op.val
        else:
            i += 1
        history.append(op)
    return (acc, ended)


def part_two(ops):
    """ Part 2 """
    for i in range(len(ops)):
        op = ops[i]
        original_type = op.type
        if op.type == 'jmp':
            op.type = 'nop'
        elif op.type == 'nop':
            op.type = 'jmp'
        else:
            continue
        (acc, ended) = part_one(ops)
        if ended == True:
            return acc
        else:
            op.type = original_type
    return 0


def main():
    """ fetch input, perform both parts, and print results"""

    # Read Input
    with open('./ex.txt', 'r', encoding='utf-8') as file:
        ex_ops = list(map(Operation, file.readlines()))

    # Read Input
    with open('./in.txt', 'r', encoding='utf-8') as file:
        ops = list(map(Operation, file.readlines()))


    ## Part 1
    print(part_one(ex_ops)[0])
    print(part_one(ops)[0])


    ## Part 2
    print(part_two(ex_ops))
    print(part_two(ops))


if __name__ == "__main__":
    main()
