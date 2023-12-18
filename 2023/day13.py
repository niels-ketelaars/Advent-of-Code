from itertools import product

old_lines = {}


def check_mirror(group, lines, part_two):
    total = 0
    need_to_break = False
    for l in range(0, len(lines) - 1):
        lines_to_check = min(l + 1, len(lines) - l - 1)
        for k in range(lines_to_check):
            if lines[l - k] == lines[l + k + 1]:
                continue
            else:
                break
        else:
            if not part_two:
                old_lines[group] = ("line", l + 1)
            elif old_lines[group] == ("line", l + 1):
                continue
            total = 100 * (l + 1)
            need_to_break = True
            break

    else:
        transpose = [[line[n] for line in lines] for n in range(len(lines[0]))]

        for c in range(0, len(transpose) - 1):
            cols_to_check = min(c + 1, len(transpose) - c - 1)
            for k in range(cols_to_check):
                if transpose[c - k] == transpose[c + k + 1]:
                    continue
                else:
                    break
            else:
                if not part_two:
                    old_lines[group] = ("col", c + 1)
                elif old_lines[group] == ("col", c + 1):
                    continue
                total = c + 1
                need_to_break = True
                break
    return total, need_to_break


def part1():
    with open("inputs/day13inp.txt", "r") as file:
        data = file.read().split("\n\n")
    total = 0
    for group in data:
        lines = group.splitlines()
        total += check_mirror(group, lines, False)[0]
    return total


def part2():
    with open("inputs/day13inp.txt", "r") as file:
        data = file.read().split("\n\n")
    total = 0
    for group in data:
        lines = group.splitlines()
        lines = [list(line) for line in lines]
        length = len(lines)
        width = len(lines[0])
        need_to_break = False
        for n, m in product(range(length), range(width)):
            if need_to_break:
                break
            lines = group.splitlines()
            lines = [list(line) for line in lines]
            if lines[n][m] == "#":
                lines[n][m] = "."
            else:
                lines[n][m] = "#"
            result, need_to_break = check_mirror(group, lines, True)
            total += result
    return total


if __name__ == "__main__":
    print(part1())
    print(part2())
