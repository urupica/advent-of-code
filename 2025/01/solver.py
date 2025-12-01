def solve(filename):
    with open(filename) as input_file:
        lines = [line.strip() for line in input_file]

    pos = 50
    result_part_1 = 0
    result_part_2 = 0
    for line in lines:
        d, n = line[0], int(line[1:])
        if d == "L":
            if n >= pos:
                result_part_2 += (n - pos) // 100 + int(pos != 0)
            pos = (pos - n) % 100
        else:
            result_part_2 += (pos + n) // 100
            pos = (pos + n) % 100
        if pos == 0:
            result_part_1 += 1

    print(f"part 1: {result_part_1}")
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
