import re


def get_start_coordinates(board):
    i = j = 0
    while board[i][j] in " #":
        j += 1
    return i, j


def solve_part_1(board, path):
    i, j = get_start_coordinates(board)
    current_dir = "R"

    directions = "RDLU"
    for path_entry in path:
        if isinstance(path_entry, str):
            k = directions.index(current_dir)
            if path_entry == "R":
                current_dir = directions[(k + 1) % 4]
            else:
                current_dir = directions[(k - 1) % 4]
        else:
            for _ in range(path_entry):
                if current_dir == "R":
                    if j < len(board[i]) - 1 and board[i][j + 1] != " ":
                        if board[i][j + 1] == ".":
                            j += 1
                        else:
                            break
                    else:
                        next_j = 0
                        while board[i][next_j] == " ":
                            next_j += 1
                        if board[i][next_j] == ".":
                            j = next_j
                        else:
                            break
                elif current_dir == "L":
                    if j > 0 and board[i][j - 1] != " ":
                        if board[i][j - 1] == ".":
                            j -= 1
                        else:
                            break
                    else:
                        next_j = len(board[i]) - 1
                        while board[i][next_j] == " ":
                            next_j -= 1
                        if board[i][next_j] == ".":
                            j = next_j
                        else:
                            break
                elif current_dir == "D":
                    if i < len(board) - 1 and j < len(board[i + 1]) and board[i + 1][j] != " ":
                        if board[i + 1][j] == ".":
                            i += 1
                        else:
                            break
                    else:
                        next_i = 0
                        while j >= len(board[next_i]) or board[next_i][j] == " ":
                            next_i += 1
                        if board[next_i][j] == ".":
                            i = next_i
                        else:
                            break
                else:
                    if i > 0 and j < len(board[i - 1]) and board[i - 1][j] != " ":
                        if board[i - 1][j] == ".":
                            i -= 1
                        else:
                            break
                    else:
                        next_i = len(board) - 1
                        while j >= len(board[next_i]) or board[next_i][j] == " ":
                            next_i -= 1
                        if board[next_i][j] == ".":
                            i = next_i
                        else:
                            break

    result_part_1 = 1_000 * (i + 1) + 4 * (j + 1) + directions.index(current_dir)
    return result_part_1


def get_next_face_coordinates(i, j, current_dir, is_sample):
    # hardcoded after manually inspecting the input files
    if is_sample:
        if current_dir == "R":
            if i < 4:
                # edge 6 (upper)
                assert j == 11
                return 11 - i, 15, "L"
            if i < 8:
                # edge 3 (vertical)
                assert j == 11
                return 8, 15 - (i - 4), "D"
            # edge 6 (lower)
            assert 8 <= i < 12 and j == 15
            return 11 - i, 11, "L"
        if current_dir == "L":
            if i < 4:
                # edge 1 (vertical)
                assert j == 8
                return 4, 4 + i, "D"
            if i < 8:
                # edge 7 (vertical)
                assert j == 0
                return 11, 12 + (7 - i), "U"
            # edge 4 (vertical)
            assert 8 <= i < 12 and j == 8
            return 7, 4 + (11 - i), "U"
        if current_dir == "D":
            if j < 4:
                # edge 5 (left)
                assert i == 7
                return 11, 8 + i, "U"
            if j < 8:
                # edge 4 (horizontal)
                assert i == 7
                return 11 - (i - 4), 8, "R"
            if j < 12:
                # edge 5 (right)
                assert i == 11
                return 7, (11 - j), "U"
            # edge 7 (horizontal)
            assert 12 <= j < 16 and i == 11
            return 7 - (i - 12), 0, "R"
        else:
            assert current_dir == "U"
            if j < 4:
                # edge 2 (left)
                assert i == 4
                return 0, 8 + (3 - i), "D"
            if j < 8:
                # edge 1 (horizontal)
                assert i == 4
                return j - 4, 8, "R"
            if j < 12:
                # edge 2 (right)
                assert i == 0
                return 4, 3 - (i - 8), "D"
            # edge 3 (horizontal)
            assert 12 <= j < 16 and i == 8
            return 4 + (15 - i), 12, "L"
    else:
        if current_dir == "R":
            if i < 50:
                # edge 5 (upper)
                assert j == 149
                return 100 + (49 - i), 99, "L"
            if i < 100:
                # edge 3 (vertical)
                assert j == 99
                return 49, 149 - (99 - i), "U"
            if i < 150:
                # edge 5 (lower)
                assert j == 99
                return 49 - (i - 100), 149, "L"
            # edge 2 (lower)
            assert 150 <= i < 200 and j == 49
            return 149, 99 - (199 - i), "U"
        if current_dir == "L":
            if i < 50:
                # edge 4 (upper)
                assert j == 50
                return 149 - i, 0, "R"
            if i < 100:
                # edge 1 (upper)
                assert j == 50
                return 100, 49 - (99 - i), "D"
            if i < 150:
                # edge 4 (lower)
                assert j == 0
                return 149 - i, 50, "R"
            # edge 6 (vertical)
            assert 150 <= i < 200 and j == 0
            return 0, 50 + (i - 150), "D"
        if current_dir == "D":
            if j < 50:
                # edge 7 (lower)
                assert i == 199
                return 0, 149 - (49 - j), "D"
            if j < 100:
                # edge 2 (horizontal)
                assert i == 149
                return 199 - (99 - j), 49, "L"
            # edge 3 (horizontal)
            assert 100 <= j < 150 and i == 49
            return 99 - (149 - j), 99, "L"
        else:
            assert current_dir == "U"
            if j < 50:
                # edge 1 (horizontal)
                assert i == 100
                return 99 - (49 - j), 50, "R"
            if j < 100:
                # edge 6 (horizontal)
                assert i == 0
                return 150 + (j - 50), 0, "R"
            # edge 7 (upper)
            assert 100 <= j < 150 and i == 0
            return 199, 49 - (149 - j), "U"


