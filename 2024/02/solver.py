def is_safe(report, tolerate_single_bad_level=False):
    report_variations = [report]
    if tolerate_single_bad_level:
        for i in range(len(report)):
            report_variations.append(report[:i] + report[i + 1:])

    for report in report_variations:
        a, b = report[:2]
        if not 1 <= abs(a - b) <= 3:
            continue

        sign = b - a
        if all(
            abs(c - d) <= 3 and sign * (d - c) > 0
            for c, d in zip(report[1:-1], report[2:])
        ):
            return True

    return False


def main(filename):
    data = []
    with open(filename) as input_file:
        for line in input_file:
            data.append([int(n) for n in line.strip().split()])

    result_part_1 = sum(is_safe(report) for report in data)
    print(f"part 1: {result_part_1}")

    result_part_2 = sum(is_safe(report, tolerate_single_bad_level=True) for report in data)
    print(f"part 1: {result_part_2}")


if __name__ == "__main__":
    for input_filename in [
        "sample.txt",
        "input.txt"
    ]:
        print(f"-- {input_filename} --")
        main(input_filename)
