from functools import reduce
from operator import mul

def apply_operator(operator, nums):
    if operator == "+":
        result = sum(nums)
    else:
        result = reduce(mul, nums, 1)
    return result


def solve(filename):
    with open(filename) as input_file:
        lines = [line.rstrip("\n") for line in input_file]

    result_part_1 = 0
    lines_split = [line.split() for line in lines]
    for i in range(len(lines_split[0])):
        nums = map(int, [line[i] for line in lines_split[:-1]])
        operator = lines_split[-1][i]
        result_part_1 += apply_operator(operator, nums)
    print(f"part 1: {result_part_1}")

    assert len({len(line) for line in lines}) == 1
    result_part_2 = 0
    operator = None
    nums = []
    for i in range(len(lines[0])):
        if lines[-1][i] != " ":
            if i > 0:
                result_part_2 += apply_operator(operator, nums)
            operator = lines[-1][i]
            nums = []
        num_str = "".join(line[i] for line in lines[:-1]).strip()
        if num_str:
            nums.append(int(num_str))
    result_part_2 += apply_operator(operator, nums)

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
