def solve(filename):
    ranges = []
    ingredients = []
    with open(filename) as input_file:
        for line in input_file:
            line = line.strip()
            if not line:
                continue
            if "-" in line:
                ranges.append(tuple(map(int, line.split("-"))))
            else:
                ingredients.append(int(line))

    result_part_1 = sum(any(a <= n <= b for a, b in ranges) for n in ingredients)
    print(f"part 1: {result_part_1}")

    merged_ranges = []
    for a, b in ranges:
        am, bm = a, b
        merged_ranges_next = []

        i = 0
        n = len(merged_ranges)

        while i < n and merged_ranges[i][1] < am:
            merged_ranges_next.append(merged_ranges[i])
            i += 1

        while i < n and merged_ranges[i][0] <= b:
            am = min(am, merged_ranges[i][0])
            bm = max(bm, merged_ranges[i][1])
            i += 1

        merged_ranges_next.append((am, bm))

        merged_ranges_next.extend(merged_ranges[i:])

        merged_ranges = merged_ranges_next

    result_part_2 = sum(b + 1 - a for a, b in merged_ranges)
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
