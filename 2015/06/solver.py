import re

def solve(filename):
    commands = []
    with open(filename) as input_file:
        for line in input_file:
            line = line.strip()
            result = re.match(r"(turn on|turn off|toggle) (\d{1,3}),(\d{1,3}) through (\d{1,3}),(\d{1,3})", line)
            command, *coordinates = result.groups()
            commands.append((command,) + tuple(map(int, coordinates)))

    size = 1_000
    grid = [[0] * size for _ in range(size)]
    for command, a, b, c, d  in commands:
        assert a <= c and b <= d
        for x in range(a, c + 1):
            for y in range(b, d + 1):
                if command == "turn on":
                    grid[x][y] = 1
                elif command == "turn off":
                    grid[x][y] = 0
                else:
                    grid[x][y] = (grid[x][y] + 1) % 2

    result_part_1 = sum(sum(row) for row in grid)
    print(f"part 1: {result_part_1}")

    grid = [[0] * size for _ in range(size)]
    for command, a, b, c, d  in commands:
        for x in range(a, c + 1):
            for y in range(b, d + 1):
                if command == "turn on":
                    grid[x][y] += 1
                elif command == "turn off":
                    grid[x][y] = max(grid[x][y] - 1, 0)
                else:
                    grid[x][y] += 2

    result_part_2 = sum(sum(row) for row in grid)
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
