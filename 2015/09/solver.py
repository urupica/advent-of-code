import re
from collections import defaultdict
from itertools import permutations


def solve(filename):
    with open(filename) as input_file:
        connections = []
        for line in input_file:
            result = re.match("(.+) to (.+) = (\d+)", line.strip())
            a, b, n = result.groups()
            connections.append((a, b, int(n)))

    neigh = defaultdict(dict)
    for a, b, n in connections:
        neigh[a][b] = n
        neigh[b][a] = n

    shortest = None
    longest = None
    for perm in permutations(neigh):
        length = 0
        for a, b in zip(perm[:-1], perm[1:]):
            if b not in neigh[a]:
                length = None
                break
            length += neigh[a][b]
        if length is not None:
            if shortest is None or length < shortest:
                shortest = length
            if longest is None or length > longest:
                longest = length

    print(f"part 1: {shortest}")
    print(f"part 2: {longest}")


def main():
    for filename in [
        "sample.txt",
        "input.txt"
    ]:
        print(f"-- {filename} --")
        solve(filename)


if __name__ == "__main__":
    main()
