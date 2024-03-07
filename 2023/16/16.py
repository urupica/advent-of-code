def get_next_positions(grid, i, j, d):
    if d == "r":
        if grid[i][j] in ".-":
            next_positions = [(i, j + 1, "r")]
        elif grid[i][j] == "/":
            next_positions = [(i - 1, j, "u")]
        elif grid[i][j] == "\\":
            next_positions = [(i + 1, j, "d")]
        else:
            next_positions = [(i - 1, j, "u"), (i + 1, j, "d")]
    elif d == "l":
        if grid[i][j] in ".-":
            next_positions = [(i, j - 1, "l")]
        elif grid[i][j] == "/":
            next_positions = [(i + 1, j, "d")]
        elif grid[i][j] == "\\":
            next_positions = [(i - 1, j, "u")]
        else:
            next_positions = [(i - 1, j, "u"), (i + 1, j, "d")]
    elif d == "d":
        if grid[i][j] in ".|":
            next_positions = [(i + 1, j, "d")]
        elif grid[i][j] == "/":
            next_positions = [(i, j - 1, "l")]
        elif grid[i][j] == "\\":
            next_positions = [(i, j + 1, "r")]
        else:
            next_positions = [(i, j - 1, "l"), (i, j + 1, "r")]
    else:
        if grid[i][j] in ".|":
            next_positions = [(i - 1, j, "u")]
        elif grid[i][j] == "/":
            next_positions = [(i, j + 1, "r")]
        elif grid[i][j] == "\\":
            next_positions = [(i, j - 1, "l")]
        else:
            next_positions = [(i, j - 1, "l"), (i, j + 1, "r")]
    return [(ii, jj, dd) for ii, jj, dd in next_positions if 0 <= ii < len(grid) and 0 <= jj < len(grid[0])]


def get_energized_cells(grid, i_s, j_s, d_s):
    visited = set()
    pool = [(i_s, j_s, d_s)]
    while pool:
        i, j, d = pool.pop()
        if (i, j, d) in visited:
            continue
        visited.add((i, j, d))
        for ii, jj, dd in get_next_positions(grid, i, j, d):
            if (ii, jj, dd) not in visited:
                pool.append((ii, jj, dd))
    visited_cells = {(i, j) for i, j, _ in visited}
    return len(visited_cells)


def main():
    with open("input.txt") as input_file:
        grid = [row.strip() for row in input_file]

    # part 1
    total = get_energized_cells(grid, 0, 0, "r")
    print(f"part 1: {total}")

    # part 2
    total = 0
    for i in range(len(grid)):
        total = max(total, get_energized_cells(grid, i, 0, "r"))
        total = max(total, get_energized_cells(grid, i, len(grid[0]) - 1, "l"))
    for j in range(len(grid[0])):
        total = max(total, get_energized_cells(grid, 0, j, "d"))
        total = max(total, get_energized_cells(grid, len(grid) - 1, j, "u"))
    print(f"part 2: {total}")


if __name__ == "__main__":
    main()
