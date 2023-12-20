import numpy as np


def solve(data, part_two):
    sum = 0
    length = len(data)
    uber_dict = {}
    for line_nmbr, line in enumerate(data):
        was_prev_numeric = False
        start = 0
        number_locations = []
        for idx, char in enumerate(line):
            if char.isnumeric():
                if not was_prev_numeric:
                    start = idx
                    was_prev_numeric = True
            else:
                if was_prev_numeric:
                    number_locations.append((start, idx - 1))
                    was_prev_numeric = False
        if was_prev_numeric:
            number_locations.append((start, length - 1))
        if line_nmbr == 0:
            pad_up = 0
        else:
            pad_up = 1
        if line_nmbr == length - 1:
            pad_down = 0
        else:
            pad_down = 1
        for x, y in number_locations:
            if x == 0:
                pad_left = 0
            else:
                pad_left = 1
            if y == length - 1:
                pad_right = 0
            else:
                pad_right = 1
            for i in range(x - pad_left, y + pad_right + 1):
                for j in range(line_nmbr - pad_up, line_nmbr + pad_down + 1):
                    lne = data[j]
                    chr = lne[i]
                    if not (part_two or chr.isnumeric() or (chr == ".")):
                        num = int(line[x : y + 1])
                        sum += num
                        break
                    if chr == "*" and part_two:
                        num = int(line[x : y + 1])
                        if (j, i) in uber_dict:
                            uber_dict[(j, i)].append(int(num))
                        else:
                            uber_dict[(j, i)] = [int(num)]
                else:
                    continue
                break
    return sum if not part_two else uber_dict


def part1():
    with open("inputs/day3inp.txt", "r") as file:
        data = file.read().splitlines()
    return solve(data, False)


def part2():
    with open("inputs/day3inp.txt", "r") as file:
        data = file.read().splitlines()
    uber_dict = solve(data, True)
    sum = 0
    for nums in uber_dict.values():
        if len(nums) == 2:
            sum += np.prod(nums)
    return sum


if __name__ == "__main__":
    print(part1())
    print(part2())
