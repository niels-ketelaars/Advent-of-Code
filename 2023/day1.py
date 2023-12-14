def part1():
    with open("inputs/day1inp.txt", "r") as file:
        sum: int = 0
        for line in file:
            calibration_value: str = ""
            for char in line:
                if char.isnumeric():
                    calibration_value = char
                    break
            for char in line[::-1]:
                if char.isnumeric():
                    calibration_value += char
                    break
            sum += int(calibration_value)
    return sum


def part2():
    nums = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    nums_rev = ["eno", "owt", "eerht", "ruof", "evif", "xis", "neves", "thgie", "enin"]
    with open("inputs/day1inp.txt", "r") as file:
        sum: int = 0
        for line in file:
            calibration_value: str = ""
            for idx, char in enumerate(line):
                if char.isnumeric():
                    calibration_value = char
                    break
                for i, num in enumerate(nums):
                    if line[idx::].startswith(num):
                        calibration_value = str(i + 1)
                        break
                else:
                    continue
                break
            line_rev = line[::-1]
            for idx, char in enumerate(line_rev):
                if char.isnumeric():
                    calibration_value += char
                    break
                for i, num in enumerate(nums_rev):
                    if line_rev[idx::].startswith(num):
                        calibration_value += str(i + 1)
                        break
                else:
                    continue
                break
            sum += int(calibration_value)
    return sum


if __name__ == "__main__":
    print(part1())
    print(part2())
