import numpy as np


def part1():
    with open("inputs/day11inp.txt", "r") as file:
        data = file.read().splitlines()
    galaxies = []
    empty_rows = []
    empty_cols = []
    for line_nmbr, line in enumerate(data):
        if line.replace(".", "") == "":
            empty_rows.append(line_nmbr)
            continue
        for idx, chr in enumerate(line):
            if chr == "#":
                galaxies.append((line_nmbr, idx))
    for i in range(140):
        col = "".join([data[k][i] for k in range(140)])
        if col.replace(".", "") == "":
            empty_cols.append(i)
    sum = 0
    for n, gal1 in enumerate(galaxies):
        for gal2 in galaxies[:n]:
            r1, c1 = gal1
            r2, c2 = gal2
            inbetween_rows = len(
                [1 for row in empty_rows if row in range(min(r1, r2), max(r1, r2))]
            )
            inbetween_cols = len(
                [1 for col in empty_cols if col in range(min(c1, c2), max(c1, c2))]
            )

            dist = np.abs(r1 - r2) + np.abs(c1 - c2) + inbetween_cols + inbetween_rows
            sum += dist
    return sum


def part2():
    with open("inputs/day11inp.txt", "r") as file:
        data = file.read().splitlines()
    galaxies = []
    empty_rows = []
    empty_cols = []
    for line_nmbr, line in enumerate(data):
        if line.replace(".", "") == "":
            empty_rows.append(line_nmbr)
            continue
        for idx, chr in enumerate(line):
            if chr == "#":
                galaxies.append((line_nmbr, idx))
    for i in range(140):
        col = "".join([data[k][i] for k in range(140)])
        if col.replace(".", "") == "":
            empty_cols.append(i)
    sum = 0
    for n, gal1 in enumerate(galaxies):
        for gal2 in galaxies[:n]:
            r1, c1 = gal1
            r2, c2 = gal2
            inbetween_rows = len(
                [1 for row in empty_rows if row in range(min(r1, r2), max(r1, r2))]
            )
            inbetween_cols = len(
                [1 for col in empty_cols if col in range(min(c1, c2), max(c1, c2))]
            )

            dist = int(
                np.abs(r1 - r2)
                + np.abs(c1 - c2)
                + inbetween_cols * 999999
                + inbetween_rows * 999999
            )
            sum += dist
    return sum


if __name__ == "__main__":
    print(part1())
    print(part2())
