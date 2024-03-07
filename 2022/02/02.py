def main(filename):
    with open(filename) as input_file:
        part_1_points = 0
        part_2_points = 0
        for line in input_file:
            line = line.strip()
            elf, me = line.split()

            # part 1
            i = "ABC".index(elf)
            j = "XYZ".index(me)
            if i == j:
                part_1_points += 3
            elif j == (i + 1) % 3:
                part_1_points += 6
            part_1_points += j + 1

            # part 2
            part_2_points += 1 + ((i + j + 2) % 3)
            part_2_points += 3 * j

    print(f"part 1: {part_1_points}")
    print(f"part 2: {part_2_points}")


if __name__ == "__main__":
    main("sample.txt")
    main("input.txt")
