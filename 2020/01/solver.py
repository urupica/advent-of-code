from itertools import combinations


def main(filename):
    with open(filename) as input_file:
        entries = [int(line) for line in input_file]

    result_part_1 = None
    for a, b in combinations(entries, 2):
        if a + b == 2020:
            result_part_1 = a * b
            break

    result_part_2 = None
    for a, b, c in combinations(entries, 3):
        if a + b + c == 2020:
            result_part_2 = a * b * c
            break

    print(f"part 1: {result_part_1}")
    print(f"part 2: {result_part_2}")


if __name__ == "__main__":
    for input_filename in [
        "sample.txt",
        "input.txt"
    ]:
        print(f"-- {input_filename} --")
        main(input_filename)
