from collections import defaultdict


def main(filename):
    grid = []
    with open(filename) as input_file:
        for line in input_file:
            grid.append(list(map(int, line.strip())))

    # part 1
    column_count = len(grid[0])
    row_count = len(grid)
    result_part_1 = 2 * column_count + 2 * (row_count - 2)

    left_trees = [defaultdict(int) for _ in range(row_count)]
    right_trees = [defaultdict(int) for _ in range(row_count)]
    top_trees = [defaultdict(int) for _ in range(column_count)]
    botton_trees = [defaultdict(int) for _ in range(column_count)]

    for i in range(row_count):
        for j in range(column_count):
            height = grid[i][j]
            right_trees[i][height] += 1
            botton_trees[j][height] += 1

    for i in range(row_count):
        for j in range(column_count):
            height = grid[i][j]
            right_trees[i][height] -= 1
            if right_trees[i][height] == 0:
                del right_trees[i][height]
            botton_trees[j][height] -= 1
            if botton_trees[j][height] == 0:
                del botton_trees[j][height]

            if 0 < i < row_count - 1 and 0 < j < column_count - 1:
                if height > min(max(left_trees[i]), max(right_trees[i]), max(top_trees[j]), max(botton_trees[j])):
                    result_part_1 += 1

            left_trees[i][height] += 1
            top_trees[j][height] += 1

    # part 2
    result_part_2 = 0
    for i in range(1, row_count - 1):
        for j in range(1, column_count - 1):
            height = grid[i][j]

            up = 0
            for ii in range(i - 1, -1, -1):
                up += 1
                if grid[ii][j] >= height:
                    break
            down = 0
            for ii in range(i + 1, row_count):
                down += 1
                if grid[ii][j] >= height:
                    break
            left = 0
            for jj in range(j - 1, -1, -1):
                left += 1
                if grid[i][jj] >= height:
                    break
            right = 0
            for jj in range(j + 1, column_count):
                right += 1
                if grid[i][jj] >= height:
                    break

            total = up * down * left * right
            result_part_2 = max(result_part_2,  total)

    print(f"part 1: {result_part_1}")
    print(f"part 2: {result_part_2}")


if __name__ == "__main__":
    for filename in [
        "sample.txt",
        "input.txt"
    ]:
        print(f"-- {filename} --")
        main(filename)
