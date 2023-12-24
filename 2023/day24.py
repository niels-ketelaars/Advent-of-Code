from numpy.linalg import solve, LinAlgError
from sympy import Symbol, nonlinsolve


def parse(data):
    hailstones = []
    for line in data:
        line = line.split(" @ ")
        hailstone = [eval(line[0]), eval(line[1])]
        hailstones.append(hailstone)
    return hailstones


def part1():
    with open("inputs/day24inp.txt", "r") as file:
        data = file.read().splitlines()
    hailstones = parse(data)
    total = 0
    for idx, stone1 in enumerate(hailstones):
        for stone2 in hailstones[idx + 1 :]:
            (px1, py1, _), (vx1, vy1, _) = stone1
            (px2, py2, _), (vx2, vy2, _) = stone2

            A = [[vx1, -vx2], [vy1, -vy2]]
            b = [[px2 - px1], [py2 - py1]]
            try:
                x = solve(A, b)
                if x[0][0] < 0 or x[1][0] < 0:
                    continue
                loc = (px1 + x[0][0] * vx1, py1 + x[0][0] * vy1)
                if (
                    200000000000000 <= loc[0] <= 400000000000000
                    and 200000000000000 <= loc[1] <= 400000000000000
                ):
                    total += 1
            except LinAlgError:
                pass
    return total


def part2():
    with open("inputs/day24inp.txt", "r") as file:
        data = file.read().splitlines()
    hailstones = parse(data)
    (px1, py1, pz1), (vx1, vy1, vz1) = hailstones[0]
    (px2, py2, pz2), (vx2, vy2, vz2) = hailstones[1]
    (px3, py3, pz3), (vx3, vy3, vz3) = hailstones[2]

    rx = Symbol("rx")
    ry = Symbol("ry")
    rz = Symbol("rz")
    qx = Symbol("qx")
    qy = Symbol("qy")
    qz = Symbol("qz")
    t1 = Symbol("t1")
    t2 = Symbol("t2")
    t3 = Symbol("t3")
    unknowns = rx, ry, rz, qx, qy, qz, t1, t2, t3

    eqx1 = rx - px1 + t1 * (qx - vx1)
    eqy1 = ry - py1 + t1 * (qy - vy1)
    eqz1 = rz - pz1 + t1 * (qz - vz1)
    eqx2 = rx - px2 + t2 * (qx - vx2)
    eqy2 = ry - py2 + t2 * (qy - vy2)
    eqz2 = rz - pz2 + t2 * (qz - vz2)
    eqx3 = rx - px3 + t3 * (qx - vx3)
    eqy3 = ry - py3 + t3 * (qy - vy3)
    eqz3 = rz - pz3 + t3 * (qz - vz3)
    eqs = eqx1, eqy1, eqz1, eqx2, eqy2, eqz2, eqx3, eqy3, eqz3

    (ans,) = nonlinsolve(eqs, unknowns)
    return ans[0] + ans[1] + ans[2]


if __name__ == "__main__":
    print(part1())
    print(part2())
