def main(filename):
    with open(filename) as input_file:
        part_1_count = 0
        part_2_count = 0

        for line in input_file:
            line = line.strip()

            range1, range2 = line.split(",")
            a, b = map(int, range1.split("-"))
            c, d = map(int, range2.split("-"))

            # part 1
            if a <= c <= d <= b or c <= a <= b <= d:
                part_1_count += 1

            # part 2
            if a <= c <= b or a <= d <= b or c <= a <= d or c <= b <= d:
                part_2_count += 1

    print(f"part 1: {part_1_count}")
    print(f"part 2: {part_2_count}")


if __name__ == "__main__":
    for filename in ["sample.txt", "input.txt"]:
        print(f"-- {filename} --")
        main(filename)
