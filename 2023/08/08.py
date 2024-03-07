import numpy as np

def main1():
    with open("input.txt") as input_file:
        directions = input_file.readline().strip()
        input_file.readline()

        destinations = {}
        for row in input_file:
            source, targets = [part.strip() for part in row.strip().split("=")]
            targets = [part.strip() for part in targets[1:-1].split(",")]
            destinations[source] = {"L": targets[0], "R": targets[1]}

    current = "AAA"
    steps = 0
    while current != "ZZZ":
        for direction in directions:
            current = destinations[current][direction]
            steps += 1
            if current == "ZZZ":
                break

    print(steps)


mem = {}


def main2():
    def get_next_z(node, index):
        if (node, index) not in mem:
            is_first_loop = True
            current = node
            current_index = index
            steps = 0
            while is_first_loop or not current.endswith("Z"):
                current = destinations[current][directions[current_index]]
                current_index = (current_index + 1) % len(directions)
                steps += 1
                is_first_loop = False
            mem[(node, index)] = (current, steps)
        print(node, index, mem[(node, index)])
        return mem[(node, index)]

    with open("input.txt") as input_file:
        directions = input_file.readline().strip()
        input_file.readline()

        destinations = {}
        for row in input_file:
            source, targets = [part.strip() for part in row.strip().split("=")]
            targets = [part.strip() for part in targets[1:-1].split(",")]
            destinations[source] = dict(zip("LR", targets))

    start_positions = [pos for pos in destinations if pos.endswith("A")]

    counters = {}
    for start in start_positions:
        current = start

        steps = 0
        while not current.endswith("Z"):
            for direction in directions:
                current = destinations[current][direction]
                steps += 1
                if current.endswith("Z"):
                    break
        counters[start] = (current, steps, steps % len(directions), steps / len(directions))

    print(counters)

    while len({val[1] for val in counters.values()}) > 1:
        start = min(counters, key=lambda x: counters[x][1])
        current, steps, index, _ = counters[start]
        current_2, steps_z = get_next_z(current, index)
        counters[start] = (current_2, steps + steps_z, (steps + steps_z) % len(directions), (steps + steps_z) / len(directions))
        print(counters)

    print([val[1] for val in counters.values()][0])


def main3():
    with open("input.txt") as input_file:
        directions = input_file.readline().strip()
        input_file.readline()

        destinations = {}
        for row in input_file:
            source, targets = [part.strip() for part in row.strip().split("=")]
            targets = [part.strip() for part in targets[1:-1].split(",")]
            destinations[source] = dict(zip("LR", targets))

    start_positions = [pos for pos in destinations if pos.endswith("A")]

    all_steps = []
    for start in start_positions:
        steps = 0
        while not start.endswith("Z"):
            for direction in directions:
                start = destinations[start][direction]
                steps += 1
                if start.endswith("Z"):
                    break
        all_steps.append(steps)
    print(np.lcm.reduce(all_steps))


if __name__ == "__main__":
    main3()
