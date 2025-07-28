import re
from collections import defaultdict
from itertools import permutations


def find_best(neigh):
    best = None
    for perm in permutations(neigh):
        total = 0
        for i in range(len(perm)):
            left, a, right = perm[(i - 1) % len(perm)], perm[i], perm[(i + 1) % len(perm)]
            total += neigh[a][left] + neigh[a][right]
        if best is None or total > best:
            best = total
    return best


def solve(filename):
    neigh = defaultdict(dict)
    with open(filename) as input_file:
        for line in input_file:
            line = line.strip()
            result = re.match(r"(.+) would (gain|lose) (\d+) happiness units by sitting next to (.+)\.", line)
            a, gain_or_loose, amount, b = result.groups()
            neigh[a][b] = int(amount) * (1 if gain_or_loose == "gain" else -1)

    best = find_best(neigh)
    print(f"part 1: {best}")

    attendees = list(neigh)
    neigh["me"] = {other: 0 for other in attendees}
    for other in attendees:
        neigh[other]["me"] = 0
    best = find_best(neigh)
    print(f"part 2: {best}")


def main():
    for filename in [
        "sample.txt",
        "input.txt"
    ]:
        print(f"-- {filename} --")
        solve(filename)


if __name__ == "__main__":
    main()
