def get_next_cell(direction, rows, cols, i, j):
    if direction == ">":
        i_next, j_next = i, (j + 1) % cols
    else:
        i_next, j_next = (i + 1) % rows, j
    return i_next, j_next


def move(grid):
    rows = len(grid)
    cols = len(grid[0])

    has_moved = False
    for direction in [">", "v"]:
        will_move = []
        for i in range(rows):
            for j in range(cols):
                i_next, j_next = get_next_cell(direction, rows, cols, i, j)
                if grid[i][j] == direction and grid[i_next][j_next] == ".":
                    will_move.append((i, j))
        for i, j in will_move:
            i_next, j_next = get_next_cell(direction, rows, cols, i, j)
            grid[i][j] = "."
            grid[i_next][j_next] = direction
        has_moved |= bool(will_move)

    return has_moved


def main(filename):
    with open(filename) as input_file:
        grid = [list(line.strip()) for line in input_file]

    moves = 0
    while True:
        moves += 1
        has_moved = move(grid)
        if not has_moved:
            break

    result_part_1 = moves
    print(f"part 1: {result_part_1}")


if __name__ == "__main__":
    for input_filename in [
        "sample.txt",
        "input.txt"
    ]:
        print(f"-- {input_filename} --")
        main(input_filename)
