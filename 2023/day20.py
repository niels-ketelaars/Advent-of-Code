from dataclasses import dataclass
import numpy as np
from math import lcm


@dataclass
class BasicGate:
    name: str
    outputs: list[str]


@dataclass
class FlipFlop(BasicGate):
    on: bool


@dataclass
class Conjuction(BasicGate):
    inputs: dict[str, bool]


def parse(data):
    dct = {"rx": BasicGate("rx", [])}
    for line in data:
        inp, outs = line.split(" -> ")
        outs = outs.split(", ")
        if inp[0] == "%":
            name = inp[1:]
            dct[name] = FlipFlop(name, outs, False)
        elif inp[0] == "&":
            name = inp[1:]
            dct[name] = Conjuction(name, outs, {})
        else:
            name = inp
            dct[name] = BasicGate(name, outs)

    for key, gate in dct.items():
        for out in gate.outputs:
            if isinstance(dct[out], Conjuction):
                dct[out].inputs[key] = False

    return dct


def pulse(inp, outp, type, dct, queue):
    # print(f"{inp} -{'high' if type else 'low'}-> {outp}")
    if isinstance(dct[outp], FlipFlop):
        if not type:
            for o in dct[outp].outputs:
                queue.append((outp, o, False if dct[outp].on else True))
            dct[outp].on = not dct[outp].on
    elif isinstance(dct[outp], Conjuction):
        dct[outp].inputs[inp] = type
        sends = not np.all(list(dct[outp].inputs.values()))
        for o in dct[outp].outputs:
            queue.append((outp, o, sends))
    else:
        for o in dct[outp].outputs:
            queue.append((outp, o, type))


def part1():
    with open("inputs/day20inp.txt", "r") as file:
        data = file.read().splitlines()
    dct = parse(data)

    total_high, total_low = 0, 0
    for _ in range(1000):
        queue = [("button", "broadcaster", False)]
        while queue != []:
            node = queue.pop(0)
            if node[2]:
                total_high += 1
            else:
                total_low += 1
            pulse(*node, dct, queue)
    return total_low * total_high


def part2():
    with open("inputs/day20inp.txt", "r") as file:
        data = file.read().splitlines()
    dct = parse(data)

    index = 0
    loops = {}
    while True:
        queue = [("button", "broadcaster", False)]
        index += 1
        while queue != []:
            node = queue.pop(0)
            if node[0] in ["kk", "xc", "sk", "vt"] and node[2] and node[0] not in loops:
                loops[node[0]] = index
            pulse(*node, dct, queue)
        if len(loops) == 4:
            return lcm(*loops.values())


if __name__ == "__main__":
    print(part1())
    print(part2())
