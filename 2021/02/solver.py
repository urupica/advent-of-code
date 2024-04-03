def main(filename):
    commands = []
    with open(filename) as input_file:
        for line in input_file:
            parts = line.strip().split()
            commands.append((parts[0], int(parts[1])))

    horizontal = 0
    depth = 0
    for direction, value in commands:
        if direction == "forward":
            horizontal += value
        elif direction == "down":
            depth += value
        else:
            depth -= value
    result_part_1 = horizontal * depth
    print(f"part 1: {result_part_1}")

    horizontal = 0
    depth = 0
    aim = 0
    for direction, value in commands:
        if direction == "forward":
            horizontal += value
            depth += aim * value
        elif direction == "down":
            aim += value
        else:
            aim -= value
    result_part_2 = horizontal * depth
    print(f"part 2: {result_part_2}")


if __name__ == "__main__":
    for input_filename in [
        "sample.txt",
        "input.txt"
    ]:
        print(f"-- {input_filename} --")
        main(input_filename)
