def main(filename):
    blocked = set()
    floor = 0
    with open(filename) as input_file:
        for line in input_file:
            line = line.strip()
            edges = [list(map(int, edge.split(","))) for edge in line.split(" -> ")]
            floor = max(floor, max(y + 2 for _, y in edges))
            for (x1, y1), (x2, y2) in zip(edges, edges[1:]):
                if x1 == x2:
                    for y in range(min(y1, y2), max(y1, y2) + 1):
                        blocked.add((x1, y))
                else:
                    for x in range(min(x1, x2), max(x1, x2) + 1):
                        blocked.add((x, y1))

    result_part_1 = 0
    blocked_1 = set(blocked)
    while True:
        x, y = 500, 0
        will_fall_forever = False
        while not will_fall_forever:
            for candidate in [(x, y + 1), (x - 1, y + 1), (x + 1, y + 1)]:
                if candidate not in blocked_1:
                    x, y = candidate
                    if y > 500:
                        will_fall_forever = True
                    break
            else:
                blocked_1.add((x, y))
                break
        if will_fall_forever:
            break
        result_part_1 += 1

    result_part_2 = 0
    blocked_2 = set(blocked)
    while True:
        result_part_2 += 1
        x, y = 500, 0
        while True:
            for candidate in [(x, y + 1), (x - 1, y + 1), (x + 1, y + 1)]:
                if candidate not in blocked_2 and candidate[1] < floor:
                    x, y = candidate
                    break
            else:
                blocked_2.add((x, y))
                break
        if y == 0:
            break

    print(f"part 1: {result_part_1}")
    print(f"part 2: {result_part_2}")


if __name__ == "__main__":
    for name in [
        "sample.txt",
        "input.txt"
    ]:
        print(f"-- {name} --")
        main(name)
