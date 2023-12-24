def possibilities(data, r, c, moves_left):
    length = len(data)
    start = (r, c, moves_left)  # (5, 5, 6)
    queue = [start]
    final = set()
    seen = {(r, c)}
    while queue != []:
        r, c, moves_left = queue.pop(0)
        if moves_left % 2 == 0:
            final.add((r, c))
        if moves_left == 0:
            continue
        for dr, dc in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            if (
                0 <= r + dr < length
                and 0 <= c + dc < length
                and not (r + dr, c + dc) in seen
                and data[r + dr][c + dc] != "#"
            ):
                queue.append((r + dr, c + dc, moves_left - 1))
                seen.add((r + dr, c + dc))
    return len(final)


def part1():
    with open("inputs/day21inp.txt", "r") as file:
        data = file.read().splitlines()
    return possibilities(data, 65, 65, 64)


def part2():
    with open("inputs/day21inp.txt", "r") as file:
        data = file.read().splitlines()
    big_data = [line * 5 for line in data] * 5
    w = len(data)
    r = 65 + w * 2

    # if f(x) denotes number of possibilities after 65+131*x steps, then f is quadratic
    f1 = possibilities(big_data, r, r, 65)
    f2 = possibilities(big_data, r, r, 65 + w)
    f3 = possibilities(big_data, r, r, 65 + w * 2)

    x = (26501365 - 65) // w
    return int(
        0.5 * (f1 - 2 * f2 + f3) * x**2 + 0.5 * (-3 * f1 + 4 * f2 - f3) * x + f1
    )


if __name__ == "__main__":
    print(part1())
    print(part2())
