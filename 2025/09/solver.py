from itertools import combinations
from shapely.geometry import Polygon


def solve(filename):
    with open(filename) as input_file:
        tiles = [tuple(map(int, line.strip().split(","))) for line in input_file]

    polygon = Polygon(tiles)
    max_area = 0
    max_area_inside = 0
    for (x1, y1), (x2, y2) in combinations(tiles, 2):
        x1, x2 = min(x1, x2), max(x1, x2)
        y1, y2 = min(y1, y2), max(y1, y2)
        area = (x2 + 1 - x1) * (y2 + 1 - y1)
        max_area = max(max_area, area)
        rectangle = Polygon([(x1, y1), (x1, y2), (x2, y2), (x2, y1)])
        if polygon.contains(rectangle):
            max_area_inside = max(max_area_inside, area)

    print(f"part 1: {max_area}")
    print(f"part 2: {max_area_inside}")


def main():
    for filename in [
        "sample.txt",
        "input.txt"
    ]:
        print(f"-- {filename} --")
        solve(filename)


if __name__ == "__main__":
    main()
