from collections import defaultdict


def main1():
    with open("input.txt") as input_file:
        grid = [row.strip() for row in input_file]

    additional_rows = []
    additional_cols = []
    for i, row in enumerate(grid):
        if "#" not in row:
            additional_rows.append(i)
    for j in range(len(grid[0])):
        if "#" not in {grid[i][j] for i in range(len(grid))}:
            additional_cols.append(j)

    horizontal = defaultdict(int)
    vertical = defaultdict(int)
    for i, row in enumerate(grid):
        for j, x in enumerate(row):
            if x == "#":
                horizontal[j] += 1
                vertical[i] += 1

    hor_count = sum(horizontal.values())
    ver_count = sum(vertical.values())
    hor_sorted = sorted(horizontal)
    ver_sorted = sorted(vertical)

    total = 0

    left = horizontal[hor_sorted[0]]
    right = hor_count - left
    j = 0
    jj = 0
    while right > 0:
        a, b = hor_sorted[j:j + 2]
        additional = 0
        while jj < len(additional_cols) and a < additional_cols[jj] < b:
            additional += 1
            jj += 1
        total += left * right * (b - a + additional)
        right -= horizontal[b]
        left += horizontal[b]
        j += 1

    up = vertical[ver_sorted[0]]
    down = ver_count - up
    i = 0
    ii = 0
    while down > 0:
        a, b = ver_sorted[i:i + 2]
        additional = 0
        while ii < len(additional_rows) and a < additional_rows[ii] < b:
            additional += 1
            ii += 1
        total += up * down * (b - a + additional)
        down -= vertical[b]
        up += vertical[b]
        i += 1

    print(total)


def main2():
    with open("input.txt") as input_file:
        grid = [row.strip() for row in input_file]

    additional_rows = []
    additional_cols = []
    for i, row in enumerate(grid):
        if "#" not in row:
            additional_rows.append(i)
    for j in range(len(grid[0])):
        if "#" not in {grid[i][j] for i in range(len(grid))}:
            additional_cols.append(j)

    horizontal = defaultdict(int)
    vertical = defaultdict(int)
    for i, row in enumerate(grid):
        for j, x in enumerate(row):
            if x == "#":
                horizontal[j] += 1
                vertical[i] += 1

    hor_count = sum(horizontal.values())
    ver_count = sum(vertical.values())
    hor_sorted = sorted(horizontal)
    ver_sorted = sorted(vertical)

    total = 0

    left = horizontal[hor_sorted[0]]
    right = hor_count - left
    j = 0
    jj = 0
    while right > 0:
        a, b = hor_sorted[j:j + 2]
        additional = 0
        while jj < len(additional_cols) and a < additional_cols[jj] < b:
            additional += 1000000 - 1
            jj += 1
        total += left * right * (b - a + additional)
        right -= horizontal[b]
        left += horizontal[b]
        j += 1

    up = vertical[ver_sorted[0]]
    down = ver_count - up
    i = 0
    ii = 0
    while down > 0:
        a, b = ver_sorted[i:i + 2]
        additional = 0
        while ii < len(additional_rows) and a < additional_rows[ii] < b:
            additional += 1000000 - 1
            ii += 1
        total += up * down * (b - a + additional)
        down -= vertical[b]
        up += vertical[b]
        i += 1

    print(total)


if __name__ == "__main__":
    main2()
