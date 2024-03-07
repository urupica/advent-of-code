def main(filename):
    with open(filename) as input_file:
        rope_1 = [[0, 0], [0, 0]]
        visited_1 = {tuple(rope_1[-1])}

        rope_2 = [[0, 0] for _ in range(10)]
        visited_2 = {tuple(rope_2[-1])}
        for line in input_file:
            line = line.strip()
            direction, count = line.split()
            count = int(count)
            for _ in range(count):
                for rope in [rope_1, rope_2]:
                    if direction == "R":
                        rope[0][1] += 1
                    elif direction == "L":
                        rope[0][1] -= 1
                    elif direction == "D":
                        rope[0][0] += 1
                    else:
                        rope[0][0] -= 1

                    for i in range(len(rope) - 1):
                        if abs(rope[i][0] - rope[i + 1][0]) == 2:
                            if rope[i][0] > rope[i + 1][0]:
                                rope[i + 1][0] += 1
                            else:
                                rope[i + 1][0] -= 1
                            if rope[i][1] > rope[i + 1][1]:
                                rope[i + 1][1] += 1
                            elif rope[i][1] < rope[i + 1][1]:
                                rope[i + 1][1] -= 1

                        elif abs(rope[i][1] - rope[i + 1][1]) == 2:
                            if rope[i][1] > rope[i + 1][1]:
                                rope[i + 1][1] += 1
                            else:
                                rope[i + 1][1] -= 1
                            if rope[i][0] > rope[i + 1][0]:
                                rope[i + 1][0] += 1
                            elif rope[i][0] < rope[i + 1][0]:
                                rope[i + 1][0] -= 1

                visited_1.add(tuple(rope_1[-1]))
                visited_2.add(tuple(rope_2[-1]))

        result_part_1 = len(visited_1)
        result_part_2 = len(visited_2)

    print(f"part 1: {result_part_1}")
    print(f"part 2: {result_part_2}")


if __name__ == "__main__":
    for name in [
        "sample.txt",
        "input.txt"
    ]:
        print(f"-- {name} --")
        main(name)
