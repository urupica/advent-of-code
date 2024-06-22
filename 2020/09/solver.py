from itertools import combinations


def main(filename):
    with open(filename) as input_file:
        numbers = [int(line) for line in input_file]

    length = {
        "sample.txt": 5,
        "input.txt": 25,
    }[filename]
    result_part_1 = None
    for i, n in enumerate(numbers[length:], start=length):
        if all(a == b or a + b != n for a, b in combinations(numbers[i - length:i], 2)):
            result_part_1 = n
    print(f"part 1: {result_part_1}")

    result_part_2 = None
    for i in range(len(numbers) - 1):
        j = i + 2
        partial_sum = numbers[i] + numbers[i + 1]
        while partial_sum < result_part_1:
            partial_sum += numbers[j]
            j += 1
        if partial_sum == result_part_1:
            result_part_2 = min(numbers[i:j]) + max(numbers[i:j])
    print(f"part 2: {result_part_2}")


if __name__ == "__main__":
    for input_filename in [
        "sample.txt",
        "input.txt",
    ]:
        print(f"-- {input_filename} --")
        main(input_filename)
