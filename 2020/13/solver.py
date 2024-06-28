import sympy


def apply_euclid_algo(a, b):
    t0, t1 = 0, 1
    s0, s1 = 1, 0
    r0, r1 = a, b

    while r1 != 0:
        q = r0 // r1
        r0, r1 = r1, r0 - q * r1
        s0, s1 = s1, s0 - q * s1
        t0, t1 = t1, t0 - q * t1

    return s0, t0


def main(filename):
    with open(filename) as input_file:
        earliest = int(input_file.readline().strip())
        bus_ids = [int(n) if n != "x" else n for n in input_file.readline().strip().split(",")]

    for n in bus_ids:
        if n != "x":
            assert sympy.isprime(n)

    result_part_1 = None
    departure = earliest
    while result_part_1 is None:
        for n in bus_ids:
            if n == "x":
                continue
            if departure % n == 0:
                result_part_1 = (departure - earliest) * n
                break
        departure += 1
    print(f"part 1: {result_part_1}")

    values = [(p, r) for r, p in enumerate(bus_ids) if p != "x"]
    p1, r1 = values[0]
    result_part_2 = None
    for i, (p2, r2) in enumerate(values[1:], start=1):
        n1, n2 = apply_euclid_algo(p1, p2)
        n1 *= (r1 - r2)
        n2 *= -(r1 - r2)

        if n1 < 0:
            k = (-n1) // p2 + 1
            n1 += k * p2
        if n1 - p2 > 0:
            k = n1 // p2
            n1 -= k * p2

        if i == len(values) - 1:
            result_part_2 = n1 * p1 - r1

        r1 -= n1 * p1
        p1 *= p2

    print(f"part 2: {result_part_2}")


if __name__ == "__main__":
    for input_filename in [
        "sample.txt",
        "input.txt"
    ]:
        print(f"-- {input_filename} --")
        main(input_filename)
