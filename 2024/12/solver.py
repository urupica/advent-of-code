def get_regions(grid):
    n, m = len(grid), len(grid[0])
    regions = []
    visited = set()
    for i in range(n):
        for j in range(m):
            if (i, j) in visited:
                continue

            region = set()
            pool = [(i, j)]
            plant = grid[i][j]
            while pool:
                a, b = pool.pop()
                if (a, b) in region:
                    continue

                region.add((a, b))
                for aa, bb in [(a - 1, b), (a + 1, b), (a, b - 1), (a, b + 1)]:
                    if 0 <= aa < n and 0 <= bb < m and grid[aa][bb] == plant and (aa, bb) not in region:
                        pool.append((aa, bb))

            regions.append(region)
            visited.update(region)

    return regions

def get_area_and_perimeters(regions, sides_only=False):
    for region in regions:
        area = len(region)

        perimeter = set()
        for a, b in region:
            for aa, bb, d in [(a - 1, b, "d"), (a + 1, b, "u"), (a, b - 1, "l"), (a, b + 1, "r")]:
                if (aa, bb) not in region:
                    perimeter.add((a, b, d))

        if not sides_only:
            yield area, len(perimeter)
            continue

        sides_count = 0
        while perimeter:
            a, b, d = perimeter.pop()
            sides_count += 1
            if d in ["l", "r"]:
                for sign in [-1, 1]:
                    aa = a + sign
                    while (aa, b, d) in perimeter:
                        perimeter.remove((aa, b, d))
                        aa += sign
            else:
                for sign in [-1, 1]:
                    bb = b + sign
                    while (a, bb, d) in perimeter:
                        perimeter.remove((a, bb, d))
                        bb += sign
        yield area, sides_count


def main(filename):
    with open(filename) as input_file:
        grid = [line.strip() for line in input_file]

    regions = get_regions(grid)

    result_part_1 = sum(area * perimeter for area, perimeter in get_area_and_perimeters(regions))
    print(f"part 1: {result_part_1}")

    result_part_2 = sum(area * sides for area, sides in get_area_and_perimeters(regions, sides_only=True))
    print(f"part 2: {result_part_2}")


if __name__ == "__main__":
    for input_filename in [
        "sample.txt",
        "input.txt"
    ]:
        print(f"-- {input_filename} --")
        main(input_filename)
