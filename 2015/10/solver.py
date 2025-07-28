def iterate(seq, n):
    for _ in range(n):
        seq_tmp = ""
        i = 0
        while i < len(seq):
            j = i
            while j < len(seq) and seq[i] == seq[j]:
                j += 1
            seq_tmp += f"{j - i}{seq[i]}"
            i = j
        seq = seq_tmp
    return len(seq)


def solve(filename):
    with open(filename) as input_file:
        seq = next(input_file).strip()

    result_part_1 = iterate(seq, 40)
    print(f"part 1: {result_part_1}")

    result_part_2 = iterate(seq, 50)
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
