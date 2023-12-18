def next_pipe(data, r, c, entrypoint):
    current_pipe = data[r][c]
    if current_pipe == "S":
        return -1
    elif current_pipe == "|":
        if entrypoint == "down":
            return r - 1, c, "down"
        elif entrypoint == "up":
            return r + 1, c, "up"
    elif current_pipe == "-":
        if entrypoint == "left":
            return r, c + 1, "left"
        elif entrypoint == "right":
            return r, c - 1, "right"
    elif current_pipe == "L":
        if entrypoint == "up":
            return r, c + 1, "left"
        elif entrypoint == "right":
            return r - 1, c, "down"
    elif current_pipe == "J":
        if entrypoint == "up":
            return r, c - 1, "right"
        elif entrypoint == "left":
            return r - 1, c, "down"
    elif current_pipe == "7":
        if entrypoint == "down":
            return r, c - 1, "right"
        elif entrypoint == "left":
            return r + 1, c, "up"
    elif current_pipe == "F":
        if entrypoint == "down":
            return r, c + 1, "left"
        elif entrypoint == "right":
            return r + 1, c, "up"
    else:
        raise Exception


def part1():
    with open("inputs/day10inp.txt", "r") as file:
        data = file.read().splitlines()
    index = 0
    current_pipe = (106, 110, "down")  # starting S
    while current_pipe != -1:
        r, c, entry = current_pipe
        current_pipe = next_pipe(data, r, c, entry)
        index += 1
    return index // 2


def part2():
    with open("inputs/day10inp.txt", "r") as file:
        data = file.read().splitlines()
    index = 0
    current_pipe = (106, 110, "down")
    lst = []
    while current_pipe != -1:
        r, c, entry = current_pipe
        lst.append((r, c))
        current_pipe = next_pipe(data, r, c, entry)
        index += 1
    area = 0.5 * sum(
        [lst[k][0] * lst[k - 1][1] - lst[k][1] * lst[k - 1][0] for k in range(len(lst))]
    )  # shoelace formula for area of a polygon
    return int(area) - index // 2 + 1  # Pick's theorem


if __name__ == "__main__":
    print(part1())
    print(part2())
