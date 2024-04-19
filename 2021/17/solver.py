from math import sqrt, floor, ceil


def get_y_k(vy, y):
    return vy + 0.5 + sqrt((vy + 0.5) ** 2 - 2 * y)


def get_x(vx, k):
    k = min(k, vx + 1)
    return k * vx - (k - 1) * k // 2


def get_y(vy, k):
    return k * vy - (k - 1) * k // 2


def get_mx_height(vy):
    if vy <= 0:
        return 0
    return get_y(vy, vy + 1)


def main(filename):
    with open(filename) as input_file:
        # target area: x=20..30, y=-10..-5
        line = input_file.readline().strip()
        x_range, y_range = line.replace("target area: x=", "").split(", y=")
        x_min, x_max = map(int, x_range.split(".."))
        y_min, y_max = map(int, y_range.split(".."))

    result_part_1 = 0
    result_part_2 = 0
    for vx in range(1, x_max + 1):
        # upper bound is just a guess, it worked...
        for vy in range(y_min, 1_000):
            k1 = floor(get_y_k(vy, y_max))
            k2 = ceil(get_y_k(vy, y_min))
            x1 = get_x(vx, k1)
            x2 = get_x(vx, k2)
            found = False
            if x1 <= x_max and x2 >= x_min:
                for k in range(k1, k2 + 1):
                    x = get_x(vx, k)
                    y = get_y(vy, k)
                    if x_min <= x <= x_max and y_min <= y <= y_max:
                        result_part_1 = max(result_part_1, get_mx_height(vy))
                        found = True
            if found:
                result_part_2 += 1

    print(f"part 1: {result_part_1}")
    print(f"part 2: {result_part_2}")


if __name__ == "__main__":
    for input_filename in [
        "sample.txt",
        "input.txt"
    ]:
        print(f"-- {input_filename} --")
        main(input_filename)
