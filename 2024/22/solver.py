from collections import defaultdict


def get_next(number):
    number = ((number * 64) ^ number) % 16777216
    number = ((number // 32) ^ number) % 16777216
    number = ((number * 2048) ^ number) % 16777216
    return number


def solve(filename):
    with open(filename) as input_file:
        numbers = [int(line) for line in input_file]

    n = len(numbers)
    ones_prev = [None] * n
    ones = [number % 10 for number in numbers]
    diffs = [() for _ in range(n)]
    for i in range(n):
        for _ in range(3):
            ones_prev[i] = ones[i]
            numbers[i] = get_next(numbers[i])
            ones[i] = numbers[i] % 10
            diffs[i] += (ones[i] - ones_prev[i],)

    seen = [set() for _ in range(n)]
    stats = defaultdict(int)
    for _ in range(1_997):
        for i in range(n):
            ones_prev[i] = ones[i]
            numbers[i] = get_next(numbers[i])
            ones[i] = numbers[i] % 10
            diffs[i] = diffs[i][-3:] + (ones[i] - ones_prev[i],)
            if diffs[i] not in seen[i]:
                stats[diffs[i]] += ones[i]
                seen[i].add(diffs[i])

    result_part_1 = sum(numbers)
    print(f"part 1: {result_part_1}")

    result_part_2 = max(stats.values())
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
