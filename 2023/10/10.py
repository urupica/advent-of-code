def get_next(grid, curr, prev):
    i, j = curr
    n, m = prev
    if grid[i][j] == "|":
        if n == i - 1:
            return i + 1, j
        return i - 1, j
    if grid[i][j] == "-":
        if m == j - 1:
            return i, j + 1
        return i, j - 1
    if grid[i][j] == "L":
        if n == i - 1:
            return i, j + 1
        return i - 1, j
    if grid[i][j] == "J":
        if n == i - 1:
            return i, j - 1
        return i - 1, j
    if grid[i][j] == "7":
        if n == i + 1:
            return i, j - 1
        return i + 1, j
    if grid[i][j] == "F":
        if n == i + 1:
            return i, j + 1
        return i + 1, j


def main1():
    with open("input.txt") as input_file:
        grid = [row.strip() for row in input_file]

    start = None
    for i, row in enumerate(grid):
        if "S" in row:
            j = row.index("S")
            start = (i, j)
            break
    i, j = start
    starting_points = []
    if i - 1 >= 0 and grid[i - 1][j] in "|7F":
        starting_points.append((i - 1, j))
    if i + 1 < len(grid) and grid[i + 1][j] in "|LJ":
        starting_points.append((i + 1, j))
    if j - 1 >= 0 and grid[i][j - 1] in "-LF":
        starting_points.append((i, j - 1))
    if j + 1 < len(grid[0]) and grid[i][j + 1] in "-J7":
        starting_points.append((i, j + 1))

    assert len(starting_points) == 2

    length = 1
    curr1, curr2 = starting_points
    prev1 = prev2 = start
    while curr1 != curr2:
        curr1, prev1 = get_next(grid, curr1, prev1), curr1
        curr2, prev2 = get_next(grid, curr2, prev2), curr2
        length += 1

    print(length)


def main2():
    with open("input.txt") as input_file:
        grid = [row.strip() for row in input_file]

    loop = []
    for i, row in enumerate(grid):
        if "S" in row:
            j = row.index("S")
            loop.append((i, j))
            break
    i, j = loop[0]
    if i - 1 >= 0 and grid[i - 1][j] in "|7F":
        loop.append((i - 1, j))
    if len(loop) == 1 and i + 1 < len(grid) and grid[i + 1][j] in "|LJ":
        loop.append((i + 1, j))
    if len(loop) == 1 and j - 1 >= 0 and grid[i][j - 1] in "-LF":
        loop.append((i, j - 1))
    if len(loop) == 1 and j + 1 < len(grid[0]) and grid[i][j + 1] in "-J7":
        loop.append((i, j + 1))

    prev, curr = loop
    while curr != loop[0]:
        loop.append(curr)
        curr, prev = get_next(grid, curr, prev), curr

    total = 0
    for i in list(range(len(grid))):
        for j in list(range(len(grid[0]))):
            if (i, j) in loop:
                continue

            counter = 0
            visited = set()
            for k, (n, m) in enumerate(loop):
                if k in visited:
                    continue
                if n != i or m < j:
                    continue

                visited.add(k)
                kk = (k - 1) % len(loop)
                while loop[kk][0] == n:
                    visited.add(kk)
                    kk = (kk - 1) % len(loop)
                prv = -1 if loop[kk][0] < n else 1
                kk = (k + 1) % len(loop)
                while loop[kk][0] == n:
                    visited.add(kk)
                    kk = (kk + 1) % len(loop)
                nxt = -1 if loop[kk][0] < n else 1
                if prv == -1 and nxt == 1:
                    counter += 1
                elif prv == 1 and nxt == -1:
                    counter -= 1
            assert counter in {-1, 0, 1}
            if counter != 0:
                total += 1
    print(total)


if __name__ == "__main__":
    main2()
