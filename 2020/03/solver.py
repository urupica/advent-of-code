def main(filename):
    with open(filename) as input_file:
        grid = [line.strip() for line in input_file]

    rows = len(grid)
    cols = len(grid[0])

    result_part_1 = None
    result_part_2 = 1
    for right, down in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
        count_trees = 0
        for i in range(1, rows):
            if down * i >= rows:
                break
            if grid[down * i][(right * i) % cols] == "#":
                count_trees += 1
        if right == 3 and down == 1:
            result_part_1 = count_trees
        result_part_2 *= count_trees

    print(f"part 1: {result_part_1}")
    print(f"part 2: {result_part_2}")


if __name__ == "__main__":
    for input_filename in [
        "sample.txt",
        "input.txt"
    ]:
        print(f"-- {input_filename} --")
        main(input_filename)
