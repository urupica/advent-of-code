def main(filename):
    result_part_1 = None
    result_part_2 = None
    with open(filename) as input_file:
        for line in input_file:
            line = line.strip()

            # part 1

            # part 2

    print(f"part 1: {result_part_1}")
    print(f"part 2: {result_part_2}")


if __name__ == "__main__":
    for name in [
        "sample.txt",
        "input.txt"
    ]:
        print(f"-- {name} --")
        main(name)
