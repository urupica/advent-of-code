import operator
from collections import defaultdict
from functools import reduce
from random import choice


def parse_input():
    neighbors = defaultdict(list)
    with open("input.txt") as input_file:
        for row in input_file:
            row = row.strip()
            source, targets = row.split(": ")
            source = source.strip()
            targets = [target.strip() for target in targets.split()]
            for target in targets:
                neighbors[source].append(target)
                neighbors[target].append(source)
    return neighbors


def main1():
    neighbors_original = parse_input()

    # part 1: run Karger's algorithm until a solution is found
    while True:
        neighbors = {v: list(l) for v, l in neighbors_original.items()}
        vertex_size = {v: 1 for v in neighbors}
        while len(neighbors) > 2:
            source = choice(list(neighbors))
            target = choice(neighbors[source])
            vertex_size[source] += vertex_size[target]
            while target in neighbors[source]:
                neighbors[source].remove(target)
            new_neighbors = neighbors[target]
            while source in new_neighbors:
                new_neighbors.remove(source)
            for neigh in new_neighbors:
                while target in neighbors[neigh]:
                    neighbors[neigh].remove(target)
                    neighbors[neigh].append(source)
            neighbors[source].extend(new_neighbors)
            neighbors.pop(target)
            vertex_size.pop(target)
        if all(len(l) == 3 for l in neighbors.values()):
            break
    print(f"part 1: {reduce(operator.mul, vertex_size.values())}")


def main2():
    pass


if __name__ == "__main__":
    main1()
