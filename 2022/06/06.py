def main(filename):
    part_1_characters_count = 0
    part_2_characters_count = 0
    with open(filename) as input_file:
        line = input_file.readline()
        for i in range(len(line) - 3):
            if len(set(line[i:i + 4])) == 4:
                part_1_characters_count = i + 4
                break
        for i in range(len(line) - 13):
            if len(set(line[i:i + 14])) == 14:
                part_2_characters_count = i + 14
                break

    print(f"part 1: {part_1_characters_count}")
    print(f"part 2: {part_2_characters_count}")


if __name__ == "__main__":
    for filename in ["sample.txt", "input.txt"]:
        print(f"-- {filename} --")
        main(filename)
