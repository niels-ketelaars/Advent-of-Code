import heapq


def dijkstra(part_two):
    with open("inputs/day17inp.txt", "r") as file:
        data = file.read().splitlines()
    length = len(data)
    width = len(data[0])
    queue = [(0, 0, 0, "", 0)]
    dct = {}
    while queue != []:
        loss, r, c, direction, travel_time = heapq.heappop(queue)
        if (r, c, direction, travel_time) in dct:
            continue
        if (r, c) == (length - 1, width - 1):
            return loss
        dct[(r, c, direction, travel_time)] = loss
        for new_direction, dr, dc in [
            ("left", 0, -1),
            ("right", 0, 1),
            ("up", -1, 0),
            ("down", 1, 0),
        ]:
            new_travel_time = 1 if new_direction != direction else travel_time + 1

            check = {direction, new_direction}
            condition1 = new_travel_time > 3
            condition2 = new_travel_time > 10 or (
                travel_time < 4 and new_direction != direction and direction != ""
            )

            if (
                check == {"left", "right"}
                or check == {"up", "down"}
                or condition1 * (not part_two)
                or condition2 * part_two
            ):
                continue

            if 0 <= r + dr < length and 0 <= c + dc < width:
                cost = int(data[r + dr][c + dc])
                heapq.heappush(
                    queue, (loss + cost, r + dr, c + dc, new_direction, new_travel_time)
                )


def part1():
    return dijkstra(False)


def part2():
    return dijkstra(True)


if __name__ == "__main__":
    print(part1())
    print(part2())
