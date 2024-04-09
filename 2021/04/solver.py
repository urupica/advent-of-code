def main(filename):
    with open(filename) as input_file:
        lines = input_file.readlines()
        numbers = lines.pop(0).strip().split(",")
        boards = []
        for i in range(len(lines) // 6):
            boards.append([line.strip().split() for line in lines[6 * i + 1:6 * (i + 1)]])

    result_part_1 = None
    result_part_2 = None
    boards_won = [False for _ in range(len(boards))]
    for number in numbers:
        for k, board in enumerate(boards):
            if boards_won[k]:
                continue
            for row in board:
                while number in row:
                    row[row.index(number)] = None
            if any(all(x is None for x in row) for row in board) or any(all(row[i] is None for row in board) for i in range(5)):
                boards_won[k] = True
                result = sum(int(x) for row in board for x in row if x is not None) * int(number)
                if result_part_1 is None:
                    result_part_1 = result
                if all(boards_won):
                    result_part_2 = result
                    break
        if all(boards_won):
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
