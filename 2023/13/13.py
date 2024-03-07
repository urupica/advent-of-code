def find_mirror(grid, skip_mirror=None):
    for i in range(1, len(grid)):
        if skip_mirror is not None and skip_mirror == i:
            continue
        is_mirror = True
        for row1, row2 in zip(grid[i:], grid[i - 1::-1]):
            if row1 != row2:
                is_mirror = False
                break
        if is_mirror:
            return i


def find_mirror_both_directions(grid):
    hor_mirror = find_mirror(grid)
    if hor_mirror is not None:
        return 100 * hor_mirror

    grid_transposed = [[grid[i][j] for i in range(len(grid))] for j in range(len(grid[0]))]
    return find_mirror(grid_transposed)


def main1():
    total = 0
    grid = []
    with open("input.txt") as input_file:
        for row in input_file:
            row = list(row.strip())
            if row:
                grid.append(row)
            else:
                total += find_mirror_both_directions(grid)
                grid = []
    total += find_mirror_both_directions(grid)

    print(total)


def find_other_mirror_both_directions(grid):
    hor_mirror = find_mirror(grid)
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            grid[i][j] = "#" if grid[i][j] == "." else "."
            hor_mirror_new = find_mirror(grid, skip_mirror=hor_mirror)
            grid[i][j] = "#" if grid[i][j] == "." else "."
            if hor_mirror_new is not None:
                return 100 * hor_mirror_new

    grid_transposed = [[grid[i][j] for i in range(len(grid))] for j in range(len(grid[0]))]
    ver_mirror = find_mirror(grid_transposed)
    for i in range(len(grid_transposed)):
        for j in range(len(grid_transposed[0])):
            grid_transposed[i][j] = "#" if grid_transposed[i][j] == "." else "."
            ver_mirror_new = find_mirror(grid_transposed, skip_mirror=ver_mirror)
            grid_transposed[i][j] = "#" if grid_transposed[i][j] == "." else "."
            if ver_mirror_new is not None:
                return ver_mirror_new


def main2():
    total = 0
    grid = []
    with open("input.txt") as input_file:
        for row in input_file:
            row = list(row.strip())
            if row:
                grid.append(row)
            else:
                total += find_other_mirror_both_directions(grid)
                grid = []
    total += find_other_mirror_both_directions(grid)

    print(total)


if __name__ == "__main__":
    main2()
