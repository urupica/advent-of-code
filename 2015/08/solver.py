def solve(filename):
    with open(filename) as input_file:
        lines = [line.strip() for line in input_file]

    result_part_1 = 0
    result_part_2 = 0
    for line in lines:
        assert len(line) >= 2 and line[0] == line[-1] == '"'
        result_part_1 += len(line)
        result_part_2 += 6 - len(line)
        line = line[1:-1]
        i = 0
        while i < len(line):
            result_part_1 -= 1
            if line[i] == "\\":
                if line[i + 1] in ['"', "\\"]:
                    i += 1
                    result_part_2 += 3
                else:
                    i += 3
                    result_part_2 += 4
            i += 1
            result_part_2 += 1

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
