from scipy.special import binom
import numpy as np


def find_poly(outs, x):
    fin_diffs = [outs]
    prev_fin_diffs = outs
    while True:
        n_th_fin_diff = [
            prev_fin_diffs[k + 1] - prev_fin_diffs[k]
            for k in range(len(prev_fin_diffs) - 1)
        ]
        if not np.any(n_th_fin_diff):
            break
        prev_fin_diffs = n_th_fin_diff
        fin_diffs.append(n_th_fin_diff)
    b = lambda k: (binom(x, k) if x != -1 else binom(k, k) * (-1) ** k)
    fin_dif_eval = sum([diff[0] * b(k) for k, diff in enumerate(fin_diffs)])
    return fin_dif_eval


def part1():
    with open("inputs/day9inp.txt", "r") as file:
        data = file.read().splitlines()
    sum = 0
    for line in data:
        outs = line.split()
        outs = [int(out) for out in outs]
        length = len(outs)
        sum += find_poly(outs, length)
    return sum


def part2():
    with open("inputs/day9inp.txt", "r") as file:
        data = file.read().splitlines()
    sum = 0
    for line in data:
        outs = line.split()
        outs = [int(out) for out in outs]
        length = len(outs)
        sum += find_poly(outs, -1)
    return sum


if __name__ == "__main__":
    print(part1())
    print(part2())
