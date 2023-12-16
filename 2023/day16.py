def next_tile(data, queue, visited):
    r, c, entrypoint = queue.pop(0)
    if r < 0 or c < 0 or r >= len(data) or c >= len(data[0]):
        return 0
    if (r, c, entrypoint) in visited:
        return 0
    tile = data[r][c]
    if entrypoint == "left":
        if tile == "." or tile == "-":
            queue.append((r, c + 1, "left"))
        elif tile == "|":
            queue.append((r - 1, c, "down"))
            queue.append((r + 1, c, "up"))
        elif tile == "\\":
            queue.append((r + 1, c, "up"))
        elif tile == "/":
            queue.append((r - 1, c, "down"))
    elif entrypoint == "right":
        if tile == "." or tile == "-":
            queue.append((r, c - 1, "right"))
        elif tile == "|":
            queue.append((r - 1, c, "down"))
            queue.append((r + 1, c, "up"))
        elif tile == "\\":
            queue.append((r - 1, c, "down"))
        elif tile == "/":
            queue.append((r + 1, c, "up"))
    elif entrypoint == "up":
        if tile == "." or tile == "|":
            queue.append((r + 1, c, "up"))
        elif tile == "-":
            queue.append((r, c + 1, "left"))
            queue.append((r, c - 1, "right"))
        elif tile == "\\":
            queue.append((r, c + 1, "left"))
        elif tile == "/":
            queue.append((r, c - 1, "right"))
    elif entrypoint == "down":
        if tile == "." or tile == "|":
            queue.append((r - 1, c, "down"))
        elif tile == "-":
            queue.append((r, c + 1, "left"))
            queue.append((r, c - 1, "right"))
        elif tile == "\\":
            queue.append((r, c - 1, "right"))
        elif tile == "/":
            queue.append((r, c + 1, "left"))
    visited.append((r, c, entrypoint))
    return 1


def part1():
    with open("inputs/day16inp.txt", "r") as file:
        data = file.read().splitlines()
    visited = []
    queue = [(0, 0, "left")]
    while queue != []:
        next_tile(data, queue, visited)
    return len({(r, c) for (r, c, entrypoint) in visited})


# takes ~2 mins to run
def part2():
    with open("inputs/day16inp.txt", "r") as file:
        data = file.read().splitlines()
    length = len(data)
    width = len(data[0])
    starting_tiles = (
        [(0, c, "up") for c in range(width)]
        + [(length - 1, c, "down") for c in range(width)]
        + [(r, 0, "left") for r in range(length)]
        + [(r, width - 1, "right") for r in range(length)]
    )
    possibilities = []
    for start in starting_tiles:
        visited = []
        queue = [start]
        while queue != []:
            next_tile(data, queue, visited)
        possibilities.append(len({(r, c) for (r, c, entrypoint) in visited}))
    return max(possibilities)


if __name__ == "__main__":
    print(part1())
    print(part2())
