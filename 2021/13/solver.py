def main(filename):
    dots = []
    foldings = []
    with open(filename) as input_file:
        for line in input_file:
            line = line.strip()
            if not line:
                continue
            if line.startswith("fold along"):
                axis, value = line.replace("fold along ", "").split("=")
                foldings.append((axis, int(value)))
            else:
                x, y = map(int, line.split(","))
                dots.append((x, y))

    max_x = max(x for x, _ in dots)
    max_y = max(y for _, y in dots)
    grid = [["."] * (max_x + 1) for _ in range(max_y + 1)]
    for x, y in dots:
        grid[y][x] = "#"

    for i, (axis, value) in enumerate(foldings):
        if axis == "x":
            assert value >= len(grid[0]) // 2
            delta = len(grid[0]) - value - 1
            for y in range(len(grid)):
                for x in range(delta):
                    if grid[y][-1 - x] == "#":
                        grid[y][-2 * delta - 1 + x] = "#"
                grid[y] = grid[y][:value]
        else:
            assert value >= len(grid) // 2
            delta = len(grid) - value - 1
            for x in range(len(grid[0])):
                for y in range(delta):
                    if grid[-1 - y][x] == "#":
                        grid[-2 * delta - 1 + y][x] = "#"
            grid = grid[:value]

        if i == 0:
            result_part_1 = sum(grid[y][x] == "#" for y in range(len(grid)) for x in range(len(grid[0])))
    print(f"part 1: {result_part_1}")

    print("part 2:")
    # prints "ALREKFKU"
    for row in grid:
        print("".join(row))


if __name__ == "__main__":
    for input_filename in [
        "sample.txt",
        "input.txt"
    ]:
        print(f"-- {input_filename} --")
        main(input_filename)
