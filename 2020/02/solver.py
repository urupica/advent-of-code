import re


def main(filename):
    database = []
    with open(filename) as input_file:
        for line in input_file:
            line = line.strip()
            a, b, char, password = re.match(r"(\d+)-(\d+) ([a-z]): ([a-z]+)", line).groups()
            database.append((int(a), int(b), char, password))

    result_part_1 = sum(
        mn <= password.count(char) <= mx
        for mn, mx, char, password in database
    )

    result_part_2 = sum(
        (password[first - 1] == char) ^ (password[second - 1] == char)
        for first, second, char, password in database
    )

    print(f"part 1: {result_part_1}")
    print(f"part 2: {result_part_2}")


if __name__ == "__main__":
    for input_filename in [
        "sample.txt",
        "input.txt"
    ]:
        print(f"-- {input_filename} --")
        main(input_filename)
