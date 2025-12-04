def get_removable_rolls(grid):
    removable_rolls = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] != "@":
                continue

            neighbors = 0
            for ii in range(i - 1, i + 2):
                for jj in range(j - 1, j + 2):
                    if i == ii and j == jj:
                        continue
                    if 0 <= ii < len(grid) and 0 <= jj < len(grid[0]) and grid[ii][jj] == "@":
                        neighbors += 1
            if neighbors < 4:
                removable_rolls.append((i, j))
    return removable_rolls


def solve(filename):
    with open(filename) as input_file:
        grid = [list(line.strip()) for line in input_file]

    result_part_1 = len(get_removable_rolls(grid))
    print(f"part 1: {result_part_1}")

    result_part_2 = 0
    while True:
        removable_rolls = get_removable_rolls(grid)
        if not removable_rolls:
            break

        result_part_2 += len(removable_rolls)
        for i, j in removable_rolls:
            grid[i][j] = "."

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
