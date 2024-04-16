import heapq


def main(filename):
    with open(filename) as input_file:
        grid = [list(map(int, line.strip())) for line in input_file]

    for part in [1, 2]:
        if part == 2:
            for i in range(len(grid)):
                row = grid[i]
                row_length = len(row)
                for _ in range(4):
                    row_extension = list(row[-row_length:])
                    for j in range(row_length):
                        row_extension[j] = row_extension[j] + 1 if row_extension[j] + 1 <= 9 else 1
                    row.extend(row_extension)

            rows_count = len(grid)
            row_length = len(grid[0])
            for _ in range(4 * rows_count):
                new_row = list(grid[-rows_count])
                for i in range(row_length):
                    new_row[i] = new_row[i] + 1 if new_row[i] + 1 <= 9 else 1
                grid.append(new_row)

        visited = set()
        max_dist = sum(sum(row) for row in grid)
        dist = {(i, j): max_dist for i in range(len(grid)) for j in range(len(grid[0]))}
        dist[(0, 0)] = 0
        heap = [(0, (0, 0))]
        while True:
            d, (i, j) = heapq.heappop(heap)

            if i == len(grid) - 1 and j == len(grid[0]) - 1:
                result_part_1 = d
                break

            visited.add((i, j))
            for ii, jj in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if 0 <= ii < len(grid) and 0 <= jj < len(grid[0]):
                    old_d = dist[(ii, jj)]
                    new_d = dist[(i, j)] + grid[ii][jj]
                    if new_d < old_d:
                        if (old_d, (ii, jj)) in heap:
                            heap.remove((old_d, (ii, jj)))
                        heapq.heapify(heap)
                        heapq.heappush(heap, (new_d, (ii, jj)))
                        dist[(ii, jj)] = new_d

        print(f"part {part}: {result_part_1}")


if __name__ == "__main__":
    for input_filename in [
        "sample.txt",
        "input.txt"
    ]:
        print(f"-- {input_filename} --")
        main(input_filename)
