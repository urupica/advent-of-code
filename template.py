def solve(filename):
    with open(filename) as input_file:
        for line in input_file:
            line = line.strip()

    result_part_1 = None
    print(f"part 1: {result_part_1}")

    # result_part_2 = None
    # print(f"part 2: {result_part_2}")


def main():
    for filename in [
        "sample.txt",
        "input.txt"
    ]:
        print(f"-- {filename} --")
        solve(filename)


if __name__ == "__main__":
    main()
