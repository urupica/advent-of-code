def main(filename):
    with open(filename) as input_file:
        boarding_passes = [line.strip() for line in input_file]

    seat_ids = set()
    for boarding_pass in boarding_passes:
        row_encoding, col_encoding = boarding_pass[:7], boarding_pass[7:]
        row = sum(2**(6 - i) for i, x in enumerate(row_encoding) if x == "B")
        col = sum(2**(2 - i) for i, x in enumerate(col_encoding) if x == "R")
        seat_ids.add(8 * row + col)

    result_part_1 = max(seat_ids)
    result_part_2 = None
    for i in range(8, 127 * 8):
        if i not in seat_ids and i - 1 in seat_ids and i + 1 in seat_ids:
            result_part_2 = i

    print(f"part 1: {result_part_1}")
    print(f"part 2: {result_part_2}")


if __name__ == "__main__":
    for input_filename in [
        "sample.txt",
        "input.txt"
    ]:
        print(f"-- {input_filename} --")
        main(input_filename)
