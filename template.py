def main(filename):
    with open(filename) as input_file:
        for line in input_file:
            line = line.strip()

    result_part_1 = None
    print(f"part 1: {result_part_1}")

    # result_part_2 = None
    # print(f"part 2: {result_part_2}")


if __name__ == "__main__":
    for input_filename in [
        "sample.txt",
        "input.txt"
    ]:
        print(f"-- {input_filename} --")
        main(input_filename)
