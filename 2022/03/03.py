from string import ascii_lowercase, ascii_uppercase


def main(filename):
    with open(filename) as input_file:
        part_1_points = 0
        part_2_points = 0

        chars = ascii_lowercase + ascii_uppercase
        group = []
        for line in input_file:
            line = line.strip()

            # part 1
            comp1, comp2 = line[:len(line) // 2], line[len(line) // 2:]
            mult = set(comp1).intersection(comp2).pop()
            part_1_points += 1 + chars.index(mult)

            # part 2
            group.append(line)
            if len(group) == 3:
                badge = set(group[0]).intersection(group[1]).intersection(group[2]).pop()
                part_2_points += 1 + chars.index(badge)
                group = []

    print(f"part 1: {part_1_points}")
    print(f"part 2: {part_2_points}")


if __name__ == "__main__":
    for filename in ["sample.txt", "input.txt"]:
        print(f"-- {filename} --")
        main(filename)
