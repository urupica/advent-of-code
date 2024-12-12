from functools import cache

@cache
def stones_after_k_steps(n, k):
    if k == 0:
        return 1

    if n == "0":
        return stones_after_k_steps("1", k - 1)
    elif len(n) % 2 == 0:
        m = len(n) // 2
        return stones_after_k_steps(n[:m], k - 1) + stones_after_k_steps(str(int(n[m:])), k - 1)
    else:
        return stones_after_k_steps(str(int(n) * 2024), k - 1)


def main(filename):
    with open(filename) as input_file:
        stones = input_file.readline().strip().split()

    result_part_1 = sum(stones_after_k_steps(n, 25) for n in stones)
    print(f"part 1: {result_part_1}")

    result_part_2 = sum(stones_after_k_steps(n, 75) for n in stones)
    print(f"part 2: {result_part_2}")


if __name__ == "__main__":
    for input_filename in [
        "sample.txt",
        "input.txt"
    ]:
        print(f"-- {input_filename} --")
        main(input_filename)
