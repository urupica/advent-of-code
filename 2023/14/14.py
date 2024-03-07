def read_input(filename):
    with open(filename) as input_file:
        return [list(row.strip()) for row in input_file]


def tilt(grid, direction):
    for i in range(len(grid)):
        offset = 0
        for j in range(len(grid)):
            x = {
                "n": grid[j][i],
                "w": grid[i][j],
                "s": grid[len(grid) - 1 - j][i],
                "e": grid[i][len(grid) - 1 - j],
            }[direction]
            if x == "O":
                if j > offset:
                    ii, jj, io, jo = {
                        "n": (j, i, offset, i),
                        "w": (i, j, i, offset),
                        "s": (len(grid) - 1 - j, i, len(grid) - 1 - offset, i),
                        "e": (i, len(grid) - 1 - j, i, len(grid) - 1 - offset),
                    }[direction]
                    grid[io][jo] = "O"
                    grid[ii][jj] = "."
                offset += 1
            elif x == "#":
                offset = j + 1


def compute_north_load(grid):
    return sum((len(grid) - i) * row.count("O") for i, row in enumerate(grid))


def main():
    filename = "input.txt"

    # part 1
    grid = read_input(filename)
    tilt(grid, "n")
    load = compute_north_load(grid)
    print(f"part 1: {load}")

    # part 2
    grid = read_input(filename)
    prev_grid = tuple(tuple(row) for row in grid)
    next_grid_map = {}
    while True:
        for direction in "nwse":
            tilt(grid, direction)
        curr_grid = tuple(tuple(row) for row in grid)
        next_grid_map[prev_grid] = curr_grid
        prev_grid = curr_grid
        if curr_grid in next_grid_map:
            break

    next_grid_list = list(next_grid_map)
    cycle_start_index = next_grid_list.index(next_grid_map[next_grid_list[-1]])
    cycle_length = len(next_grid_list) - cycle_start_index

    offset = (10**9 - cycle_start_index) % cycle_length
    last_grid = next_grid_list[cycle_start_index + offset]
    load = compute_north_load(last_grid)
    print(f"part 2: {load}")


if __name__ == "__main__":
    main()
