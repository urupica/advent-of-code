def main(filename):
    with open(filename) as input_file:
        board = [line.strip() for line in input_file]

    start = board[0].index(".")
    end = board[-1].index(".")
    rows = len(board)
    cols = len(board[0])
    blizzards = {(i, j): [] for i in range(rows) for j in range(cols)}
    for i in range(rows):
        for j in range(cols):
            if board[i][j] in "<>v^":
                blizzards[(i, j)].append(board[i][j])

    step = 0
    pool = {(0, start)}
    start_visited = end_visited = False
    while True:
        step += 1

        blizzards_current = [(i, j, list(directions)) for (i, j), directions in blizzards.items() if directions]
        for i, j, directions in blizzards_current:
            for d in directions:
                if d == ">":
                    if j + 1 < cols - 1:
                        blizzards[(i, j + 1)].append(">")
                    else:
                        blizzards[i, 1].append(">")
                elif d == "<":
                    if j - 1 > 0:
                        blizzards[(i, j - 1)].append("<")
                    else:
                        blizzards[i, cols - 2].append("<")
                elif d == "v":
                    if i + 1 < rows - 1:
                        blizzards[(i + 1, j)].append("v")
                    else:
                        blizzards[1, j].append("v")
                else:
                    assert d == "^"
                    if i - 1 > 0:
                        blizzards[(i - 1, j)].append("^")
                    else:
                        blizzards[rows - 2, j].append("^")
                blizzards[(i, j)].remove(d)

        pool_next = set()
        for i, j in pool:
            for ii, jj in [(i, j), (i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if 0 <= ii < rows and 0 <= jj < cols and not blizzards[(ii, jj)] and board[ii][jj] != "#":
                    pool_next.add((ii, jj))
        pool = pool_next

        if (rows - 1, end) in pool and not start_visited and not end_visited:
            end_visited = True
            result_part_1 = step
            pool = {(rows - 1, end)}
        elif (0, start) in pool and end_visited and not start_visited:
            start_visited = True
            pool = {(0, start)}
        elif (rows - 1, end) in pool and end_visited and start_visited:
            result_part_2 = step
            break

    print(f"part 1: {result_part_1}")
    print(f"part 2: {result_part_2}")


if __name__ == "__main__":
    for input_filename in [
        "sample.txt",
        "input.txt"
    ]:
        print(f"-- {input_filename} --")
        main(input_filename)
