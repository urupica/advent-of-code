from functools import cache


@cache
def is_possible(patterns, design):
    if not design:
        return True

    return any(
        is_possible(patterns, design[len(pattern):])
        for pattern in patterns
        if design.startswith(pattern)
    )

@cache
def count_possible(patterns, design):
    if not design:
        return 1

    return sum(
        count_possible(patterns, design[len(pattern):])
        for pattern in patterns
        if design.startswith(pattern)
    )

def main(filename):
    with open(filename) as input_file:
        pattern_data, design_data = input_file.read().strip().split("\n\n")

    patterns = tuple(pattern_data.split(", "))
    designs = design_data.split("\n")

    result_part_1 = sum(is_possible(patterns, design) for design in designs)
    print(f"part 1: {result_part_1}")

    result_part_2 = sum(count_possible(patterns, design) for design in designs)
    print(f"part 2: {result_part_2}")


if __name__ == "__main__":
    for input_filename in [
        "sample.txt",
        "input.txt"
    ]:
        print(f"-- {input_filename} --")
        main(input_filename)
