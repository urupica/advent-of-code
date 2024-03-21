import re
from collections import defaultdict

aa = ba = ca = cb = da = dc = best = visited = None


def is_worse(a, b, c, d, A, B, C, D, s):
    return any(a2 >= a and b2 >= b and c2 >= c and d2 >= d for a2, b2, c2, d2 in visited[(A, B, C, D, s)])


def find_max(a, b, c, d, A, B, C, D, s=24):
    global best
    if s == 0:
        best = max(best, d)
        return
    if is_worse(a, b, c, d, A, B, C, D, s):
        return
    visited[(A, B, C, D, s)].add((a, b, c, d))
    an, bn, cn, dn = A, B, C, D
    if a >= da and c >= dc:
        if not is_worse(a - da + an, b + bn, c - dc + cn, d + dn, A, B, C, D + 1, s - 1):
            find_max(a - da + an, b + bn, c - dc + cn, d + dn, A, B, C, D + 1, s - 1)
    else:
        if C < dc and a >= ca and b >= cb and not is_worse(a - ca + an, b - cb + bn, c + cn, d + dn, A, B, C + 1, D, s - 1):
                find_max(a - ca + an, b - cb + bn, c + cn, d + dn, A, B, C + 1, D, s - 1)
        if A < max(aa, ba, ca, da) and a >= aa and not is_worse(a -aa + an, b + bn, c + cn, d + dn, A + 1, B, C, D, s - 1):
                find_max(a - aa + an, b + bn, c + cn, d + dn, A + 1, B, C, D, s - 1)
        if B < cb and a >= ba and not is_worse(a - ba + an, b + bn, c + cn, d + dn, A, B + 1, C, D, s - 1):
                find_max(a - ba + an, b + bn, c + cn, d + dn, A, B + 1, C, D, s - 1)
        if not is_worse(a + an, b + bn, c + cn, d + dn, A, B, C, D, s - 1):
            find_max(a + an, b + bn, c + cn, d + dn, A, B, C, D, s - 1)


def main(filename):
    global aa, ba, ca, cb, da, dc, best, visited
    blueprints = []
    with open(filename) as input_file:
        for line in input_file:
            line = line.strip()
            # Blueprint 1: Each ore robot costs 4 ore. Each clay robot costs 2 ore. Each obsidian robot costs 3 ore and 14 clay. Each geode robot costs 2 ore and 7 obsidian.
            parts = re.split("Blueprint |: Each ore robot costs | ore. Each clay robot costs | ore. Each obsidian robot costs | ore and | clay. Each geode robot costs | obsidian.", line)
            blueprints.append(tuple(map(int, parts[1:-1])))

    result_part_1 = 0
    for n, aa, ba, ca, cb, da, dc in blueprints:
        best = 0
        visited = defaultdict(set)
        find_max(0, 0, 0, 0, 1, 0, 0, 0)
        result_part_1 += n * best
    print(f"part 1: {result_part_1}")

    result_part_2 = 1
    for n, aa, ba, ca, cb, da, dc in blueprints[:3]:
        print(f"checking blueprint {n} of 3 ...")
        best = 0
        visited = defaultdict(set)
        find_max(0, 0, 0, 0, 1, 0, 0, 0, 32)
        print(best)
        result_part_2 *= best
    print(f"part 2: {result_part_2}")


if __name__ == "__main__":
    for input_filename in [
        "sample.txt",
        "input.txt"
    ]:
        print(f"-- {input_filename} --")
        main(input_filename)
