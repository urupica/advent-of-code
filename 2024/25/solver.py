def solve(filename):
    locks = []
    keys = []
    with open(filename) as input_file:
        sections = input_file.read().split("\n\n")
        for section in sections:
            lines = [line.strip() for line in section.split("\n")]
            heights = [[lines[i][j] for i in range(1, 6)].count("#") for j in range(5)]
            if lines[0] == "#####":
                locks.append(heights)
            else:
                keys.append(heights)

    result_part_1 = sum(
        all(a + b <= 5 for a, b in zip(lock, key))
        for lock in locks
        for key in keys
    )
    print(f"part 1: {result_part_1}")


def main():
    for filename in [
        "sample.txt",
        "input.txt"
    ]:
        print(f"-- {filename} --")
        solve(filename)


if __name__ == "__main__":
    main()
