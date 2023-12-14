import numpy as np


def f(data):
    data = [list(line) for line in data]
    length = len(data)
    for line_nmbr in range(length - 1, 0, -1):
        for lines_below in range(line_nmbr, length):
            for chr_nmbr in range(len(data[lines_below])):
                chr = data[lines_below][chr_nmbr]
                if chr == "O" and data[lines_below - 1][chr_nmbr] == ".":
                    data[lines_below][chr_nmbr] = "."
                    data[lines_below - 1][chr_nmbr] = "O"
    return data


def part1():
    with open("inputs/day14inp.txt", "r") as file:
        data = file.read().splitlines()
    data = f(data)
    length = len(data)
    total = 0
    for line_nmbr in range(length):
        line = data[line_nmbr]
        total += (length - line_nmbr) * line.count("O")
    return total


def part2():
    with open("inputs/day14inp.txt", "r") as file:
        data = file.read().splitlines()
    length = len(data)
    last = [data]
    for i in range(1000000000):
        first_pass = np.rot90(f(data), k=-1)
        second_pass = np.rot90(f(first_pass), k=-1)
        third_pass = np.rot90(f(second_pass), k=-1)
        fourth_pass = np.rot90(f(third_pass), k=-1)
        data = [list(m) for m in fourth_pass]
        if data in last:
            eq = [(1 if np.array_equal(l, data) else 0) for l in last]
            idx = np.nonzero(eq)[0][0]
            offset = (1000000000 - idx) % (i + 1 - idx)
            final = last[idx + offset]
            break
        last.append(data)
    print(final)
    total = 0
    for line_nmbr in range(length):
        line = final[line_nmbr]
        total += (length - line_nmbr) * line.count("O")
    return total


if __name__ == "__main__":
    print(part1())
    print(part2())
