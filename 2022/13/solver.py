from functools import cmp_to_key


def parse(s):
    depth = 0
    parsed = []
    i = 0
    for j, x in enumerate(s):
        if x == "[":
            depth += 1
            if depth == 1:
                i = j + 1
        elif x == "," and depth == 1 and i < j:
            parsed.append(int(s[i:j]))
            i = j + 1
        elif x == "]":
            depth -= 1
            if depth == 1:
                parsed.append(parse(s[i:j + 1]))
                i = j + 2
            elif depth == 0 and i < j:
                parsed.append(int(s[i:j]))
    return parsed


def is_in_right_order(left, right):
    for x, y in zip(left, right):
        if isinstance(x, int) and isinstance(y, int):
            if x < y:
                return True
            if x > y:
                return False
        elif isinstance(x, list) and isinstance(y, list):
            check = is_in_right_order(x, y)
            if check is True:
                return True
            if check is False:
                return False
        else:
            if isinstance(x, list):
                y = [y]
            else:
                x = [x]
            check = is_in_right_order(x, y)
            if check is True:
                return True
            if check is False:
                return False
    if len(left) < len(right):
        return True
    if len(left) > len(right):
        return False


def compare(left, right):
    return {True: -1, False: 1, None: 0}[is_in_right_order(parse(left), parse(right))]


def main(filename):
    all_packets = []
    with open(filename) as input_file:
        left = None
        for line_count, line in enumerate(input_file):
            line = line.strip()
            if line_count % 3 < 2:
                all_packets.append(line)

    result_part_1 = 0
    for count, packet in enumerate(all_packets):
        if count % 2 == 0:
            left = parse(packet)
        else:
            right = parse(packet)
            if is_in_right_order(left, right):
                result_part_1 += count // 2 + 1

    control1, control2 = "[[2]]", "[[6]]"
    all_packets.extend([control1, control2])
    all_packets.sort(key=cmp_to_key(compare))
    index1 = all_packets.index(control1) + 1
    index2 = all_packets.index(control2) + 1
    result_part_2 = index1 * index2

    print(f"part 1: {result_part_1}")
    print(f"part 2: {result_part_2}")


if __name__ == "__main__":
    for name in [
        "sample.txt",
        "input.txt"
    ]:
        print(f"-- {name} --")
        main(name)
