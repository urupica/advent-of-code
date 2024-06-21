import re

# improved solution based on https://www.reddit.com/r/adventofcode/comments/rnejv5/comment/hps5hgw/


INSTRUCTIONS = r"""inp w
mul x 0
add x z
mod x 26
div z (\d+)
add x (-?\d+)
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y (-?\d+)
mul y x
add z y""".split("\n")


def main(filename):
    a_stats = {1: 0, 26: 0}
    z_blocks = []
    conditions = []
    with open(filename) as input_file:
        lines = [line.strip() for line in input_file]
        assert len(lines) == 14 * len(INSTRUCTIONS)
        for i in range(14):
            a = b = c = None
            for j, (line, pattern) in enumerate(zip(lines[i * len(INSTRUCTIONS):(i + 1) * len(INSTRUCTIONS)], INSTRUCTIONS)):
                result = re.match(pattern, line)
                assert result
                if j == 4:
                    a = int(result.group(1))
                    assert a in [1, 26]
                elif j == 5:
                    b = int(result.group(1))
                    assert -16 <= b <= 16
                elif j == 15:
                    c = int(result.group(1))
                    assert -16 <= c <= 16
            if a == 1:
                assert 10 <= b <= 16
            a_stats[a] += 1
            assert a_stats[1] >= a_stats[26]
            if a == 1:
                z_blocks.append((i, c))
            else:
                var, n = z_blocks.pop()
                conditions.append((var, n + b, i))
    assert a_stats == {1: 7, 26: 7}

    max_digits = [None] * 14
    min_digits = [None] * 14
    for var1, n, var2 in conditions:
        if n >= 0:
            max_digits[var1] = 9 - n
            max_digits[var2] = 9
            min_digits[var1] = 1
            min_digits[var2] = 1 + n
        else:
            max_digits[var1] = 9
            max_digits[var2] = 9 + n
            min_digits[var1] = 1 - n
            min_digits[var2] = 1
    result_part_1 = int("".join(map(str, max_digits)))
    result_part_2 = int("".join(map(str, min_digits)))

    print(f"part 1: {result_part_1}")
    print(f"part 2: {result_part_2}")


if __name__ == "__main__":
    main("input.txt")
