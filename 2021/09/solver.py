import operator
from functools import reduce


def main(filename):
    with open(filename) as input_file:
        grid = [list(map(int, line.strip())) for line in input_file]

    result_part_1 = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if all(
                grid[i][j] < grid[ii][jj]
                for ii, jj in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]
                if 0 <= ii < len(grid) and 0 <= jj < len(grid[0])
            ):
                result_part_1 += 1 + grid[i][j]
    print(f"part 1: {result_part_1}")

    unvisited = {(i, j) for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j] != 9}
    basin_sizes = []
    while unvisited:
        # discover next basin
        pool = [unvisited.pop()]
        visited = set()
        while pool:
            i, j = pool.pop()
            if (i, j) in visited:
                continue
            visited.add((i, j))
            for ii, jj in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if 0 <= ii < len(grid) and 0 <= jj < len(grid[0]) and grid[ii][jj] != 9:
                    if (ii, jj) not in visited:
                        pool.append((ii, jj))
        basin_sizes.append(len(visited))
        unvisited.difference_update(visited)

    basin_sizes.sort()
    result_part_2 = reduce(operator.mul, basin_sizes[-3:])
    print(f"part 2: {result_part_2}")


if __name__ == "__main__":
    for input_filename in [
        "sample.txt",
        "input.txt"
    ]:
        print(f"-- {input_filename} --")
        main(input_filename)
