def main(filename):
    sensors = []
    with open(filename) as input_file:
        for line in input_file:
            sensor, beacon = line.strip().replace("Sensor at ", "").split(": closest beacon is at ")
            sensors.append(tuple(tuple(int(t[2:]) for t in data.split(", ")) for data in [sensor, beacon]))

    # part 1
    if filename == "sample.txt":
        row_y = 10
    else:
        row_y = 2_000_000
    row_coverage = set()
    sensors_on_row = set()
    for (sx, sy), (bx, by) in sensors:
        dist = abs(sx - bx) + abs(sy - by)
        y_diff = abs(sy - row_y)
        if y_diff <= dist:
            x_diff_max = dist - y_diff
            x_left = sx - x_diff_max
            x_right = sx + x_diff_max
            row_coverage.update(range(x_left, x_right + 1))
        if by == row_y:
            sensors_on_row.add(bx)
    row_coverage.difference_update(sensors_on_row)
    result_part_1 = len(row_coverage)
    print(f"part 1: {result_part_1}")

    # part 2
    # it takes a long time to run for large input, but hey, I only need to run it once...
    if filename == "sample.txt":
        max_coord = 20
    else:
        max_coord = 4_000_000
    candidates = set()
    for i, ((sx, sy), (bx, by)) in enumerate(sensors):
        dist = abs(sx - bx) + abs(sy - by) + 1
        for y in range(max(sy - dist, 0), min(sy + dist, max_coord) + 1):
            dx = dist - abs(y - sy)
            cand = [(x, y) for x in [sx - dx, sx + dx] if 0 <= x <= max_coord]
            for j, ((sx2, sy2), (bx2, by2)) in enumerate(sensors):
                if i != j:
                    dist2 = abs(sx2 - bx2) + abs(sy2 - by2)
                    for xx, yy in list(cand):
                        if abs(xx - sx2) + abs(yy - sy2) <= dist2:
                            cand.remove((xx, yy))
                if not cand:
                    break
            candidates.update(cand)

    assert len(candidates) == 1
    x, y = candidates.pop()
    result_part_2 = x * 4_000_000 + y
    print(f"part 2: {result_part_2}")


if __name__ == "__main__":
    for name in [
        "sample.txt",
        "input.txt"
    ]:
        print(f"-- {name} --")
        main(name)
