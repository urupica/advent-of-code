from itertools import combinations


class Pair:
    def __init__(self, *, parent=None, side=None, left=None, right=None):
        self.parent = parent
        self.side = side
        self.left = left
        self.right = right


def parse(pair_str, parent=None, side=None):
    if pair_str.isnumeric():
        return int(pair_str)

    depth = 0
    for i, x in enumerate(pair_str):
        if x == "[":
            depth += 1
        elif x == "]":
            depth -= 1
        elif x == "," and depth == 1:
            pair = Pair(parent=parent, side=side)
            pair.left = parse(pair_str[1:i], pair, "l")
            pair.right = parse(pair_str[i + 1:-1], pair, "r")
            return pair


def get_nested_pair(pair, depth=0):
    if not pair:
        return

    if depth == 4:
        return pair

    return (
        not isinstance(pair.left, int) and get_nested_pair(pair.left, depth + 1)
        or not isinstance(pair.right, int) and get_nested_pair(pair.right, depth + 1)
    )


def get_pair_to_split(pair):
    if pair is None:
        return None

    if isinstance(pair.left, int):
        if pair.left >= 10:
            return pair, "l"
    else:
        data = get_pair_to_split(pair.left)
        if data is not None:
            return data

    if isinstance(pair.right, int):
        if pair.right >= 10:
            return pair, "r"
    else:
        return get_pair_to_split(pair.right)


def add_to_left_value(pair, value):
    while pair.parent is not None and pair.side == "l":
        pair = pair.parent

    if pair.parent is not None and pair.side == "r":
        pair = pair.parent
        if isinstance(pair.left, int):
            pair.left += value
        else:
            pair = pair.left
            while not isinstance(pair.right, int):
                pair = pair.right
            pair.right += value


def add_to_right_value(pair, value):
    while pair.parent is not None and pair.side == "r":
        pair = pair.parent

    if pair.parent is not None and pair.side == "l":
        pair = pair.parent
        if isinstance(pair.right, int):
            pair.right += value
        else:
            pair = pair.right
            while not isinstance(pair.left, int):
                pair = pair.left
            pair.left += value


def explode(pair):
    nested_pair = get_nested_pair(pair)
    if not nested_pair:
        return False

    add_to_left_value(nested_pair, nested_pair.left)
    add_to_right_value(nested_pair, nested_pair.right)
    if nested_pair.side == "l":
        nested_pair.parent.left = 0
    else:
        nested_pair.parent.right = 0
    return True


def split(pair):
    split_data = get_pair_to_split(pair)
    if split_data is None:
        return False

    split_pair, side = split_data
    if side == "l":
        value = split_pair.left
        split_pair.left = Pair(parent=split_pair, side="l", left=value // 2, right=value - (value // 2))
    else:
        value = split_pair.right
        split_pair.right = Pair(parent=split_pair, side="r", left=value // 2, right=value - (value // 2))
    return True


def add(pair_1, pair_2):
    result = Pair(left=pair_1, right=pair_2)
    pair_1.parent = result
    pair_1.side = "l"
    pair_2.parent = result
    pair_2.side = "r"

    while explode(result) or split(result):
        pass
    return result


def compute_magnitude(pair):
    if isinstance(pair, int):
        return pair

    if isinstance(pair.left, int):
        left_magnitude = pair.left
    else:
        left_magnitude = compute_magnitude(pair.left)

    if isinstance(pair.right, int):
        right_magnitude = pair.right
    else:
        right_magnitude = compute_magnitude(pair.right)

    return 3 * left_magnitude + 2 * right_magnitude


def main(filename):
    with open(filename) as input_file:
        pairs_str = [line.strip() for line in input_file]

    result = parse(pairs_str[0])
    for pair_str in pairs_str[1:]:
        result = add(result, parse(pair_str))
    result_part_1 = compute_magnitude(result)
    print(f"part 1: {result_part_1}")

    result_part_2 = 0
    for pair_str_1, pair_str_2 in combinations(pairs_str, 2):
        pair_1 = parse(pair_str_1)
        pair_2 = parse(pair_str_2)
        result_part_2 = max(result_part_2, compute_magnitude(add(pair_1, pair_2)))
        pair_1 = parse(pair_str_1)
        pair_2 = parse(pair_str_2)
        result_part_2 = max(result_part_2, compute_magnitude(add(pair_2, pair_1)))
    print(f"part 2: {result_part_2}")


if __name__ == "__main__":
    for input_filename in [
        "sample.txt",
        "input.txt"
    ]:
        print(f"-- {input_filename} --")
        main(input_filename)
