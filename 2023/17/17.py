def parse_input():
    with open("sample.txt") as input_file:
        grid = [list(map(int, row.strip())) for row in input_file]
    return grid


def get_next_positions1(grid, i, j, c, d):
    next_positions = []
    if d is None:
        assert i == j == c == 0
        next_positions += [(1, 0, 1, "d"), (0, 1, 1, "r")]
    elif d == "r":
        next_positions += [(i + 1, j, 1, "d"), (i - 1, j, 1, "u"), (i, j + 1, c + 1, "r")]
    elif d == "l":
        next_positions += [(i + 1, j, 1, "d"), (i - 1, j, 1, "u"), (i, j - 1, c + 1, "l")]
    elif d == "d":
        next_positions += [(i, j + 1, 1, "r"), (i, j - 1, 1, "l"), (i + 1, j, c + 1, "d")]
    else:
        assert d == "u"
        next_positions += [(i, j + 1, 1, "r"), (i, j - 1, 1, "l"), (i - 1, j, c + 1, "u")]
    return [pos for pos in next_positions if 0 <= pos[0] < len(grid) and 0 <= pos[1] < len(grid[0]) and pos[2] <= 3]


def main1():
    grid = parse_input()

    pool = [(0, 0, 0, None)]
    visited = set()
    dist = {(0, 0, 0, None): 0}
    while True:
        m = min(pool, key=dist.get)
        pool.remove(m)
        if m in visited:
            continue
        visited.add(m)
        i, j, c, d = m
        if i == len(grid) - 1 and j == len(grid[0]) - 1:
            result = dist[m]
            break
        for pos in get_next_positions1(grid, i, j, c, d):
            if pos in visited:
                continue
            ii, jj = pos[:2]
            if pos not in dist:
                dist[pos] = dist[m] + grid[ii][jj]
            else:
                dist[pos] = min(dist[pos], dist[m] + grid[ii][jj])
            pool.append(pos)

    print(result)


def get_next_positions2(grid, i, j, c, d):
    next_positions = []
    if d is None:
        assert i == j == c == 0
        next_positions += [(4, 0, 4, "d", [(ii, 0) for ii in range(1, 4)]), (0, 4, 4, "r", [(0, jj) for jj in range(1, 4)])]
    elif d == "r":
        next_positions += [(i + 4, j, 4, "d", [(i + ii, j) for ii in range(1, 4)]), (i - 4, j, 4, "u", [(i - ii, j) for ii in range(1, 4)]), (i, j + 1, c + 1, "r", [])]
    elif d == "l":
        next_positions += [(i + 4, j, 4, "d", [(i + ii, j) for ii in range(1, 4)]), (i - 4, j, 4, "u", [(i - ii, j) for ii in range(1, 4)]), (i, j - 1, c + 1, "l", [])]
    elif d == "d":
        next_positions += [(i, j + 4, 4, "r", [(i, j + jj) for jj in range(1, 4)]), (i, j - 4, 4, "l", [(i, j - jj) for jj in range(1, 4)]), (i + 1, j, c + 1, "d", [])]
    else:
        assert d == "u"
        next_positions += [(i, j + 4, 4, "r", [(i, j + jj) for jj in range(1, 4)]), (i, j - 4, 4, "l", [(i, j - jj) for jj in range(1, 4)]), (i - 1, j, c + 1, "u", [])]
    return [pos for pos in next_positions if 0 <= pos[0] < len(grid) and 0 <= pos[1] < len(grid[0]) and 4 <= pos[2] <= 10]


def main2():
    grid = parse_input()

    pool = [(0, 0, 0, None)]
    visited = set()
    dist = {(0, 0, 0, None): 0}
    while True:
        m = min(pool, key=dist.get)
        pool.remove(m)
        if m in visited:
            continue
        visited.add(m)
        i, j, c, d = m

        has_better = False
        for (ii, jj, cc, dd), dst in dist.items():
            if ii == i and jj == j and dd == d and cc <= c and dist[(ii, jj, cc, dd)] < dist[m]:
                has_better = True
                break
        if has_better:
            continue

        if i == len(grid) - 1 and j == len(grid[0]) - 1:
            result = dist[m]
            break
        for *pos, ext in get_next_positions2(grid, i, j, c, d):
            pos = tuple(pos)
            if pos in visited:
                continue
            ii, jj = pos[:2]
            new_dist = grid[ii][jj] + sum(grid[iii][jjj] for iii, jjj in ext)
            if pos not in dist:
                dist[pos] = dist[m] + new_dist
            else:
                dist[pos] = min(dist[pos], dist[m] + new_dist)
            pool.append(pos)

    print(result)


if __name__ == "__main__":
    main2()
