from itertools import product


def get_adjacent_seats(grid, part):
    rows = len(grid)
    cols = len(grid[0])

    if part == 1:
        adjacent_seats = {
            (i, j): [
                (ii, jj)
                for ii in range(i - 1, i + 2) for jj in range(j - 1, j + 2)
                if (ii, jj) != (i, j) and 0 <= ii < rows and 0 <= jj < cols and grid[ii][jj] == "L"
            ]
            for i in range(rows) for j in range(cols) if grid[i][j] == "L"
        }
        occupancy_limit = 4
    else:
        adjacent_seats = {(i, j): [] for i in range(rows) for j in range(cols) if grid[i][j] == "L"}
        for i, j in adjacent_seats:
            for di, dj in product((-1, 0, 1), repeat=2):
                if di == dj == 0:
                    continue
                length = 1
                while True:
                    ii = i + length * di
                    jj = j + length * dj
                    if not 0 <= ii < rows or not 0 <= jj < cols:
                        break
                    if grid[ii][jj] == "L":
                        adjacent_seats[(i, j)].append((ii, jj))
                        break
                    length += 1
        occupancy_limit = 5
    return adjacent_seats, occupancy_limit


def main(filename):
    with open(filename) as input_file:
        original_grid = [list(line.strip()) for line in input_file]

    for part in [1, 2]:
        grid = [list(row) for row in original_grid]
        adjacent_seats, occupancy_limit = get_adjacent_seats(grid, part)
        while True:
            flip_status = []
            for (i, j), adjacent in adjacent_seats.items():
                if grid[i][j] == "L" and not any(grid[ii][jj] == "#" for ii, jj in adjacent):
                    flip_status.append((i, j))
                elif grid[i][j] == "#" and sum(grid[ii][jj] == "#" for ii, jj in adjacent) >= occupancy_limit:
                    flip_status.append((i, j))
            if flip_status:
                for i, j in flip_status:
                    grid[i][j] = "#" if grid[i][j] == "L" else "L"
            else:
                break
        result = sum(row.count("#") for row in grid)
        print(f"part {part}: {result}")


if __name__ == "__main__":
    for input_filename in [
        "sample.txt",
        "input.txt"
    ]:
        print(f"-- {input_filename} --")
        main(input_filename)
