def checksum_after_moving_blocks(disk_map):
    expanded_disk_map = []
    for i, x in enumerate(disk_map):
        if i % 2 == 0:
            expanded_disk_map.extend([i // 2] * int(x))
        else:
            expanded_disk_map.extend([None] * int(x))

    empty_positions = [i for i, x in enumerate(expanded_disk_map) if x is None]
    while empty_positions:
        x = expanded_disk_map.pop()
        if x is None:
            empty_positions.pop()
        else:
            expanded_disk_map[empty_positions[0]] = x
            empty_positions.pop(0)

    return sum(i * x for i, x in enumerate(expanded_disk_map))


def checksum_after_moving_files(disk_map):
    blocks = []
    for i, x in enumerate(disk_map):
        if i % 2 == 0:
            blocks.append((i // 2, int(x), False))
        else:
            blocks.append((None, int(x)))

    i = len(blocks) - 1
    while i > 0:
        if blocks[i][0] is not None and blocks[i][2] is False:
            value, length, _ = blocks[i]
            for j in range(i):
                if blocks[j][0] is None and blocks[j][1] >= length:
                    length_diff = blocks[j][1] - length
                    blocks[j] = (value, length, True)
                    if length_diff > 0:
                        blocks.insert(j + 1, (None, length_diff))
                        i += 1
                    blocks[i] = (None, length)
                    break
        i -= 1

    checksum = 0
    i = 0
    for value, length, *_ in blocks:
        if value is not None:
            for j in range(i, i + length):
                checksum += value * j
        i += length

    return checksum


def main(filename):
    with open(filename) as input_file:
        disk_map = input_file.readline().strip()

    result_part_1 = checksum_after_moving_blocks(disk_map)
    print(f"part 1: {result_part_1}")

    result_part_2 = checksum_after_moving_files(disk_map)
    print(f"part 2: {result_part_2}")


if __name__ == "__main__":
    for input_filename in [
        "sample.txt",
        "input.txt"
    ]:
        print(f"-- {input_filename} --")
        main(input_filename)
