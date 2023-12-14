from functools import cache


@cache
def possibilities(springs, groups):
    if not groups:
        if all(spring in [".", "?"] for spring in springs):
            return 1
        else:
            return 0
    size_first_group = groups[0]
    remaining_groups = groups[1:]
    remaining_spring_spaces = sum(remaining_groups) + len(remaining_groups)
    count = 0
    for i in range(len(springs) - remaining_spring_spaces - size_first_group + 1):
        possible_springs = "." * i + "#" * size_first_group + "."
        if all(
            spring == possible_spring or spring == "?"
            for spring, possible_spring in zip(springs, possible_springs)
        ):
            count += possibilities(springs[len(possible_springs) :], remaining_groups)
    return count


def part1():
    with open("inputs/day12inp.txt", "r") as file:
        data = file.read().splitlines()
    sum = 0
    for line in data:
        row = line.split()
        springs, groups = row
        groups = tuple(map(int, groups.split(",")))
        sum += possibilities(springs, groups)
    return sum


def part2():
    with open("inputs/day12inp.txt", "r") as file:
        data = file.read().splitlines()
    sum = 0
    for line in data:
        row = line.split()
        springs, groups = row
        springs = "?".join((springs,) * 5)
        groups = tuple(map(int, groups.split(","))) * 5
        sum += possibilities(springs, groups)
    return sum


if __name__ == "__main__":
    print(part1())
    print(part2())
