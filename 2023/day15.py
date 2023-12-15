import numpy as np


def hash(input):
    total = 0
    for chr in input:
        total = (17 * (total + ord(chr))) % 256
    return total


def part1():
    with open("inputs/day15inp.txt", "r") as file:
        data = file.read().split(",")
    sum = 0
    for group in data:
        sum += hash(group)
    return sum


def part2():
    with open("inputs/day15inp.txt", "r") as file:
        data = file.read().split(",")
    boxes = {k: {} for k in range(256)}
    for group in data:
        if "-" in group:
            label = group[:-1]
            if label in boxes[hash(label)]:
                del boxes[hash(label)][label]
        elif "=" in group:
            label, focal_len = group.split("=")
            boxes[hash(label)][label] = focal_len
    total = 0
    for box_nmbr, box in boxes.items():
        for lens_nmbr, focal_len in enumerate(box.values()):
            total += (box_nmbr + 1) * (lens_nmbr + 1) * int(focal_len)
    return total


if __name__ == "__main__":
    print(part1())
    print(part2())
