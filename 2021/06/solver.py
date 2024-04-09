from collections import Counter


def main(filename):
    with open(filename) as input_file:
        fish = {
            **{day: 0 for day in range(9)},
            **Counter(map(int, input_file.readline().strip().split(","))),
        }

    for counter in range(256):
        zeroes = fish[0]
        for n in range(1, 9):
            fish[n - 1] = fish[n]
        fish[6] += zeroes
        fish[8] = zeroes
        if counter == 79:
            result_part_1 = sum(fish.values())
    result_part_2 = sum(fish.values())

    print(f"part 1: {result_part_1}")
    print(f"part 2: {result_part_2}")


if __name__ == "__main__":
    for input_filename in [
        "sample.txt",
        "input.txt"
    ]:
        print(f"-- {input_filename} --")
        main(input_filename)
