import numpy as np


def part1():
    sum = 0
    with open("inputs/day4inp.txt", "r") as file:
        data = file.read().splitlines()
    for line in data:
        line = line.replace("\n", "").replace("  ", " ")
        game = line.split(": ")[1]
        winning_nums = game.split(" | ")[0].split(" ")
        drawn_nums = game.split(" | ")[1].split(" ")
        intersection = [num for num in drawn_nums if num in winning_nums]
        score = 2 ** (len(intersection) - 1) if len(intersection) > 0 else 0
        sum += score
    return sum


def part2():
    dic = {k: 1 for k in range(187)}
    with open("inputs/day4inp.txt", "r") as file:
        data = file.read().splitlines()
    for line_nmbr, line in enumerate(data):
        line = line.replace("  ", " ")
        game = line.split(": ")[1]
        winning_nums = game.split(" | ")[0].split(" ")
        drawn_nums = game.split(" | ")[1].split(" ")
        intersection = [num for num in drawn_nums if num in winning_nums]
        points = len(intersection)
        for k in range(points):
            dic[line_nmbr + k + 1] = dic[line_nmbr + k + 1] + dic[line_nmbr]
    return sum(dic.values())


if __name__ == "__main__":
    print(part1())
    print(part2())
