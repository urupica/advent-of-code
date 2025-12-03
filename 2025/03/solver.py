def find_best(banks, batteries):
    result = 0
    for bank in banks:
        bank_rev = bank[::-1]
        l = len(bank)
        best = [[None] * j + [j] * (l - j) for j in range(batteries)]
        for i in range(1, l):
            for j in range(min(i, batteries)):
                if bank_rev[i] >= bank_rev[best[j][i - 1]]:
                    best[j][i] = i
                else:
                    best[j][i] = best[j][i - 1]

        cur = l - 1
        best_digits = []
        for j in range(batteries - 1, -1, -1):
            best_digits.append(bank_rev[best[j][cur]])
            cur = best[j][cur] - 1
        result += int("".join(map(str, best_digits)))
    return result


def solve(filename):
    with open(filename) as input_file:
        banks = [list(map(int, line.strip())) for line in input_file]

    result_part_1 = find_best(banks, 2)
    result_part_2 = find_best(banks, 12)

    print(f"part 1: {result_part_1}")
    print(f"part 2: {result_part_2}")


def main():
    for filename in [
        "sample.txt",
        "input.txt"
    ]:
        print(f"-- {filename} --")
        solve(filename)


if __name__ == "__main__":
    main()
