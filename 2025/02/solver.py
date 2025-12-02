def _is_invalid(n, parts=None):
    if parts == 2:
        if len(str(n)) % 2 != 0:
            return False
        k = len(str(n)) // 2
        return str(n)[:k] == str(n)[k:]

    for l in range(1, len(str(n)) // 2 + 1):
        a = str(n)[:l]
        if a * (len(str(n)) // l) == str(n):
            return True
    return False




def solve(filename):
    with open(filename) as input_file:
        line = input_file.readline()
        ranges = [tuple(map(int, part.split("-"))) for part in line.split(",")]

    result_part_1 = 0
    result_part_2 = 0
    for l, u in ranges:
        for n in range(l, u + 1):
            if _is_invalid(n, parts=2):
                result_part_1 += n
            if _is_invalid(n):
                result_part_2 += n

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
