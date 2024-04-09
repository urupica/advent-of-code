from itertools import chain


def main(filename):
    with open(filename) as input_file:
        lines = []
        min_x = max_x = min_y = max_y = None
        for line in input_file:
            start, end = line.strip().split(" -> ")
            start_x, start_y = map(int, start.split(","))
            end_x, end_y = map(int, end.split(","))
            min_x = min(start_x, end_x, min_x if min_x is not None else start_x)
            max_x = max(start_x, end_x, max_x if max_x is not None else start_x)
            min_y = min(start_y, end_y, min_y if min_y is not None else start_y)
            max_y = max(start_y, end_y, max_y if max_y is not None else start_y)
            lines.append([start_x, start_y, end_x, end_y])

    x_length = max_x - min_x + 1
    y_length = max_y - min_y + 1
    board_1 = [[0] * x_length for _ in range(y_length)]
    board_2 = [[0] * x_length for _ in range(y_length)]
    for start_x, start_y, end_x, end_y in lines:
        if start_x == end_x:
            for y in range(min(start_y, end_y), max(start_y, end_y) + 1):
                board_1[y - min_y][start_x - min_x] += 1
                board_2[y - min_y][start_x - min_x] += 1
        elif start_y == end_y:
            for x in range(min(start_x, end_x), max(start_x, end_x) + 1):
                board_1[start_y - min_y][x - min_x] += 1
                board_2[start_y - min_y][x - min_x] += 1
        else:
            left = min((start_x, start_y), (end_x, end_y))
            right = max((start_x, start_y), (end_x, end_y))
            factor = 1 if left[1] < right[1] else -1
            length = right[0] - left[0] + 1
            for delta in range(length):
                board_2[left[1] + factor * delta - min_y][left[0] + delta - min_x] += 1

    result_part_1 = sum(x > 1 for x in chain(*board_1))
    result_part_2 = sum(x > 1 for x in chain(*board_2))
    print(f"part 1: {result_part_1}")
    print(f"part 2: {result_part_2}")


if __name__ == "__main__":
    for input_filename in [
        "sample.txt",
        "input.txt"
    ]:
        print(f"-- {input_filename} --")
        main(input_filename)
