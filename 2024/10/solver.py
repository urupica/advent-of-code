def get_score(grid, source, ignore_multiple_paths=True):
    n = len(grid)
    m = len(grid[0])

    score = 0
    stack = [source]
    visited = set()
    while stack:
        i, j = stack.pop()

        if (i, j) in visited:
            continue

        if ignore_multiple_paths:
            visited.add((i, j))

        if grid[i][j] == 9:
            score += 1
            continue

        for ii, jj in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
            if 0 <= ii < n and 0 <= jj < m and grid[ii][jj] == grid[i][j] + 1 and (ii, jj) not in visited:
                stack.append((ii, jj))

    return score


def main(filename):
    with open(filename) as input_file:
        grid = tuple(tuple(map(int, line.strip())) for line in input_file)

    n = len(grid)
    m = len(grid[0])

    result_part_1 = sum(
        get_score(grid, (i, j))
        for i in range(n)
        for j in range(m)
        if grid[i][j] == 0
    )
    print(f"part 1: {result_part_1}")

    result_part_2 = sum(
        get_score(grid, (i, j), ignore_multiple_paths=False)
        for i in range(n)
        for j in range(m)
        if grid[i][j] == 0
    )
    print(f"part 2: {result_part_2}")


if __name__ == "__main__":
    for input_filename in [
        "sample.txt",
        "input.txt"
    ]:
        print(f"-- {input_filename} --")
        main(input_filename)
