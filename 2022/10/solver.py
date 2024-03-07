def main(filename):
    result_part_1 = 0
    result_part_2 = ""
    with open(filename) as input_file:
        x = 1
        cycle = 0
        next_check = 20
        for line in input_file:
            line = line.strip()
            if line == "noop":
                if cycle + 1 == next_check:
                    result_part_1 += next_check * x
                    next_check += 40

                if abs(cycle % 40 - x) <= 1:
                    result_part_2 += "#"
                else:
                    result_part_2 += "."
                if cycle % 40 == 39:
                    result_part_2 += "\n"

                cycle += 1
            else:
                value = int(line[5:])
                if cycle + 1 == next_check or cycle + 2 == next_check:
                    result_part_1 += next_check * x
                    next_check += 40

                if abs(cycle % 40 - x) <= 1:
                    result_part_2 += "#"
                else:
                    result_part_2 += "."
                if cycle % 40 == 39:
                    result_part_2 += "\n"
                if abs((cycle + 1) % 40 - x) <= 1:
                    result_part_2 += "#"
                else:
                    result_part_2 += "."
                if (cycle + 1) % 40 == 39:
                    result_part_2 += "\n"

                cycle += 2
                x += value

    print(f"part 1: {result_part_1}")
    print(f"part 2:\n{result_part_2}")


if __name__ == "__main__":
    for name in [
        "sample.txt",
        "input.txt"
    ]:
        print(f"-- {name} --")
        main(name)
