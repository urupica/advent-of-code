import re


def main(filename):
    with open(filename) as input_file:
        line = input_file.read().strip()

    multiplications = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", line)
    result_part_1 = sum(int(a) * int(b) for a, b in multiplications)
    print(f"part 1: {result_part_1}")

    operations = re.findall(r"do\(\)|don't\(\)|mul\(\d{1,3},\d{1,3}\)", line)
    enabled = True
    result_part_2 = 0
    for operation in operations:
        if operation == "do()":
            enabled = True
        elif operation == "don't()":
            enabled = False
        elif enabled:
            a, b = re.search(r"mul\((\d{1,3}),(\d{1,3})\)", operation).groups()
            result_part_2 += int(a) * int(b)

    print(f"part 2: {result_part_2}")


if __name__ == "__main__":
    for input_filename in [
        "sample.txt",
        "input.txt"
    ]:
        print(f"-- {input_filename} --")
        main(input_filename)
