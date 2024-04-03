def main(filename):
    with open(filename) as input_file:
        depths = [int(line.strip()) for line in input_file]

    result_part_1 = sum(d2 > d1 for d1, d2 in zip(depths[:-1], depths[1:]))
    print(f"part 1: {result_part_1}")

    result_part_2 = sum(sum(depths[n + 1:n + 4]) > sum(depths[n:n + 3]) for n in range(len(depths) - 3))
    print(f"part 2: {result_part_2}")


if __name__ == "__main__":
    for input_filename in [
        "sample.txt",
        "input.txt"
    ]:
        print(f"-- {input_filename} --")
        main(input_filename)
