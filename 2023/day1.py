def find_calibration(line):
    calibration_value = ""
    for char in line:
        if char.isnumeric():
            calibration_value = char
            break
    for char in line[::-1]:
        if char.isnumeric():
            calibration_value += char
            break
    return int(calibration_value)


def part1():
    with open("inputs/day1inp.txt", "r") as file:
        data = file.read().splitlines()
    sum = 0
    for line in data:
        sum += find_calibration(line)
    return sum


def part2():
    nums = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    with open("inputs/day1inp.txt", "r") as file:
        data = file.read().splitlines()
    sum = 0
    for line in data:
        for idx, num in enumerate(nums):
            line = line.replace(num, num + f"{idx+1}" + num)
        sum += find_calibration(line)
    return sum


if __name__ == "__main__":
    print(part1())
    print(part2())
