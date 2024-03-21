def simulate(orig, multiplier=1, rounds=1):
    pos = [[n * multiplier, i] for n, i in orig]
    length = len(pos)
    for _ in range(rounds):
        for k in range(length):
            n, i = pos[k]
            if n != 0:
                if n > 0:
                    j = (i + n) % (length - 1)
                else:
                    j = (i + n - 1) % (length - 1) + 1
                if i != j:
                    pos[k][1] = j
                    for kk in range(length):
                        if kk != k:
                            if i < pos[kk][1] <= j:
                                pos[kk][1] -= 1
                            elif j <= pos[kk][1] < i:
                                pos[kk][1] += 1

    zero_index = [i for n, i in orig if n == 0][0]
    k = pos[zero_index][1]
    return sum(n for n, i in pos if any((k + x) % length == i for x in [1_000, 2_000, 3_000]))


def main(filename):
    with open(filename) as input_file:
        orig = tuple((n, i) for i, n in enumerate(map(int, (line.strip() for line in input_file))))

    result_part_1 = simulate(orig)
    print(f"part 1: {result_part_1}")

    result_part_2 = simulate(orig, multiplier=811589153, rounds=10)
    print(f"part 2: {result_part_2}")

    if filename == "sample.txt":
        assert result_part_1 == 3
        assert result_part_2 == 1623178306
    else:
        assert result_part_1 == 3700
        assert result_part_2 == 10626948369382


if __name__ == "__main__":
    for input_filename in [
        "sample.txt",
        "input.txt"
    ]:
        print(f"-- {input_filename} --")
        main(input_filename)