def solve_part_2(board, path, is_sample):
    i, j = get_start_coordinates(board)
    current_dir = "R"

    directions = "RDLU"
    for path_entry in path:
        if isinstance(path_entry, str):
            k = directions.index(current_dir)
            if path_entry == "R":
                current_dir = directions[(k + 1) % 4]
            else:
                current_dir = directions[(k - 1) % 4]
        else:
            for _ in range(path_entry):
                move_to_next_face = False
                if current_dir == "R":
                    if j < len(board[i]) - 1 and board[i][j + 1] != " ":
                        if board[i][j + 1] == ".":
                            j += 1
                        else:
                            break
                    else:
                        move_to_next_face = True
                elif current_dir == "L":
                    if j > 0 and board[i][j - 1] != " ":
                        if board[i][j - 1] == ".":
                            j -= 1
                        else:
                            break
                    else:
                        move_to_next_face = True
                elif current_dir == "D":
                    if i < len(board) - 1 and j < len(board[i + 1]) and board[i + 1][j] != " ":
                        if board[i + 1][j] == ".":
                            i += 1
                        else:
                            break
                    else:
                        move_to_next_face = True
                else:
                    if i > 0 and j < len(board[i - 1]) and board[i - 1][j] != " ":
                        if board[i - 1][j] == ".":
                            i -= 1
                        else:
                            break
                    else:
                        move_to_next_face = True

                if move_to_next_face:
                    i_next, j_next, current_dir_next = get_next_face_coordinates(i, j, current_dir, is_sample)
                    assert board[i_next][j_next] in ".#"
                    if board[i_next][j_next] == "#":
                        break
                    else:
                        i, j, current_dir = i_next, j_next, current_dir_next

    result_part_2 = 1_000 * (i + 1) + 4 * (j + 1) + directions.index(current_dir)
    return result_part_2


def main(filename):
    board = []
    path = None
    with open(filename) as input_file:
        is_board = True
        for line in input_file:
            line = line.replace("\n", "")
            if is_board:
                if line:
                    board.append(line)
                else:
                    is_board = False
            else:
                path = line

    path = re.split("(R|L)", path)
    path = tuple(map(lambda x: int(x) if x not in "RL" else x, path))

    result_part_1 = solve_part_1(board, path)
    print(f"part 1: {result_part_1}")

    result_part_2 = solve_part_2(board, path, is_sample=filename == "sample.txt")
    print(f"part 2: {result_part_2}")


if __name__ == "__main__":
    for input_filename in [
        "sample.txt",
        "input.txt"
    ]:
        print(f"-- {input_filename} --")
        main(input_filename)
