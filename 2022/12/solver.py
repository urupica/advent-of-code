from string import ascii_lowercase


def get_height(value):
    if value == "S":
        return 0
    if value == "E":
        return 25
    return ascii_lowercase.index(value)


def get_neighbors(grid, visited, vertex):
    i, j = vertex
    height = get_height(grid[i][j])
    for ii, jj in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
        if 0 <= ii < len(grid) and 0 <= jj < len(grid[0]) and (ii, jj) not in visited:
            other_height = get_height(grid[ii][jj])
            if other_height >= height - 1:
                yield ii, jj


def main(filename):
    with open(filename) as input_file:
        grid = [line.strip() for line in input_file]

    rows, cols = len(grid), len(grid[0])
    start = [(i, j) for i in range(rows) for j in range(cols) if grid[i][j] == "E"][0]
    dist = {(i, j): rows * cols for i in range(rows) for j in range(cols)}
    dist[start] = 0
    visited = set()
    unvisited = set(dist)
    current = start
    result_part_2 = None
    while True:
        for neigh in get_neighbors(grid, visited, current):
            dist[neigh] = min(dist[neigh], dist[current] + 1)
        visited.add(current)
        unvisited.remove(current)
        current = min(unvisited, key=dist.get)
        if grid[current[0]][current[1]] in "Sa":
            if result_part_2 is None:
                result_part_2 = dist[current]
        if grid[current[0]][current[1]] == "S":
            result_part_1 = dist[current]
            break

    print(f"part 1: {result_part_1}")
    print(f"part 2: {result_part_2}")


if __name__ == "__main__":
    for name in [
        "sample.txt",
        "input.txt"
    ]:
        print(f"-- {name} --")
        main(name)
