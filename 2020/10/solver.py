from collections import defaultdict


def main(filename):
    with open(filename) as input_file:
        adapters = [int(line.strip()) for line in input_file]

    adapters.append(0)
    adapters.sort()
    adapters.append(adapters[-1] + 3)

    distribution = defaultdict(int)
    for a, b in zip(adapters[:-1], adapters[1:]):
        distribution[b - a] += 1
    result_part_1 = distribution[1] * distribution[3]
    print(f"part 1: {result_part_1}")

    count_options = {0: 1}
    for a in adapters[1:]:
        count_options[a] = sum(count_options[b] for b in [a - 1, a - 2, a - 3] if b in count_options)
    result_part_2 = count_options[adapters[-1]]
    print(f"part 2: {result_part_2}")


if __name__ == "__main__":
    for input_filename in [
        "sample.txt",
        "input.txt"
    ]:
        print(f"-- {input_filename} --")
        main(input_filename)
