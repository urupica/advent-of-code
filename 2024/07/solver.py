import numpy as np


def passes_test(test, numbers, additional_operator=False):
    base = 3 if additional_operator else 2
    length = len(numbers) - 1
    for mask in range(base**length):
        mask_str = np.base_repr(mask, base=base).zfill(length)
        result = numbers[0]
        for number, op in zip(numbers[1:], mask_str):
            if op == "0":
                result += number
            elif op == "1":
                result *= number
            else:
                result = int(str(result) + str(number))
            if result > test:
                break
        if result == test:
            return True
    return False


def main(filename):
    equations = []
    with open(filename) as input_file:
        for line in input_file:
            test, numbers = line.strip().split(":")
            test = int(test)
            numbers = list(map(int, numbers.split()))
            equations.append((test, numbers))

    result_part_1 = sum(test for test, numbers in equations if passes_test(test, numbers))
    print(f"part 1: {result_part_1}")

    result_part_2 = sum(test for test, numbers in equations if passes_test(test, numbers, additional_operator=True))
    print(f"part 2: {result_part_2}")


if __name__ == "__main__":
    for input_filename in [
        "sample.txt",
        "input.txt"
    ]:
        print(f"-- {input_filename} --")
        main(input_filename)
