from functools import cache


@cache
def compute_wins(pos_a, pos_b, total_a=0, total_b=0, turn=0):
    if total_a >= 21:
        return 1, 0
    if total_b >= 21:
        return 0, 1

    total_wins_a = total_wins_b = 0
    for steps, count in {
        3: 1,
        4: 3,
        5: 6,
        6: 7,
        7: 6,
        8: 3,
        9: 1,
    }.items():
        if turn == 0:
            new_pos = (pos_a + steps) % 10
            wins_a, wins_b = compute_wins(new_pos, pos_b, total_a + new_pos + 1, total_b, 1)
        else:
            new_pos = (pos_b + steps) % 10
            wins_a, wins_b = compute_wins(pos_a, new_pos, total_a, total_b + new_pos + 1, 0)
        total_wins_a += count * wins_a
        total_wins_b += count * wins_b
    return total_wins_a, total_wins_b


def main(filename):
    with open(filename) as input_file:
        original_pos = [
            int(line.strip().replace(f"Player {i} starting position: ", "")) - 1
            for i, line in enumerate(input_file, start=1)
        ]

    pos = list(original_pos)
    total = [0] * 2
    k = 0
    while True:
        die = (3 * k) % 100 + 1 + (3 * k + 1) % 100 + 1 + (3 * k + 2) % 100 + 1
        k_mod_2 = k % 2
        pos[k_mod_2] = (pos[k_mod_2] + die) % 10
        total[k_mod_2] += pos[k_mod_2] + 1
        if total[k_mod_2] >= 1_000:
            result_part_1 = total[(k + 1) % 2] * (3 * (k + 1))
            break
        k += 1
    print(f"part 1: {result_part_1}")

    wins_a, wins_b = compute_wins(original_pos[0], original_pos[1])
    result_part_2 = max(wins_a, wins_b)
    print(f"part 2: {result_part_2}")


if __name__ == "__main__":
    for input_filename in [
        "sample.txt",
        "input.txt"
    ]:
        print(f"-- {input_filename} --")
        main(input_filename)
