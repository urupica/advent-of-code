import re


def do_intersect(cuboid_1, cuboid_2):
    x_min_1, x_max_1, y_min_1, y_max_1, z_min_1, z_max_1 = cuboid_1
    x_min_2, x_max_2, y_min_2, y_max_2, z_min_2, z_max_2 = cuboid_2
    return (
        x_min_1 < x_max_2 and x_min_2 < x_max_1
        and y_min_1 < y_max_2 and y_min_2 < y_max_1
        and z_min_1 < z_max_2 and z_min_2 < z_max_1
    )


def get_difference_cuboids(cuboid_1, cuboid_2):
    # remove cuboid_2 part from cuboid_1 and break remaining part of cuboid_1 into cuboids
    x_min_1, x_max_1, y_min_1, y_max_1, z_min_1, z_max_1 = cuboid_1
    x_min_2, x_max_2, y_min_2, y_max_2, z_min_2, z_max_2 = cuboid_2
    x_limits = sorted({x_min_1, x_max_1, x_min_2, x_max_2})
    y_limits = sorted({y_min_1, y_max_1, y_min_2, y_max_2})
    z_limits = sorted({z_min_1, z_max_1, z_min_2, z_max_2})
    for x_min, x_max in zip(x_limits[:-1], x_limits[1:]):
        for y_min, y_max in zip(y_limits[:-1], y_limits[1:]):
            for z_min, z_max in zip(z_limits[:-1], z_limits[1:]):
                if (
                    x_min_1 <= x_min and x_max <= x_max_1
                    and y_min_1 <= y_min and y_max <= y_max_1
                    and z_min_1 <= z_min and z_max <= z_max_1
                ) and not (
                    x_min_2 <= x_min and x_max <= x_max_2
                    and y_min_2 <= y_min and y_max <= y_max_2
                    and z_min_2 <= z_min and z_max <= z_max_2
                ):
                    yield x_min, x_max, y_min, y_max, z_min, z_max


def main(filename):
    steps = []
    with open(filename) as input_file:
        for line in input_file:
            line = line.strip()
            # pattern examples:
            # on x=10..12,y=10..12,z=10..12
            # off x=9..11,y=9..11,z=9..11
            result = re.search(r"(on|off) x=(-?\d+)\.\.(-?\d+),y=(-?\d+)\.\.(-?\d+),z=(-?\d+)\.\.(-?\d+)", line)
            on_or_off, *coordinates = result.groups()
            # increase upper limits by one
            coordinates = tuple(int(n) if i % 2 == 0 else int(n) + 1 for i, n in enumerate(coordinates))
            steps.append((on_or_off, tuple(map(int, coordinates))))

    on_cuboids = set()
    for on_or_off, cuboid in steps:
        if on_or_off == "on":
            new_on_cuboid_parts = {cuboid}
            for on_cuboid in list(on_cuboids):
                for cuboid_part in list(new_on_cuboid_parts):
                    if do_intersect(on_cuboid, cuboid_part):
                        new_on_cuboid_parts.remove(cuboid_part)
                        new_on_cuboid_parts.update(get_difference_cuboids(cuboid_part, on_cuboid))
            on_cuboids.update(new_on_cuboid_parts)
        else:
            for on_cuboid in list(on_cuboids):
                if do_intersect(on_cuboid, cuboid):
                    on_cuboids.remove(on_cuboid)
                    on_cuboids.update(get_difference_cuboids(on_cuboid, cuboid))

    result_part_1 = sum(
        (x_max - x_min) * (y_max - y_min) * (z_max - z_min)
        for x_min, x_max, y_min, y_max, z_min, z_max in on_cuboids
        if -50 <= min(x_min, y_min, z_min) and max(x_max, y_max, z_max) <= 51
    )
    print(f"part 1: {result_part_1}")

    result_part_2 = sum(
        (x_max - x_min) * (y_max - y_min) * (z_max - z_min)
        for x_min, x_max, y_min, y_max, z_min, z_max in on_cuboids
    )
    print(f"part 2: {result_part_2}")


if __name__ == "__main__":
    for input_filename in [
        "sample.txt",
        "input.txt"
    ]:
        print(f"-- {input_filename} --")
        main(input_filename)
