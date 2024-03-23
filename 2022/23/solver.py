from collections import defaultdict


def simulate(board, limit_rounds=None, run_until_no_elf_moves=False):
    directions = [
        tuple((-1, j) for j in range(-1, 2)),  # north
        tuple((1, j) for j in range(-1, 2)),  # south
        tuple((i, -1) for i in range(-1, 2)),  # west
        tuple((i, 1) for i in range(-1, 2)),  # east
    ]
    all_directions = tuple((i, j) for i in range(-1, 2) for j in range(-1, 2) if not i == j == 0)

    round_count = 0
    while True:
        # extend board if necessary
        if "#" in board[0]:
            board.insert(0, ["."] * len(board[0]))
        if "#" in board[-1]:
            board.append(["."] * len(board[0]))
        if "#" in [row[0] for row in board]:
            for row in board:
                row.insert(0, ".")
        if "#" in [row[-1] for row in board]:
            for row in board:
                row.append(".")

        proposed_moves = defaultdict(list)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "#":
                    if not any(
                        board[i + ii][j + jj] == "#"
                        for ii, jj in all_directions
                        if 0 <= i + ii < len(board) and 0 <= j + jj < len(board[0])
                    ):
                        continue
                    for direction_coordinates in directions:
                        if not any(
                            board[i + ii][j + jj] == "#"
                            for ii, jj in direction_coordinates
                            if 0 <= i + ii < len(board) and 0 <= j + jj < len(board[0])
                        ):
                            ii, jj = direction_coordinates[1]
                            proposed_moves[(i + ii, j + jj)].append((i, j))
                            break

        no_elf_moved = True
        for target_coordinates, elves_coordinates in proposed_moves.items():
            if len(elves_coordinates) == 1:
                i, j = elves_coordinates[0]
                ii, jj = target_coordinates
                board[i][j] = "."
                board[ii][jj] = "#"
                no_elf_moved = False

        directions.append(directions.pop(0))

        round_count += 1
        if round_count == limit_rounds:
            break

        if run_until_no_elf_moves and no_elf_moved:
            return round_count

    # crop board if necessary
    while "#" not in board[0]:
        board.pop(0)
    while "#" not in board[-1]:
        board.pop()
    while "#" not in [row[0] for row in board]:
        for row in board:
            row.pop(0)
    while "#" not in [row[-1] for row in board]:
        for row in board:
            row.pop()

    return sum(board[i][j] == "." for i in range(len(board)) for j in range(len(board[0])))


def main(filename):
    board_orig = ()
    with open(filename) as input_file:
        for line in input_file:
            board_orig += (tuple(line.strip()),)

    board = [list(row) for row in board_orig]
    result_part_1 = simulate(board, limit_rounds=10)
    print(f"part 1: {result_part_1}")

    board = [list(row) for row in board_orig]
    result_part_2 = simulate(board, run_until_no_elf_moves=True)
    print(f"part 2: {result_part_2}")


if __name__ == "__main__":
    for input_filename in [
        "sample.txt",
        "input.txt"
    ]:
        print(f"-- {input_filename} --")
        main(input_filename)
