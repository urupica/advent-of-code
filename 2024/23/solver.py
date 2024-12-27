from collections import defaultdict
from itertools import combinations


neighbors = {}


def find_maximal_cliques(r, p, x):
    # Bron–Kerbosch algorithm
    if not p and not x:
        yield r

    while p:
        v = p.pop()
        n = neighbors[v]
        yield from find_maximal_cliques(r.union({v}), p.intersection(n), x.intersection(n))
        x.add(v)


def count_triples():
    found = set()
    valid_vertices = [v for v in neighbors if v.startswith("t")]
    for v in valid_vertices:
        for a, b in combinations(neighbors[v], 2):
            if b in neighbors[a]:
                s = tuple(sorted({v, a, b}))
                found.add(s)
    return len(found)


def solve(filename):
    global neighbors
    neighbors = defaultdict(set)
    with open(filename) as input_file:
        for line in input_file:
            v, w = line.strip().split("-")
            neighbors[v].add(w)
            neighbors[w].add(v)

    result_part_1 = count_triples()
    print(f"part 1: {result_part_1}")

    largest_clique = max(find_maximal_cliques(set(), set(neighbors), set()), key=len)
    result_part_2 = ",".join(sorted(largest_clique))
    print(f"part 2: {result_part_2}")


def main():
    for filename in [
        "sample.txt",
        "input.txt"
    ]:
        print(f"-- {filename} --")
        solve(filename)


if __name__ == "__main__":
    main()
