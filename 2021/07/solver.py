from collections import Counter


def main(filename):
    with open(filename) as input_file:
        positions = list(map(int, input_file.readline().strip().split(",")))

    counter = Counter(positions)
    pos = min(positions)
    total_fuel_1 = sum(abs(x - pos) * n for x, n in counter.items())
    total_fuel_2 = sum(abs(x - pos) * (abs(x - pos) + 1) * n // 2 for x, n in counter.items())
    keep_searching_1 = keep_searching_2 = True
    while keep_searching_1 or keep_searching_2:
        pos += 1
        if keep_searching_1:
            total_fuel_1_next = sum(abs(x - pos) * n for x, n in counter.items())
            if total_fuel_1_next < total_fuel_1:
                total_fuel_1 = total_fuel_1_next
            else:
                keep_searching_1 = False
        if keep_searching_2:
            total_fuel_2_next = sum(abs(x - pos) * (abs(x - pos) + 1) * n // 2 for x, n in counter.items())
            if total_fuel_2_next < total_fuel_2:
                total_fuel_2 = total_fuel_2_next
            else:
                keep_searching_2 = False

    print(f"part 1: {total_fuel_1}")
    print(f"part 2: {total_fuel_2}")


if __name__ == "__main__":
    for input_filename in [
        "sample.txt",
        "input.txt"
    ]:
        print(f"-- {input_filename} --")
        main(input_filename)
