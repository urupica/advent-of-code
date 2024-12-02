from collections import Counter


def main(filename):
    location_ids_left = []
    location_ids_right = []

    with open(filename) as input_file:
        for line in input_file:
            left, right = map(int, line.strip().split())
            location_ids_left.append(left)
            location_ids_right.append(right)

    location_ids_left.sort()
    location_ids_right.sort()

    result_part_1 = sum(abs(left - right) for left, right in zip(location_ids_left, location_ids_right))
    print(f"part 1: {result_part_1}")

    counter = Counter(location_ids_right)
    result_part_2 = sum(left * counter.get(left, 0) for left in location_ids_left)
    print(f"part 2: {result_part_2}")


if __name__ == "__main__":
    for input_filename in [
        "sample.txt",
        "input.txt"
    ]:
        print(f"-- {input_filename} --")
        main(input_filename)
