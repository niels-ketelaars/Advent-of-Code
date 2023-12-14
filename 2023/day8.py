from math import lcm


def part1():
    with open("inputs/day8inp.txt", "r") as file:
        data = file.read().splitlines()
    instructions = data[0]
    dct = {}
    for line in data[2:]:
        splitted = line.split(" = ")
        first = splitted[0]
        second = splitted[1].replace("(", "").replace(")", "").split(", ")
        dct[first] = second
    start = "AAA"
    index = 0
    while True:
        for chr in instructions:
            index += 1
            if chr == "L":
                out = dct[start][0]
            else:
                out = dct[start][1]

            if out == "ZZZ":
                return index
            else:
                start = out


def part2():
    with open("inputs/day8inp.txt", "r") as file:
        data = file.read().splitlines()
    instructions = data[0]
    dct = {}
    for line in data[2:]:
        splitted = line.split(" = ")
        first = splitted[0]
        second = splitted[1].replace("(", "").replace(")", "").split(", ")
        dct[first] = second
    starting_nodes = [start for start in dct if start.endswith("A")]
    indices = []
    for start in starting_nodes:
        index = 0
        while True:
            for chr in instructions:
                index += 1
                if chr == "L":
                    out = dct[start][0]
                else:
                    out = dct[start][1]

                if out.endswith("Z"):
                    break
                else:
                    start = out
            else:
                continue
            break
        indices.append(index)
    return indices


if __name__ == "__main__":
    print(part1())
    print(lcm(*part2()))
