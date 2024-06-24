def main(filename):
    instructions = []
    with open(filename) as input_file:
        for line in input_file:
            line = line.strip()
            instructions.append((line[0], int(line[1:])))

    direction = "E"
    position = [0, 0]
    for action, value in instructions:
        if action == "N" or action == "F" and direction == "N":
            position[1] += value
        elif action == "S" or action == "F" and direction == "S":
            position[1] -= value
        elif action == "E" or action == "F" and direction == "E":
            position[0] += value
        elif action == "W" or action == "F" and direction == "W":
            position[0] -= value
        elif action == "L":
            assert value % 90 == 0
            direction = "NWSE"[("NWSE".index(direction) + value // 90) % 4]
        elif action == "R":
            assert value % 90 == 0
            direction = "NWSE"[("NWSE".index(direction) - value // 90) % 4]
        else:
            raise ValueError
    result_part_1 = abs(position[0]) + abs(position[1])
    print(f"part 1: {result_part_1}")

    waypoint = [10, 1]
    position = [0, 0]
    for action, value in instructions:
        if action == "N":
            waypoint[1] += value
        elif action == "S":
            waypoint[1] -= value
        elif action == "E":
            waypoint[0] += value
        elif action == "W":
            waypoint[0] -= value
        elif action == "F":
            position[0] += value * waypoint[0]
            position[1] += value * waypoint[1]
        else:
            if action == "R":
                value = -value
            value = value % 360
            if value == 90:
                waypoint[0], waypoint[1] = -waypoint[1], waypoint[0]
            elif value == 180:
                waypoint[0], waypoint[1] = -waypoint[0], -waypoint[1]
            elif value == 270:
                waypoint[0], waypoint[1] = waypoint[1], -waypoint[0]

    result_part_2 = abs(position[0]) + abs(position[1])
    print(f"part 2: {result_part_2}")


if __name__ == "__main__":
    for input_filename in [
        "sample.txt",
        "input.txt"
    ]:
        print(f"-- {input_filename} --")
        main(input_filename)
