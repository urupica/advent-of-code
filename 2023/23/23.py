def is_valid_slope_walk(i, j, ii, jj, grid, check_slopes):
    if not check_slopes:
        return True
    return (
        ii < i and grid[i][j] == "^"
        or ii > i and grid[i][j] == "v"
        or jj < j and grid[i][j] == "<"
        or jj > j and grid[i][j] == ">"
    )


def parse_input(filename, check_slopes):
    with open(filename) as input_file:
        grid = [row.strip() for row in input_file]

    start = end = None
    vertices = set()
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell != "#":
                if i == 0:
                    start = (i, j)
                if i == len(grid) - 1:
                    end = (i, j)
                neighbor_count = 0
                for ii, jj in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                    if 0 <= ii < len(grid) and 0 <= jj < len(grid[0]) and grid[ii][jj] != "#":
                        neighbor_count += 1
                if neighbor_count > 2:
                    vertices.add((i, j))
    vertices.update({start, end})

    neighbors = {v: [] for v in vertices}
    for i, j in vertices:
        paths = []
        for ii, jj in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
            if 0 <= ii < len(grid) and 0 <= jj < len(grid[0]) and grid[ii][jj] != "#":
                if grid[i][j] == "." or is_valid_slope_walk(i, j, ii, jj, grid, check_slopes):
                    paths.append(((i, j), (ii, jj), 1))
        for path_start, path_current, length in paths:
            if path_current in neighbors:
                neighbors[path_start].append((path_current, length))
                continue
            path_prev = path_start
            while True:
                path_next = None
                i, j = path_current
                for ii, jj in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                    if (ii, jj) != path_prev and 0 <= ii < len(grid) and 0 <= jj < len(grid[0]) and grid[ii][jj] != "#":
                        if grid[i][j] == "." or is_valid_slope_walk(i, j, ii, jj, grid, check_slopes):
                            path_next = (ii, jj)
                            break
                if path_next is None:
                    break
                elif path_next in neighbors:
                    neighbors[path_start].append((path_next, length + 1))
                    break
                path_prev = path_current
                path_current = path_next
                length += 1
    return neighbors, start, end


def main():
    for part in [1, 2]:
        neighbors, start, end = parse_input("input.txt", check_slopes=part == 1)
        max_length = 0
        pool = [(start, 0, set())]
        while pool:
            vertex, path_length, visited = pool.pop()
            for neigh, edge_length in neighbors[vertex]:
                if neigh not in visited:
                    if neigh == end:
                        max_length = max(max_length, path_length + edge_length)
                    else:
                        pool.append((neigh, path_length + edge_length, visited.union({vertex})))
        print(f"part {part}: {max_length}")


if __name__ == "__main__":
    main()
