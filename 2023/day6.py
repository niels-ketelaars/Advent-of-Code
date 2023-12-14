import numpy as np


def part1():
    with open("inputs/day6inp.txt", "r") as file:
        data = file.read().splitlines()
    times, dist = data[0].split()[1:], data[1].split()[1:]
    prod = 1
    for k in range(4):
        T = int(times[k])
        D = int(dist[k])
        t1 = np.floor(1 + 0.5 * (T - np.sqrt(T**2 - 4 * D)))
        t2 = np.ceil(-1 + 0.5 * (T + np.sqrt(T**2 - 4 * D)))
        prod *= t2 - t1 + 1
    return prod


def part2():
    with open("inputs/day6inp.txt", "r") as file:
        data = file.read().splitlines()
    times, dist = data[0].split()[1:], data[1].split()[1:]

    T = int(times[0] + times[1] + times[2] + times[3])
    D = int(dist[0] + dist[1] + dist[2] + dist[3])
    t1 = np.floor(1 + 0.5 * (T - np.sqrt(T**2 - 4 * D)))
    t2 = np.ceil(-1 + 0.5 * (T + np.sqrt(T**2 - 4 * D)))
    return t2 - t1 + 1


if __name__ == "__main__":
    print(part1())
    print(part2())
