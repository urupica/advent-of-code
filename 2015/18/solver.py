def perform_step(grid, corners_stuck=False):
    n = len(grid)
    m = len(grid[0])

    corners = [(0, 0), (n - 1, 0), (0, m - 1), (n - 1, m - 1)]
    if corners_stuck:
        for i, j in corners:
            grid[i][j] = 1

    grid_copy = [list(row) for row in grid]
    for i in range(n):
        for j in range(m):
            if corners_stuck and (i, j) in corners:
                continue

            count = sum(
                grid_copy[ii][jj]
                for ii in range(max(0, i - 1), min(n - 1, i + 1) + 1)
                for jj in range(max(0, j - 1), min(m - 1, j + 1) + 1)
                if ii != i or jj != j
            )
            if grid_copy[i][j] == 1 and count not in [2, 3]:
                grid[i][j] = 0
            elif grid_copy[i][j] == 0 and count == 3:
                grid[i][j] = 1


def solve(filename):
    grid_orig = []
    with open(filename) as input_file:
        for line in input_file:
            grid_orig.append([1 if x == "#" else 0 for x in line.strip()])

    steps = 4 if filename == "sample.txt" else 100
    grid = [list(row) for row in grid_orig]
    for _ in range(steps):
        perform_step(grid)
    result_part_1 = sum(sum(row) for row in grid)
    print(f"part 1: {result_part_1}")

    steps = 5 if filename == "sample.txt" else 100
    grid = [list(row) for row in grid_orig]
    for _ in range(steps):
        perform_step(grid, corners_stuck=True)
    result_part_2 = sum(sum(row) for row in grid)
    print(f"part 2: {result_part_2}")


def main():
    for filename in [
        "sample.txt",
        "input.txt"
    ]:
        print(f"-- {filename} --")
        solve(filename)


if __name__ == "__main__":
    main()
