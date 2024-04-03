def decode(s):
    d = {
        "=": -2,
        "-": -1,
        "0": 0,
        "1": 1,
        "2": 2,
    }

    return sum(d[x] * 5**(len(s) - i) for i, x in enumerate(s, start=1))


def encode(n):
    d = {
        -2: "=",
        -1: "-",
        0: "0",
        1: "1",
        2: "2"
    }

    s = ""
    if not -2 <= n <= 2:
        k = 1
        while not any(-5**k + 1 <= 2 * (n - a * 5**k) <= 5**k - 1 for a in range(-2, 3)):
            k += 1
        while k > 0:
            for a in range(-2, 3):
                if -5**k + 1 <= 2 * (n - a * 5**k) <= 5**k - 1:
                    s += d[a]
                    n -= a * 5**k
                    break
            k -= 1
    s += d[n]
    return s


def main(filename):
    with open(filename) as input_file:
        snafu_numbers = [line.strip() for line in input_file]

    snafu_sum = sum(decode(s) for s in snafu_numbers)
    result_part_1 = encode(snafu_sum)
    print(f"part 1: {result_part_1}")


if __name__ == "__main__":
    for input_filename in [
        "sample.txt",
        "input.txt"
    ]:
        print(f"-- {input_filename} --")
        main(input_filename)
