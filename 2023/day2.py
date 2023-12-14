cubes = {"red": 12, "green": 13, "blue": 14}


def part1():
    with open("inputs/day2inp.txt", "r") as file:
        sum = 0
        for game, line in enumerate(file):
            line = line.replace("\n", "")
            game_result = line.split(": ")[1].split("; ")
            for draws in game_result:
                dict = {"red": 0, "green": 0, "blue": 0}
                draws = draws.split(", ")
                for draw in draws:
                    draw = draw.split(" ")
                    dict[draw[1]] = int(draw[0])
                if not (
                    (dict["red"] <= cubes["red"])
                    and (dict["green"] <= cubes["green"])
                    and (dict["blue"] <= cubes["blue"])
                ):
                    break
            else:
                print(line + " is possible")
                sum += game + 1
    return sum


def part2():
    with open("inputs/day2inp.txt", "r") as file:
        sum = 0
        for line in file:
            line = line.replace("\n", "")
            game_result = line.split(": ")[1].split("; ")
            max_red = 0
            max_blue = 0
            max_green = 0
            for draws in game_result:
                dict = {"red": 0, "green": 0, "blue": 0}
                draws = draws.split(", ")
                for draw in draws:
                    draw = draw.split(" ")
                    dict[draw[1]] = int(draw[0])
                if max_red < dict["red"]:
                    max_red = dict["red"]
                if max_blue < dict["blue"]:
                    max_blue = dict["blue"]
                if max_green < dict["green"]:
                    max_green = dict["green"]
            power = max_red * max_blue * max_green
            sum += power
    return sum


if __name__ == "__main__":
    print(part2())
