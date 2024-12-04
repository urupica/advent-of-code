def main(filename):
    with open(filename) as input_file:
        grid = [line.strip() for line in input_file]

    n = len(grid)
    assert n == len(grid[0])  # make sure the grid is square

    # part 1
    directions = [(i, j) for i in range(-1, 2) for j in range(-1, 2) if i != 0 or j != 0]
    result_part_1 = sum(
        all(grid[i + k * a][j + k * b] == x for k, x in enumerate("XMAS"))
        for i in range(n)
        for j in range(n)
        for a, b in directions
        if 0 <= i + 3 * a < n and 0 <= j + 3 * b < n
    )
    print(f"part 1: {result_part_1}")

    # part 2
    result_part_2 = sum(
        (
            grid[i][j] == "A" and
            {grid[i - 1][j - 1], grid[i + 1][j + 1]} == {grid[i + 1][j - 1], grid[i - 1][j + 1]} == {"M", "S"}
        )
        for i in range(1, n - 1)
        for j in range(1, n - 1)
    )
    print(f"part 2: {result_part_2}")


if __name__ == "__main__":
    for input_filename in [
        "sample.txt",
        "input.txt"
    ]:
        print(f"-- {input_filename} --")
        main(input_filename)
