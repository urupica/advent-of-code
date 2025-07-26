def solve(filename):
    with open(filename) as input_file:
        line = next(input_file)

    result_part_1 = line.count("(") - line.count(")")
    print(f"part 1: {result_part_1}")

    floor = 0
    for count, symbol in enumerate(line, start=1):
        if symbol == "(":
            floor += 1
        else:
            floor -= 1
        if floor == -1:
            print(f"part 2: {count}")
            break

def main():
    for filename in [
        "sample.txt",
        "input.txt"
    ]:
        print(f"-- {filename} --")
        solve(filename)


if __name__ == "__main__":
    main()
