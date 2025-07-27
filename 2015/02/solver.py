def solve(filename):
    boxes = []
    with open(filename) as input_file:
        for line in input_file:
            boxes.append(tuple(sorted(map(int, line.split("x")))))


    result_part_1 = sum(3 * a * b + 2 * a * c + 2 * b * c for a, b, c in boxes)
    print(f"part 1: {result_part_1}")

    result_part_2 = sum(2 * (a + b) + a * b * c for a, b, c in boxes)
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
