def parse_input(filename, part):
    steps = []
    with open(filename) as input_file:
        for row in input_file:
            parts = row.strip().split()
            if part == 1:
                direction, distance, _ = parts
                distance = int(distance)
            else:
                *_, code = parts
                distance = int(code[2:-2], 16)
                direction = "RDLU"[int(code[-2])]
            steps.append((direction, distance))
    return steps


def compute_area(steps):
    x = y = 0
    path = []
    for d, l in steps:
        assert l > 0
        if d == "R":
            y += l
        elif d == "L":
            y -= l
        elif d == "D":
            x += l
        else:
            assert d == "U"
            x -= l
        path.append((x, y))

    area = sum(
        path[i][0] * path[(i + 1) % len(path)][1] - path[i][1] * path[(i + 1) % len(path)][0]
        for i in range(len(path))
    ) // 2
    if area > 0:
        # make sure the path goes clockwise
        path = path[::-1]

    # expand area
    path_expanded = []
    for i, (y, x) in enumerate(path):
        yp, xp = path[(i - 1) % len(path)]
        yn, xn = path[(i + 1) % len(path)]
        assert sum(x != xo for xo in [xp, xn]) == sum(y != yo for yo in [yp, yn]) == 1
        xx = x
        yy = y
        if x > xp:
            if yn > y:
                xx = x + 1
        elif x < xp:
            yy = y + 1
            if yn > y:
                xx = x + 1
        elif y > yp:
            xx = x + 1
            if xn < x:
                yy = y + 1
        elif y < yp:
            if xn < x:
                yy = y + 1
        else:
            raise ValueError("#####")

        path_expanded.append((yy, xx))

    area_expanded = -sum(
        path_expanded[i][0] * path_expanded[(i + 1) % len(path_expanded)][1] - path_expanded[i][1] * path_expanded[(i + 1) % len(path_expanded)][0]
        for i in range(len(path_expanded))
    ) // 2
    return area_expanded


def main():
    # filename = "sample.txt"
    filename = "input.txt"

    for part in [1, 2]:
        steps = parse_input(filename, part)
        area = compute_area(steps)
        print(f"part {part}: {area}")


if __name__ == "__main__":
    main()
