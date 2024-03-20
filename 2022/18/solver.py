from itertools import combinations


def main(filename):
    cubes = []
    with open(filename) as input_file:
        for line in input_file:
            cubes.append(tuple(map(int, line.strip().split(","))))

    exposed_surfaces = 6 * len(cubes)
    for cube1, cube2 in combinations(cubes, 2):
        if sum(abs(a - b) for a, b in zip(cube1, cube2)) == 1:
            exposed_surfaces -= 2
    print(f"part 1: {exposed_surfaces}")

    min_x, max_x = min(x for x, y, z in cubes), max(x for x, y, z in cubes)
    min_y, max_y = min(y for x, y, z in cubes), max(y for x, y, z in cubes)
    min_z, max_z = min(z for x, y, z in cubes), max(z for x, y, z in cubes)
    cubes = set(cubes)
    outside_air_bubbles = (
        {(x, y, z) for x in range(min_x - 1, max_x + 2) for y in range(min_y - 1, max_y + 2) for z in {min_z - 1, max_z + 1}}
        | {(x, y, z) for x in range(min_x - 1, max_x + 2) for z in range(min_z - 1, max_z + 2) for y in {min_y - 1, max_y + 1}}
        | {(x, y, z) for y in range(min_y - 1, max_y + 2) for z in range(min_z - 1, max_z + 2) for x in {min_x - 1, max_x + 1}}
    )
    trapped_air_bubbles = set()
    candidates = {(x, y, z) for x in range(min_x, max_x + 1) for y in range(min_y, max_y + 1) for z in range(min_z, max_z + 1) if (x, y, z) not in cubes}
    for cand in candidates:
        pool = [cand]
        visited = set()
        determined = False
        while pool:
            v = pool.pop()
            if v in visited:
                continue
            x, y, z = v
            if v in outside_air_bubbles:
                outside_air_bubbles.add(cand)
                determined = True
                break
            elif v in trapped_air_bubbles:
                trapped_air_bubbles.add(cand)
                determined = True
                break
            visited.add(v)
            for xx, yy, zz in [(x - 1, y, z), (x + 1, y, z), (x, y - 1, z), (x, y + 1, z), (x, y, z - 1), (x, y, z + 1)]:
                if min_x - 1 <= xx <= max_x + 1 and min_y - 1 <= yy <= max_y + 1 and min_z - 1 <= zz <= max_z + 1:
                    if (xx, yy, zz) not in visited and (xx, yy, zz) not in cubes:
                        pool.append((xx, yy, zz))
        if not determined:
            trapped_air_bubbles.add(cand)

    trapped_surfaces = 0
    for air_bubble in trapped_air_bubbles:
        for cube in cubes:
            if sum(abs(a - b) for a, b in zip(air_bubble, cube)) == 1:
                trapped_surfaces += 1

    result_part_2 = exposed_surfaces - trapped_surfaces
    print(f"part 2: {result_part_2}")


if __name__ == "__main__":
    for input_filename in [
        "sample.txt",
        "input.txt"
    ]:
        print(f"-- {input_filename} --")
        main(input_filename)
