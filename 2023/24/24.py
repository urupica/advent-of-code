from itertools import combinations
from fractions import Fraction as frac
from scipy.linalg import solve


def parse_input(filename):
    with open(filename) as input_file:
        hailstones = []
        for row in input_file:
            row = row.strip()
            position, velocity = [part.strip() for part in row.split("@")]
            position = tuple(int(n) for n in position.split(","))
            velocity = tuple(int(n) for n in velocity.split(","))
            hailstones.append((position, velocity))
    return hailstones


def will_cross(p1, v1, p2, v2, test_area):
    mn, mx = test_area
    det = -v1[0] * v2[1] + v1[1] * v2[0]
    if det == 0:
        return False
    t1 = frac(1, det) * (v2[1] * (p1[0] - p2[0]) - v2[0] * (p1[1] - p2[1]))
    t2 = frac(1, det) * (v1[1] * (p1[0] - p2[0]) - v1[0] * (p1[1] - p2[1]))
    x1 = p1[0] + t1 * v1[0]
    y1 = p1[1] + t1 * v1[1]
    x2 = p2[0] + t2 * v2[0]
    y2 = p2[1] + t2 * v2[1]
    assert x1 == x2
    assert y1 == y2
    return t1 > 0 and t2 > 0 and mn <= x1 <= mx and mn <= y1 <= mx


def main():
    # filename, test_area = "sample.txt", (7, 27)
    filename, test_area = "input.txt", (200000000000000, 400000000000000)
    hailstones = parse_input(filename)

    # part 1
    total = sum(will_cross(p1, v1, p2, v2, test_area) for (p1, v1), (p2, v2) in combinations(hailstones, 2))
    print(f"part 1: {total}")

    # part 2
    (p1, v1), (p2, v2), (p3, v3) = hailstones[:3]
    w1 = [v1[i] - v2[i] for i in range(3)]
    w2 = [v1[i] - v3[i] for i in range(3)]
    q1 = [p2[i] - p1[i] for i in range(3)]
    q2 = [p3[i] - p1[i] for i in range(3)]
    a = [
        [0, w1[2], -w1[1], 0, q1[2], -q1[1]],
        [-w1[2], 0, w1[0], -q1[2], 0, q1[0]],
        [w1[1], -w1[0], 0, q1[1], -q1[0], 0],
        [0, w2[2], -w2[1], 0, q2[2], -q2[1]],
        [-w2[2], 0, w2[0], -q2[2], 0, q2[0]],
        [w2[1], -w2[0], 0, q2[1], -q2[0], 0],
    ]
    b = [
        p1[1] * v1[2] - p1[2] * v1[1] - (p2[1] * v2[2] - p2[2] * v2[1]),
        p1[2] * v1[0] - p1[0] * v1[2] - (p2[2] * v2[0] - p2[0] * v2[2]),
        p1[0] * v1[1] - p1[1] * v1[0] - (p2[0] * v2[1] - p2[1] * v2[0]),
        p1[1] * v1[2] - p1[2] * v1[1] - (p3[1] * v3[2] - p3[2] * v3[1]),
        p1[2] * v1[0] - p1[0] * v1[2] - (p3[2] * v3[0] - p3[0] * v3[2]),
        p1[0] * v1[1] - p1[1] * v1[0] - (p3[0] * v3[1] - p3[1] * v3[0]),
    ]
    ret = solve(a, b)
    print(f"part 2: {sum(map(lambda x: int(x + 0.1), ret[:3]))}")


if __name__ == "__main__":
    main()
