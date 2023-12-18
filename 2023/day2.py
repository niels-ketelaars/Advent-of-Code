cubes = {"red": 12, "green": 13, "blue": 14}


def part1():
    with open("inputs/day2inp.txt", "r") as file:
        data = file.read().splitlines()
    sum = 0
    for game, line in enumerate(data):
        game_result = ", ".join(line.split(": ")[1].split("; ")).split(", ")
        for draws in game_result:
            draw = draws.split(" ")
            if int(draw[0]) > cubes[draw[1]]:
                break
        else:
            sum += game + 1
    return sum


def part2():
    with open("inputs/day2inp.txt", "r") as file:
        data = file.read().splitlines()
    sum = 0
    for line in data:
        game_result = ", ".join(line.split(": ")[1].split("; ")).split(", ")
        dct = {"red": 0, "green": 0, "blue": 0}
        for draws in game_result:
            draw = draws.split(" ")
            print(draw)
            if dct[draw[1]] < int(draw[0]):
                dct[draw[1]] = int(draw[0])
        power = dct["red"] * dct["blue"] * dct["green"]
        sum += power
    return sum


if __name__ == "__main__":
    print(part1())
    print(part2())
