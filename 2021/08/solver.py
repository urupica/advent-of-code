from itertools import chain


def main(filename):
    with open(filename) as input_file:
        displays = []
        for line in input_file:
            signal_patterns, output_values = [part.split() for part in line.strip().split(" | ")]
            displays.append((signal_patterns, output_values))

    result_part_1 = sum(
        len(value) in [2, 3, 4, 7]
        for value in chain(*[output_values for _, output_values in displays])
    )
    print(f"part 1: {result_part_1}")

    result_part_2 = 0
    for signal_patterns, output_values in displays:
        # corresponds to cf
        two_digit_pattern = set([pattern for pattern in signal_patterns if len(pattern) == 2][0])
        c_f_maps = two_digit_pattern

        # corresponds to acf
        three_digit_pattern = set([pattern for pattern in signal_patterns if len(pattern) == 3][0])
        a_map = three_digit_pattern.difference(two_digit_pattern).pop()

        # corresponds to bcdf
        four_digit_pattern = set([pattern for pattern in signal_patterns if len(pattern) == 4][0])
        b_d_maps = four_digit_pattern.difference(c_f_maps)

        # corresponds to acdfg
        three_pattern = [pattern for pattern in signal_patterns if len(pattern) == 5 and c_f_maps.issubset(pattern)][0]
        g_map = set(three_pattern).difference({a_map}.union(c_f_maps).union(b_d_maps)).pop()
        d_map = set(three_pattern).difference({a_map, g_map}.union(c_f_maps)).pop()
        b_map = b_d_maps.difference(d_map).pop()

        # corresponds to abcefg
        zero_pattern = [pattern for pattern in signal_patterns if len(pattern) == 6 and d_map not in pattern][0]
        e_map = set(zero_pattern).difference({a_map, b_map, g_map}.union(c_f_maps)).pop()

        # corresponds to acdeg
        two_pattern = [
            pattern
            for pattern in signal_patterns
            if len(pattern) == 5 and {a_map, d_map, e_map, g_map}.issubset(pattern)
        ][0]
        c_map = set(two_pattern).difference({a_map, d_map, e_map, g_map}).pop()

        # last one remaining
        f_map = set('abcdefg').difference({a_map, b_map, c_map, d_map, e_map, g_map}).pop()

        mapping = {
            a_map: "a",
            b_map: "b",
            c_map: "c",
            d_map: "d",
            e_map: "e",
            f_map: "f",
            g_map: "g",
        }
        display_mapping = {
            "abcefg": "0",
            "cf": "1",
            "acdeg": "2",
            "acdfg": "3",
            "bcdf": "4",
            "abdfg": "5",
            "abdefg": "6",
            "acf": "7",
            "abcdefg": "8",
            "abcdfg": "9"
        }

        display = ""
        for value in output_values:
            mapped_value = "".join(sorted(mapping[x] for x in value))
            display += display_mapping[mapped_value]
        result_part_2 += int(display)

    print(f"part 2: {result_part_2}")


if __name__ == "__main__":
    for input_filename in [
        "sample.txt",
        "input.txt"
    ]:
        print(f"-- {input_filename} --")
        main(input_filename)
