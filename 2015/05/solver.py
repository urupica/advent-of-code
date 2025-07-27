from itertools import product
from string import ascii_lowercase


def solve(filename):
    with open(filename) as input_file:
        lines = [line.strip() for line in input_file]

    result_part_1 = sum(
        all(
            [
                sum(line.count(vowel) for vowel in "aeiou") >= 3,
                any(letter * 2 in line for letter in ascii_lowercase),
                not any(string in line for string in ["ab", "cd", "pq", "xy"])
            ]
        )
        for line in lines
    )
    print(f"part 1: {result_part_1}")

    result_part_2 = sum(
        all(
            [
                any(
                    (pair:="".join(comb)) in line and pair in line[line.index(pair) + 2:]
                    for comb in product(ascii_lowercase, repeat=2)
                ),
                any(
                    letter == line[i] == line[i + 2]
                    for letter in ascii_lowercase
                    for i in range(len(line) - 2)
                )
            ]
        )
        for line in lines
    )
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
