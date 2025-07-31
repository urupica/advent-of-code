from math import log


def find_lowest_hose_number(min_presents, part):
    houses = [0] * 10**(max(1, int(log(min_presents, 10)) - 1))
    for i in range(1, len(houses)):
        upper = len(houses)
        if part == 2:
            upper = min(upper, 50 * i)
        for j in range(i, upper, i):
            houses[j] += i * (10 if part == 1 else 11)
    return next(i for i, n in enumerate(houses) if n >= min_presents)


def solve(filename):
    with open(filename) as input_file:
        presents = int(next(input_file).strip())

    result_part_1 = find_lowest_hose_number(presents, 1)
    print(f"part 1: {result_part_1}")

    result_part_2 = find_lowest_hose_number(presents, 2)
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
