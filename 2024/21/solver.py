import re
from itertools import batched


def get_row_column_numerical_keypad(key):
    if key in "789":
        row = 1
    elif key in "456":
        row = 2
    elif key in "123":
        row = 3
    else:
        row = 4

    if key in "741":
        col = 1
    elif key in "8520":
        col = 2
    else:
        col = 3

    return row, col


def get_row_column_directional_keypad(key):
    if key in "^A":
        row = 1
    else:
        row = 2

    if key == "<":
        col = 1
    elif key in "^v":
        col = 2
    else:
        col = 3

    return row, col


def move_to_numerical_keypad(current, target):
    current_row, current_col = get_row_column_numerical_keypad(current)
    target_row, target_col = get_row_column_numerical_keypad(target)

    if current_row == target_row:
        if current_col < target_col:
            return [(">", target_col - current_col, "A", 1)]
        else:
            return [("<", current_col - target_col, "A", 1)]
    elif current_col == target_col:
        if current_row < target_row:
            return [("v", target_row - current_row, "A", 1)]
        else:
            return [("^", current_row - target_row, "A", 1)]
    else:
        if current_col < target_col:
            if current_row < target_row:
                if current_col == 1 and target_row == 4:
                    return [(">", target_col - current_col, "v", target_row - current_row, "A", 1)]
                else:
                    return [
                        (">", target_col - current_col, "v", target_row - current_row, "A", 1),
                        ("v", target_row - current_row, ">", target_col - current_col, "A", 1),
                    ]
            else:
                return [
                    (">", target_col - current_col, "^", current_row - target_row, "A", 1),
                    ("^", current_row - target_row, ">", target_col - current_col, "A", 1),
                ]
        else:
            if current_row < target_row:
                return [
                    ("<", current_col - target_col, "v", target_row - current_row, "A", 1),
                    ("v", target_row - current_row, "<", current_col - target_col, "A", 1),
                ]
            else:
                if current_row == 4 and target_col == 1:
                    return [("^", current_row - target_row, "<", current_col - target_col, "A", 1)]
                else:
                    return [
                        ("<", current_col - target_col, "^", current_row - target_row, "A", 1),
                        ("^", current_row - target_row, "<", current_col - target_col, "A", 1),
                    ]


def move_to_directional_keypad(current, target):
    current_row, current_col = get_row_column_directional_keypad(current)
    target_row, target_col = get_row_column_directional_keypad(target)

    if current_row == target_row:
        if current_col < target_col:
            return [(">", target_col - current_col, "A", 1)]
        else:
            return [("<", current_col - target_col, "A", 1)]
    elif current_col == target_col:
        if current_row < target_row:
            return [("v", target_row - current_row, "A", 1)]
        else:
            return [("^", current_row - target_row, "A", 1)]
    else:
        if current_col < target_col:
            if current_row < target_row:
                return [
                    (">", target_col - current_col, "v", target_row - current_row, "A", 1),
                    ("v", target_row - current_row, ">", target_col - current_col, "A", 1),
                ]
            else:
                if current_col == 1:
                    return [(">", target_col - current_col, "^", current_row - target_row, "A", 1)]
                else:
                    return [
                        (">", target_col - current_col, "^", current_row - target_row, "A", 1),
                        ("^", current_row - target_row, ">", target_col - current_col, "A", 1),
                    ]
        else:
            if current_row < target_row:
                if target_col == 1:
                    return [("v", target_row - current_row, "<", current_col - target_col, "A", 1)]
                else:
                    return [
                        ("<", current_col - target_col, "v", target_row - current_row, "A", 1),
                        ("v", target_row - current_row, "<", current_col - target_col, "A", 1),
                    ]
            else:
                return [
                    ("<", current_col - target_col, "^", current_row - target_row, "A", 1),
                    ("^", current_row - target_row, "<", current_col - target_col, "A", 1),
                ]


def get_best_moves_directional_keypad():
    max_level = 25
    best_moves_directional_keypad = {level: {} for level in range(1, max_level + 1)}

    level = 1
    while level <= max_level:
        for current in ["<", "v", ">", "^", "A"]:
            for target in ["<", "v", ">", "^", "A"]:
                if current == target:
                    continue
                if level == 1:
                    best_moves_directional_keypad[level][(current, target)] = min(sum(option[1::2]) for option in move_to_directional_keypad(current, target))
                else:
                    best = None
                    for option in move_to_directional_keypad(current, target):
                        prev = "A"
                        total = 0
                        for step_dir, step_count in batched(option, 2):
                            total += best_moves_directional_keypad[level - 1][(prev, step_dir)] + step_count - 1
                            prev = step_dir
                        if best is None or total < best:
                            best = total
                    best_moves_directional_keypad[level][(current, target)] = best
        level += 1
    return best_moves_directional_keypad

def get_best_move_numerical_keypad(best_moves_keypad, level, current, target):
    best = None
    for option in move_to_numerical_keypad(current, target):
        prev = "A"
        total = 0
        for step_dir, step_count in batched(option, 2):
            total += best_moves_keypad[level][(prev, step_dir)] + step_count - 1
            prev = step_dir
        if best is None or total < best:
            best = total
    return best


def solve(filename):
    with open(filename) as input_file:
        codes = [line.strip() for line in input_file]

    best_moves_keypad = get_best_moves_directional_keypad()

    for part, level in [(1, 2), (2, 25)]:
        result_part = 0
        for code in codes:
            current = "A"
            result = 0
            for target in code:
                result += get_best_move_numerical_keypad(best_moves_keypad, level, current, target)
                current = target
            result_part += result * int("".join(re.findall(r"\d", code)))
        print(f"part {part}: {result_part}")


def main():
    for filename in [
        "sample.txt",
        "input.txt"
    ]:
        print(f"-- {filename} --")
        solve(filename)


if __name__ == "__main__":
    main()
