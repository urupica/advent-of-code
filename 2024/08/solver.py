from collections import defaultdict
from itertools import combinations


def count_antinodes(n, m, frequency_coordinate_list, include_resonance=False):
    antinodes = set()
    for frequency_coordinates in frequency_coordinate_list:
        for (i, j), (ii, jj) in combinations(frequency_coordinates, 2):
            di = abs(ii - i)
            dj = abs(jj - j)
            if (ii - i) * (jj - j) > 0:
                directions = [(-di, -dj), (di, dj)]
            else:
                directions = [(-di, +dj), (di, -dj)]
            for ddi, ddj in directions:
                count = 0
                a = max(i, ii) if ddi >= 0 else min(i, ii)
                b = max(j, jj) if ddj >= 0 else min(j, jj)
                while 0 <= a < n and 0 <= b < m and (include_resonance or count <= 1):
                    if include_resonance or count == 1:
                        antinodes.add((a, b))
                    a += ddi
                    b += ddj
                    count += 1
    return len(antinodes)


def main(filename):
    with open(filename) as input_file:
        grid = [line.strip() for line in input_file]

    n = len(grid)
    m = len(grid[0])
    antennas = defaultdict(list)
    for i in range(n):
        for j in range(m):
            frequency = grid[i][j]
            if frequency != ".":
                antennas[frequency].append((i, j))

    result_part_1 = count_antinodes(n, m, antennas.values())
    print(f"part 1: {result_part_1}")

    result_part_2 = count_antinodes(n, m, antennas.values(), include_resonance=True)
    print(f"part 2: {result_part_2}")


if __name__ == "__main__":
    for input_filename in [
        "sample.txt",
        "input.txt"
    ]:
        print(f"-- {input_filename} --")
        main(input_filename)
