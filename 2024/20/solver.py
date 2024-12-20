from collections import deque


def get_distances_to(grid, vertex):
    n, m = len(grid), len(grid[0])
    queue = deque()
    dist = {vertex: 0}
    queue.append(vertex)
    while queue:
        i, j = queue.popleft()
        for ii, jj in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
            if 0 <= ii < n and 0 <= jj < m and grid[ii][jj] != "#" and (ii, jj) not in dist:
                dist[(ii, jj)] = dist[(i, j)] + 1
                queue.append((ii, jj))
    return dist


def count_cheats(grid, min_save, max_cheat_length):
    n, m = len(grid), len(grid[0])
    start = next((i, j) for i in range(n) for j in range(m) if grid[i][j] == "S")
    end = next((i, j) for i in range(n) for j in range(m) if grid[i][j] == "E")
    dist_start = get_distances_to(grid, start)
    dist_end = get_distances_to(grid, end)
    path_length = dist_end[start]
    max_length = path_length - min_save

    cheats = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == "#":
                continue
            ds = dist_start[(i, j)]
            for ii in range(max(0, i - max_cheat_length), min(n, i + max_cheat_length + 1)):
                for jj in range(max(0, j - max_cheat_length), min(n, j + max_cheat_length + 1)):
                    if grid[ii][jj] == "#":
                        continue
                    d = abs(i - ii) + abs(j - jj)
                    if d > max_cheat_length:
                        continue
                    de = dist_end[(ii, jj)]
                    if ds + d + de <= max_length:
                        cheats += 1
    return cheats


def main(filename):
    with open(filename) as input_file:
        grid = [line.strip() for line in input_file]

    if filename == "sample.txt":
        # check all sample values from the description
        print("verifying output data for part 1...")
        for ps, save in [(64, 1), (40, 1), (38, 1), (36, 1), (20, 1), (12, 3), (10, 2), (8, 4), (6, 2), (4, 14), (2, 14)]:
            a = count_cheats(grid, ps, 2)
            b = count_cheats(grid, ps + 1, 2)
            assert a - b == save, f"{ps}, {save}, {a}, {b}"

        print("verifying output data for part 2...")
        for ps, save in [(76, 3), (74, 4), (72, 22), (70, 12), (68, 14), (66, 12), (64, 19), (62, 20), (60, 23), (58, 25), (56, 39), (54, 29), (52, 31), (50, 32)]:
            a = count_cheats(grid, ps, 20)
            b = count_cheats(grid, ps + 1, 20)
            assert a - b == save, f"{ps}, {save}, {a}, {b}"
    else:
        result_part_1 = count_cheats(grid, 100, 2)
        print(f"part 1: {result_part_1}")

        result_part_2 = count_cheats(grid, 100, 20)
        print(f"part 2: {result_part_2}")


if __name__ == "__main__":
    for input_filename in [
        "sample.txt",
        "input.txt"
    ]:
        print(f"-- {input_filename} --")
        main(input_filename)
