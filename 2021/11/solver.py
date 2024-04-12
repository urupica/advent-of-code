def main(filename):
    with open(filename) as input_file:
        grid = [list(map(int, line.strip())) for line in input_file]
    rows = len(grid)
    cols = len(grid[0])

    result_part_1 = 0
    step = 0
    while True:
        step += 1
        flashed = set()
        flashed_visited = set()
        for i in range(rows):
            for j in range(cols):
                grid[i][j] += 1
                if grid[i][j] > 9:
                    flashed.add((i, j))
        while flashed:
            i, j = flashed.pop()
            flashed_visited.add((i, j))
            for ii in range(max(i - 1, 0), min(i + 1, rows - 1) + 1):
                for jj in range(max(j - 1, 0), min(j + 1, cols - 1) + 1):
                    if ii == i and jj == j:
                        continue
                    grid[ii][jj] += 1
                    if grid[ii][jj] > 9 and (ii, jj) not in flashed_visited:
                        flashed.add((ii, jj))
        for i, j in flashed_visited:
            grid[i][j] = 0
        if step <= 100:
            result_part_1 += len(flashed_visited)
        if len(flashed_visited) == rows * cols:
            result_part_2 = step
            break

    print(f"part 1: {result_part_1}")
    print(f"part 2: {result_part_2}")


if __name__ == "__main__":
    for input_filename in [
        "sample.txt",
        "input.txt"
    ]:
        print(f"-- {input_filename} --")
        main(input_filename)
