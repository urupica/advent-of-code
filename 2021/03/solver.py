from collections import Counter


def main(filename):
    with open(filename) as input_file:
        report = [line.strip() for line in input_file]
    bit_length = len(report[0])

    # part 1
    counter = [Counter(row[i] for row in report) for i in range(bit_length)]
    gamma = "".join(max(counter_position, key=counter_position.get) for counter_position in counter)
    epsilon = "".join(min(counter_position, key=counter_position.get) for counter_position in counter)
    result_part_1 = int(gamma, 2) * int(epsilon, 2)
    print(f"part 1: {result_part_1}")

    # part 2
    oxygen_candidates = list(report)
    co2_candidates = list(report)
    for i in range(bit_length):
        if len(oxygen_candidates) > 1:
            counter_position = Counter(row[i] for row in oxygen_candidates)
            if counter_position.get("1", 0) >= counter_position.get("0", 0):
                oxygen_candidates = [row for row in oxygen_candidates if row[i] == "1"]
            else:
                oxygen_candidates = [row for row in oxygen_candidates if row[i] == "0"]
        if len(co2_candidates) > 1:
            counter_position = Counter(row[i] for row in co2_candidates)
            if counter_position.get("0", 0) <= counter_position.get("1", 0):
                co2_candidates = [row for row in co2_candidates if row[i] == "0"]
            else:
                co2_candidates = [row for row in co2_candidates if row[i] == "1"]
    result_part_2 = int(oxygen_candidates[0], 2) * int(co2_candidates[0], 2)
    print(f"part 2: {result_part_2}")


if __name__ == "__main__":
    for input_filename in [
        "sample.txt",
        "input.txt"
    ]:
        print(f"-- {input_filename} --")
        main(input_filename)
