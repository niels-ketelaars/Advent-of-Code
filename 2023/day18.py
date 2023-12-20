def solve(data, part_two):
    coord = (0, 0)
    coords = [coord]
    total = 0
    for line in data:
        if part_two:
            directions = [0, 2, 3, 1]
            color = line.split()[-1]
            dist = int(color[2:-2], 16)
            direction = int(color[-2])
        else:
            directions = ["R", "L", "U", "D"]
            direction, dist, _ = line.split()
        r, c = coord
        if direction == directions[0]:
            coord = r, c + int(dist)
        elif direction == directions[1]:
            coord = r, c - int(dist)
        elif direction == directions[2]:
            coord = r - int(dist), c
        elif direction == directions[3]:
            coord = r + int(dist), c
        coords.append(coord)
        total += int(dist)
    area = 0.5 * sum(
        [
            coords[k][0] * coords[k - 1][1] - coords[k][1] * coords[k - 1][0]
            for k in range(len(coords))
        ]
    )  # shoelace formula for area of a polygon
    return int(area) + total // 2 + 1  # Pick's theorem


def part1():
    with open("inputs/day18inp.txt", "r") as file:
        data = file.read().splitlines()
    return solve(data, False)


def part2():
    with open("inputs/day18inp.txt", "r") as file:
        data = file.read().splitlines()
    return solve(data, True)


if __name__ == "__main__":
    print(part1())
    print(part2())
