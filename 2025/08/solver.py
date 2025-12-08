from functools import reduce
from itertools import combinations
from operator import mul


def get_components(neighbors):
    components = []
    pool = list(neighbors)
    visited = set()
    while pool:
        i = pool.pop()
        if i in visited:
            continue
        component_pool = [i]
        component = []
        while component_pool:
            i = component_pool.pop()
            if i in visited:
                continue
            component.append(i)
            visited.add(i)
            for j in neighbors[i]:
                if j in visited:
                    continue
                component_pool.append(j)
        components.append(component)
    return components


def solve(filename):
    with open(filename) as input_file:
        junction_boxes = [tuple(map(int, line.split(","))) for line in input_file]

    distances = {}
    for (x1, y1, z1), (x2, y2, z2) in combinations(junction_boxes, 2):
        dist = (x2 - x1)**2 + (y2 - y1)**2 +  (z2 - z1)**2
        assert dist not in distances
        distances[dist] = (x1, y1, z1), (x2, y2, z2)

    junction_box_id_map = {box: i for i, box in enumerate(junction_boxes)}
    neighbors = {i: [] for i in junction_box_id_map.values()}

    # part 1
    pairs = 10 if filename == "sample.txt" else 1_000
    distances_sorted = sorted(distances.items())
    for dist, (v1, v2) in distances_sorted[:pairs]:
        i1 = junction_box_id_map[v1]
        i2 = junction_box_id_map[v2]
        neighbors[i1].append(i2)
        neighbors[i2].append(i1)

    components = get_components(neighbors)
    components.sort(key=len, reverse=True)
    result_part_1 = reduce(mul, map(len,  components[:3]), 1)
    print(f"part 1: {result_part_1}")

    # part 2
    result_part_2 = None
    for dist, (v1, v2) in distances_sorted[pairs:]:
        i1 = junction_box_id_map[v1]
        i2 = junction_box_id_map[v2]
        neighbors[i1].append(i2)
        neighbors[i2].append(i1)

        components = get_components(neighbors)
        if len(components) == 1:
            result_part_2 = v1[0] * v2[0]
            break
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
