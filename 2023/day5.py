from tqdm import tqdm


def mapping(map, inp: int):
    for line in map:
        splits = line.split(" ")
        if inp >= int(splits[1]) and inp < int(splits[1]) + int(splits[2]):
            return int(splits[0]) + inp - int(splits[1])
    return inp


def rev_map(map, outp: int):
    for line in map:
        splits = line.split(" ")
        if outp in range(int(splits[0]), int(splits[2]) + int(splits[0])):
            return int(splits[1]) - int(splits[0]) + outp
    return outp


def part1():
    with open("inputs/day5inp.txt", "r") as file:
        data = file.read().split("\n\n")
    loc = float("inf")
    seeds = data[0].split(" ")[1:]
    seed_soil = data[1].splitlines()[1:]
    soil_fert = data[2].splitlines()[1:]
    fert_water = data[3].splitlines()[1:]
    water_light = data[4].splitlines()[1:]
    light_temp = data[5].splitlines()[1:]
    temp_hum = data[6].splitlines()[1:]
    hum_loc = data[7].splitlines()[1:]
    for k in tqdm(range(0, len(seeds), 2)):
        seed = int(seeds[k])
        rng = int(seeds[k + 1])
        for sd in tqdm(range(seed, seed + rng)):
            soil = mapping(seed_soil, sd)
            fert = mapping(soil_fert, soil)
            water = mapping(fert_water, fert)
            light = mapping(water_light, water)
            temp = mapping(light_temp, light)
            hum = mapping(temp_hum, temp)
            location = mapping(hum_loc, hum)
            loc = location if location < loc else loc
    return min(loc)


# takes 2+ hours to run...
def part2():
    with open("inputs/day5inp.txt", "r") as file:
        data = file.read().split("\n\n")
    seeds = data[0].split(" ")[1:]
    seed_soil = data[1].splitlines()[1:]
    soil_fert = data[2].splitlines()[1:]
    fert_water = data[3].splitlines()[1:]
    water_light = data[4].splitlines()[1:]
    light_temp = data[5].splitlines()[1:]
    temp_hum = data[6].splitlines()[1:]
    hum_loc = data[7].splitlines()[1:]
    for loc in tqdm(range(0, 340994526)):
        hum = rev_map(hum_loc, loc)
        temp = rev_map(temp_hum, hum)
        light = rev_map(light_temp, temp)
        water = rev_map(water_light, light)
        fert = rev_map(fert_water, water)
        soil = rev_map(soil_fert, fert)
        seed = rev_map(seed_soil, soil)
        for k in range(0, len(seeds), 2):
            if seed in range(int(seeds[k]), int(seeds[k]) + int(seeds[k + 1])):
                return loc


if __name__ == "__main__":
    print(part1())
    print(part2())
