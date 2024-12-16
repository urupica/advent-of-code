from collections import defaultdict


def compute_score(grid, path_length=False):
    directions = "rdlu"
    n = len(grid)
    m = len(grid[0])

    start = next((i, j) for i in range(n) for j in range(m) if grid[i][j] == "S")
    dist = {(start, "r"): 0}
    visited = set()
    prev = defaultdict(set)
    min_dist = None
    while set(dist).difference(visited):
        (i, j), d = min(set(dist).difference(visited), key=dist.get)
        visited.add(((i, j), d))

        if grid[i][j] == "E":
            if not path_length:
                return dist[((i, j), d)]
            if min_dist is None or dist[((i, j), d)] < min_dist:
                min_dist = dist[((i, j), d)]
            continue

        if min_dist is not None and dist[((i, j), d)] >= min_dist:
            continue

        k = directions.index(d)
        for dd, points in [(d, 1), (directions[(k - 1) % 4], 1001), (directions[(k + 1) % 4], 1001)]:
            ii, jj = {
                "r": (i, j + 1),
                "l": (i, j - 1),
                "d": (i + 1, j),
                "u": (i - 1, j),
            }[dd]
            if 0 <= ii < n and 0 <= jj < m and grid[ii][jj] in ".SE" and ((ii, jj), dd) not in visited:
                if ((ii, jj), dd) not in dist or dist[((i, j), d)] + points <= dist[((ii, jj), dd)]:
                    dist[((ii, jj), dd)] = dist[((i, j), d)] + points
                    if path_length:
                        prev[((ii, jj), dd)].add(((i, j), d))

    end = next((i, j) for i in range(n) for j in range(m) if grid[i][j] == "E")
    seats = set()
    pool = [(end, d) for d in directions if (end, d) in dist and dist[(end, d)] == min_dist]
    while pool:
        pos, d = pool.pop()
        seats.add(pos)
        pool.extend(prev[(pos, d)])
    return len(seats)

def main(filename):
    with open(filename) as input_file:
        grid = [line.strip() for line in input_file]

    result_part_1 = compute_score(grid)
    print(f"part 1: {result_part_1}")

    result_part_2 = compute_score(grid, path_length=True)
    print(f"part 2: {result_part_2}")


if __name__ == "__main__":
    for input_filename in [
        "sample.txt",
        "input.txt"
    ]:
        print(f"-- {input_filename} --")
        main(input_filename)
