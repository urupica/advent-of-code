import re
from itertools import batched

def compute_tokens(prizes, fix_coordinates=False):
    tokens = 0
    for a, c, b, d, x, y in prizes:
        if fix_coordinates:
            x += 10**13
            y += 10**13

        det = a * d - b * c
        n = d * x - b * y
        m = -c * x + a * y
        if n % det == m % det == 0:
            tokens += 3 * n // det + m // det
    return tokens


def main(filename):
    regexes = [
        r"Button A: X\+(\d+), Y\+(\d+)",
        r"Button B: X\+(\d+), Y\+(\d+)",
        r"Prize: X=(\d+), Y=(\d+)",
    ]
    parsed_integers = []
    with open(filename) as input_file:
        for i, line in enumerate(input_file):
            if i % 4 <= 2:
                regex = regexes[i % 4]
                parsed_integers.append(tuple(map(int, re.match(regex, line).groups())))
    # merge groups of 3 into tuples of length 6 for each prize
    prizes = [sum(batch, ()) for batch in batched(parsed_integers, 3)]

    result_part_1 = compute_tokens(prizes)
    print(f"part 1: {result_part_1}")

    result_part_2 = compute_tokens(prizes, fix_coordinates=True)
    print(f"part 2: {result_part_2}")


if __name__ == "__main__":
    for input_filename in [
        "sample.txt",
        "input.txt"
    ]:
        print(f"-- {input_filename} --")
        main(input_filename)
