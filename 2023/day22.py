from itertools import product
from copy import deepcopy
from tqdm import tqdm

# part1 is off by one, part2 is off by a lot, need to fix


def parse(data):
    bricks = []
    for line_nmbr, line in enumerate(data):
        line = line.split("~")
        brick = [[int(c) for c in b.split(",")] for b in line]
        brick.append(line_nmbr)
        bricks.append(brick)
    bricks.append([[0, 0, 0], [10, 10, 0], -1])
    print(bricks)
    bricks.sort(key=lambda x: x[0][2])
    return bricks


def drop(bricks):
    cpy = deepcopy(bricks)
    for idx, brick in enumerate(cpy):
        brick_z_length = int(brick[1][2] - brick[0][2])
        for below in [] if idx == 0 else cpy[idx - 1 :: -1]:
            for x, y in product(
                range(below[0][0], below[1][0] + 1), range(below[0][1], below[1][1] + 1)
            ):
                if brick[0][0] <= x <= brick[1][0] and brick[0][1] <= y <= brick[1][1]:
                    brick[0][2] = int(below[1][2] + 1)
                    brick[1][2] = int(brick[0][2] + brick_z_length)
                    break
            else:
                continue
            break
        else:
            brick[0][2] = 1
            brick[1][2] = int(brick[0][2] + brick_z_length)
    return cpy


def part1():
    with open("inputs/day22inp.txt", "r") as file:
        data = file.read().splitlines()
    bricks = parse(data)
    bricks = drop(bricks)
    disint = 0
    for brick in tqdm(bricks):
        bricks_copy1 = deepcopy(bricks)
        bricks_copy1.remove(brick)
        if bricks_copy1 == drop(bricks_copy1):
            disint += 1
    return disint


def part2():
    with open("inputs/day22inp.txt", "r") as file:
        data = file.read().splitlines()
    bricks = parse(data)
    bricks = drop(bricks)
    disint = 0
    for brick in tqdm(bricks[1:]):
        bricks_copy1 = deepcopy(bricks)
        bricks_copy1.remove(brick)
        new = drop(bricks_copy1)
        if bricks_copy1 != new:
            change = len([val for val in bricks_copy1 if not val in new])
            disint += change
    return disint


if __name__ == "__main__":
    print(part1())
    print(part2())
