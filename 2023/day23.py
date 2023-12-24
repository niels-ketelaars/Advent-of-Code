import sys

sys.setrecursionlimit(10**8)


def dfs(data, loc, seen):
    lenght = len(data)
    r, c = loc
    match data[r][c]:
        case ">":
            new_locs = [(r, c + 1)]
        case "<":
            new_locs = [(r, c - 1)]
        case "v":
            new_locs = [(r + 1, c)]
        case "^":
            new_locs = [(r - 1, c)]
        case _:
            new_locs = [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]
    step_possibilities = []
    for new_loc in new_locs:
        r_new, c_new = new_loc
        if data[r_new][c_new] == "#":
            continue
        elif new_loc in seen:
            continue
        elif r_new == lenght - 1:
            return 1
        new_seen = seen.copy()
        new_seen.add(new_loc)
        step_possibilities.append(dfs(data, new_loc, new_seen))

    return -float("inf") if step_possibilities == [] else max(step_possibilities) + 1


def part1():
    with open("inputs/day23inp.txt", "r") as file:
        data = file.read().splitlines()
    return dfs(data, (1, 1), {(0, 1)}) + 1


def part2():
    with open("inputs/day23inp.txt", "r") as file:
        data = file.read().splitlines()
    pass


if __name__ == "__main__":
    # print(part1())
    print(part2())
