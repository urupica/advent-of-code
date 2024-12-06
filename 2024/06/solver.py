from collections import defaultdict


def simulate_tour(grid):
    n = len(grid)
    assert len(grid[0]) == n  # confirm that it's a square grid

    i, j = next((i, j) for i in range(n) for j in range(n) if grid[i][j] == "^")  # start position
    u, v = -1, 0  # direction, start facing up

    visited = defaultdict(list)
    visited[(i, j)].append((u, v))
    is_loop = False
    while True:
        ii, jj = i + u, j + v  # try to move one step in direction (u, v)
        if not 0 <= ii < n or not 0 <= jj < n:
            break  # would move outside the grid
        elif grid[ii][jj] == "#":
            u, v = v, -u  # hit an obstacle rotate 90 degrees clockwise
        else:
            i, j = ii, jj  # valid move
            if (u, v) in visited[(i, j)]:  # we already were on that spot facing that direction
                is_loop = True
                break
            visited[(i, j)].append((u, v))

    path = list(visited)
    return path, is_loop


def count_loops(grid):
    path, _ = simulate_tour(grid)
    count = 0
    # put obstacles each position of the original tour, all other positions wouldn't affect the path
    # we're not allowed to block the starting position
    for i, j in path[1:]:
        grid[i][j] = "#"
        _, is_loop = simulate_tour(grid)
        grid[i][j] = "."
        if is_loop:
            count += 1
    return count


def main(filename):
    with open(filename) as input_file:
        grid = [list(line.strip()) for line in input_file]

    path, _ = simulate_tour(grid)
    result_part_1 = len(path)
    print(f"part 1: {result_part_1}")

    result_part_2 = count_loops(grid)
    print(f"part 2: {result_part_2}")


if __name__ == "__main__":
    for input_filename in [
        "sample.txt",
        "input.txt"
    ]:
        print(f"-- {input_filename} --")
        main(input_filename)
