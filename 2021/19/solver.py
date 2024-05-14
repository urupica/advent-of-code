from collections import Counter
from itertools import permutations, combinations

import numpy as np


def get_all_rotations():
    two_d_rotations = [[[1, 0], [0, 1]], [[0, 1], [-1, 0]], [[-1, 0], [0, -1]], [[0, -1], [1, 0]]]

    x_rotations = [
        [[1, 0, 0], [0] + m[0], [0] + m[1]]
        for m in two_d_rotations
    ]
    y_rotations = [
        [[m[0][0], 0, m[0][1]], [0, 1, 0], [m[1][0], 0, m[1][1]]]
        for m in two_d_rotations
    ]
    z_rotations = [
        [m[0] + [0], m[1] + [0], [0, 0, 1]]
        for m in two_d_rotations
    ]

    all_rotations = set()
    for x in x_rotations:
        for y in y_rotations:
            for z in z_rotations:
                for a, b, c in permutations([x, y, z]):
                    all_rotations.add(tuple(tuple(row) for row in np.matmul(np.matmul(a, b), c)))
    all_rotations = tuple(all_rotations)

    return all_rotations


def check_intersection(all_rotations, scanners, i, j):
    for rot in all_rotations:
        beacons_i = scanners[i][1]
        beacons_j_rotated = [np.matmul(rot, bcn) for bcn in scanners[j][1]]
        diff_counter = Counter(tuple(bcn_j - bcn_i) for bcn_i in beacons_i for bcn_j in beacons_j_rotated)
        diff_counter_max = max(diff_counter.values())
        if diff_counter_max >= 12:
            diff = [dff for dff, cnt in diff_counter.items() if cnt == diff_counter_max][0]
            return (
                tuple(np.array(scanners[i][0]) - diff),
                tuple(tuple(bcn) for bcn in beacons_j_rotated)
            )


def main(filename):
    scanners = []
    beacons = []
    with open(filename) as input_file:
        for line in input_file:
            line = line.strip()
            if line.startswith("--- scanner"):
                beacons = []
            elif not line:
                scanners.append(((0, 0, 0), beacons))
            else:
                beacons.append(tuple(map(int, line.split(","))))
    scanners.append(((0, 0, 0), beacons))

    all_rotations = get_all_rotations()
    visited = set()
    pool = {0}
    while pool:
        i = pool.pop()
        if i in visited:
            continue
        visited.add(i)

        for j in set(range(len(scanners))).difference(visited).difference(pool):
            new_scanner_j_data = check_intersection(all_rotations, scanners, i, j)
            if new_scanner_j_data:
                scanners[j] = new_scanner_j_data
                pool.add(j)

    all_beacons = {tuple(np.array(origin) + beacon) for origin, beacons in scanners for beacon in beacons}
    result_part_1 = len(all_beacons)
    print(f"part 1: {result_part_1}")

    result_part_2 = max(
        abs(a_x - b_x) + abs(a_y - b_y) + abs(a_z - b_z)
        for ((a_x, a_y, a_z), _), ((b_x, b_y, b_z), _) in combinations(scanners, 2)
    )
    print(f"part 2: {result_part_2}")


if __name__ == "__main__":
    for input_filename in [
        "sample.txt",
        "input.txt"
    ]:
        print(f"-- {input_filename} --")
        main(input_filename)
