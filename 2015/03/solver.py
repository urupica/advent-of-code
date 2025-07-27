def get_new_position(position, direction):
    if direction == ">":
        return position[0] + 1, position[1]
    elif direction == "<":
        return position[0] - 1, position[1]
    elif direction == "v":
        return position[0], position[1] + 1
    else:
        return position[0], position[1] - 1


def solve(filename):
    with open(filename) as input_file:
        line = next(input_file).strip()

    position = (0, 0)
    seen = {position}
    for direction in line:
        position = get_new_position(position, direction)
        seen.add(position)
    result_part_1 = len(seen)
    print(f"part 1: {result_part_1}")

    position_a = position_b = (0, 0)
    seen = {position_a, position_b}
    for i, direction in enumerate(line):
        if i % 2 == 0:
            position_a = get_new_position(position_a, direction)
            seen.add(position_a)
        else:
            position_b = get_new_position(position_b, direction)
            seen.add(position_b)
    result_part_2 = len(seen)
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
