def parse_input(filename):
    grid = []
    movements = ""
    with open(filename) as input_file:
        is_grid_input = True
        for line in input_file:
            line = line.strip()
            if not line:
                is_grid_input = False
            elif is_grid_input:
                grid.append(list(line))
            else:
                movements += line
    return grid, movements


def increase_grid(grid):
    increased_grid = []
    for row in grid:
        increased_row = []
        for x in row:
            if x in ".#":
                increased_row.extend([x] * 2)
            elif x == "O":
                increased_row.extend(["[", "]"])
            else:
                increased_row.extend(["@", "."])
        increased_grid.append(increased_row)
    return increased_grid


def simulate(grid, movements):
    robot = next(
        (x, y)
        for y in range(len(grid))
        for x in range(len(grid[0]))
        if grid[y][x] == "@"
    )

    for d in movements:
        dx, dy = {
            "v": (0, 1),
            "^": (0, -1),
            ">": (1, 0),
            "<": (-1, 0),
        }[d]

        stack = [robot]
        i = 0
        possible = True
        while i < len(stack):
            x, y = stack[i]
            nx, ny = x + dx, y + dy
            if grid[ny][nx] == "O":
                if (nx, ny) not in stack:
                    stack.append((nx, ny))
            elif grid[ny][nx] == "[":
                if (nx, ny) not in stack:
                    stack.extend([(nx, ny), (nx + 1, ny)])
            elif grid[ny][nx] == "]":
                if (nx, ny) not in stack:
                    stack.extend([(nx, ny), (nx - 1, ny)])
            elif grid[ny][nx] == "#":
                possible = False
                break
            i += 1

        if possible:
            for x, y in stack[::-1]:
                grid[y + dy][x + dx] = grid[y][x]
                grid[y][x] = "."
            robot = stack[0][0] + dx, stack[0][1] + dy


def compute_sum(grid):
    return sum(
        100 * y + x
        for y in range(len(grid))
        for x in range(len(grid[0]))
        if grid[y][x] in "O["
    )


def main(filename):
    grid, movements = parse_input(filename)

    grid_copy = [list(row) for row in grid]
    simulate(grid_copy, movements)
    result_part_1 = compute_sum(grid_copy)
    print(f"part 1: {result_part_1}")

    increased_grid = increase_grid(grid)
    simulate(increased_grid, movements)
    result_part_2 = compute_sum(increased_grid)
    print(f"part 2: {result_part_2}")


if __name__ == "__main__":
    for input_filename in [
        "sample.txt",
        "input.txt"
    ]:
        print(f"-- {input_filename} --")
        main(input_filename)
