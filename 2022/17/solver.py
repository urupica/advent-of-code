rocks = (
    (
        (1, 1, 1, 1),
    ),
    (
        (0, 1, 0),
        (1, 1, 1),
        (0, 1, 0),
    ),
    # upside down so enumerating shows bottom to top
    (
        (1, 1, 1),
        (0, 0, 1),
        (0, 0, 1),
    ),
    (
        (1,),
        (1,),
        (1,),
        (1,),
    ),
    (
        (1, 1),
        (1, 1),
    ),
)


def simulate(jets, total_rocks):
    blocked = [set(range(7))]
    states = {}
    jet_index = 0
    rock_count = 0
    max_height = 0
    cycle_found = False
    max_height_gain_in_cycle = 0
    skipped_cycles = 0
    while rock_count < total_rocks:
        rock = rocks[rock_count % 5]
        max_height = len(blocked) - 1
        current = [2, max_height + 4]
        while True:
            jet = jets[jet_index]
            jet_index = (jet_index + 1) % len(jets)
            if jet == ">":
                if current[0] + len(rock[0]) < 7:
                    if not any(
                        current[1] + j < len(blocked) and current[0] + 1 + i in blocked[current[1] + j]
                        for j, row in enumerate(rock)
                        for i, x in enumerate(row)
                        if x == 1
                    ):
                        current[0] += 1
            else:
                if current[0] - 1 >= 0:
                    if not any(
                        current[1] + j < len(blocked) and current[0] - 1 + i in blocked[current[1] + j]
                        for j, row in enumerate(rock)
                        for i, x in enumerate(row)
                        if x == 1
                    ):
                        current[0] -= 1
            if any(
                current[1] - 1 + j < len(blocked) and current[0] + i in blocked[current[1] - 1 + j]
                for j, row in enumerate(rock)
                for i, x in enumerate(row)
                if x == 1
            ):
                for j, row in enumerate(rock):
                    while current[1] + j >= len(blocked):
                        blocked.append(set())
                    for i, x in enumerate(row):
                        if x == 1:
                            blocked[current[1] + j].add(current[0] + i)
                break
            current[1] -= 1

        rock_count += 1
        max_height = len(blocked) - 1
        if not cycle_found:
            state = [None] * 7
            j = len(blocked) - 1
            while None in state:
                for i in range(7):
                    if state[i] is None and i in blocked[j]:
                        state[i] = j
                j -= 1
            lowest = min(state)
            for i in range(7):
                state[i] -= lowest
            state += [rock_count % 5, jet_index]
            state = tuple(state)

            if state in states:
                max_height_gain_in_cycle = max_height - states[state][0]
                rocks_in_cycle = rock_count - states[state][1]
                skipped_cycles = (total_rocks - rock_count) // rocks_in_cycle
                rock_count += skipped_cycles * rocks_in_cycle
                cycle_found = True
            else:
                states[state] = (max_height, rock_count)

    return max_height + skipped_cycles * max_height_gain_in_cycle


def main(filename):
    with open(filename) as input_file:
        jets = input_file.readline().strip()

    result_part_1 = simulate(jets, 2022)
    print(f"part 1: {result_part_1}")

    result_part_2 = simulate(jets, 1_000_000_000_000)
    print(f"part 2: {result_part_2}")


if __name__ == "__main__":
    for input_filename in [
        "sample.txt",
        "input.txt"
    ]:
        print(f"-- {input_filename} --")
        main(input_filename)
