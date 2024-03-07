from collections import defaultdict


STEPS = 26501365


def print_grid(grid, current_positions):
    for i, row in enumerate(grid):
        print("".join("O" if (i, j) in current_positions else x for j, x in enumerate(row)))
    print()


def main():
    with open("input.txt") as input_file:
        grid = [row.strip() for row in input_file]

    start = None
    for i, row in enumerate(grid):
        for j, x in enumerate(row):
            if x == "S":
                start = (i, j)

    N, M = len(grid), len(grid[0])

    # part 1
    current_positions = {start}
    for s in range(64):
        next_positions = set()
        for i, j in current_positions:
            for ii, jj in [(i + 1, j), (i - 1, j), (i, j - 1), (i, j + 1)]:
                if 0 <= ii < N and 0 <= jj < M and grid[ii][jj] in {".", "S"}:
                    next_positions.add((ii, jj))
        current_positions = next_positions
    print(f"part 1: {len(current_positions)}")

    # part 2
    current_positions = {start}
    first_odd = defaultdict(dict)
    first_even = defaultdict(dict)
    first_even[start][(0, 0)] = 0
    visited = set()
    s = 0
    total = None
    while True:
        s += 1
        next_positions = set()
        for i, j in current_positions:
            if (i, j) in visited:
                continue
            visited.add((i, j))
            first_dict = first_even if s % 2 == 0 else first_odd
            for ii, jj in [(i + 1, j), (i - 1, j), (i, j - 1), (i, j + 1)]:
                if grid[ii % N][jj % M] in {".", "S"}:
                    if (ii, jj) in visited:
                        continue
                    next_positions.add((ii, jj))
                    ii_m, ii_d = ii % N, ii // N
                    jj_m, jj_d = jj % M, jj // M
                    if (ii_m, jj_m) not in first_dict or (ii_d, jj_d) not in first_dict[(ii_m, jj_m)]:
                        first_dict[(ii_m, jj_m)][(ii_d, jj_d)] = s
        current_positions = next_positions

        if (STEPS % 2) != (s % 2):
            continue

        valid = True
        total = 0
        first_dict = first_even if STEPS % 2 == 0 else first_odd
        for (i, j) in first_dict:
            first_dict_i_j = first_dict[(i, j)]
            if (0, 0) in first_dict_i_j:
                total += 1

                # axes
                for u, v in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    if not (6 * u, 6 * v) in first_dict_i_j:
                        valid = False
                        break
                    total += 2 + (STEPS - first_dict_i_j[(4 * u, 4 * v)]) // (first_dict_i_j[(6 * u, 6 * v)] - first_dict_i_j[(4 * u, 4 * v)])

                # quadrants
                for u, v in [(1, 1), (-1, 1), (1, -1), (-1, -1)]:
                    if not all(((1 + k) * u, (3 - k) * v) in first_dict_i_j for k in range(3)):
                        valid = False
                        break
                    mem = (STEPS - first_dict_i_j[(u, v)]) // (first_dict_i_j[(2 * u, 2 * v)] - first_dict_i_j[(u, v)])
                    total += (mem + 1) ** 2

            else:
                # axes
                for u, v in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    if not (5 * u, 5 * v) in first_dict_i_j:
                        valid = False
                        break
                    total += 2 + (STEPS - first_dict_i_j[(3 * u, 3 * v)]) // (first_dict_i_j[(5 * u, 5 * v)] - first_dict_i_j[(3 * u, 3 * v)])

                # quadrants
                for u, v in [(1, 1), (-1, 1), (1, -1), (-1, -1)]:
                    if not all(((1 + k) * u, (4 - k) * v) in first_dict_i_j for k in range(4)):
                        valid = False
                        break
                    mem = (STEPS - first_dict_i_j[(2 * u, v)]) // (first_dict_i_j[(4 * u, v)] - first_dict_i_j[(2 * u, v)])
                    total += (mem + 1) * (mem + 2)

            if not valid:
                break
        if valid:
            break

    print(f"part 2: {total}")


if __name__ == "__main__":
    main()
