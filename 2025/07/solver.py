def solve(filename):
    with open(filename) as input_file:
        grid = [line.strip() for line in input_file]

    # part 1
    result_part_1 = 0
    locations = {next(i for i, x in enumerate(grid[0]) if x == "S")}
    for row in grid[1:]:
        splitters = {j for j, x in enumerate(row) if x == "^"}
        if splitters:
            new_locations = set()
            for i in locations:
                if i in splitters:
                    result_part_1 += 1
                    new_locations.update({i - 1, i + 1})
                else:
                    new_locations.add(i)
            locations = new_locations
    print(f"part 1: {result_part_1}")

    # part 2
    start = next(i for i, x in enumerate(grid[0]) if x == "S")
    timelines = [0] * len(grid[0])
    timelines[start] = 1
    for row in grid[1:]:
        new_timelines = [0] * len(grid[0])
        for i, x in enumerate(row):
            if x == "^":
                new_timelines[i - 1] += timelines[i]
                new_timelines[i + 1] += timelines[i]
            else:
                new_timelines[i] += timelines[i]
        timelines = new_timelines
    result_part_2 = sum(timelines)
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
