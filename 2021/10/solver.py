def main(filename):
    with open(filename) as input_file:
        input_data = [line.strip() for line in input_file]

    # part 1
    opening = {
        ")": "(",
        "]": "[",
        "}": "{",
        ">": "<",
    }
    score = {
        ")": 3,
        "]": 57,
        "}": 1197,
        ">": 25137,
    }
    result_part_1 = 0
    corrupted_lines = set()
    for i, row in enumerate(input_data):
        stack = []
        for c in row:
            if c in "([{<":
                stack.append(c)
            else:
                if not stack or stack[-1] != opening[c]:
                    result_part_1 += score[c]
                    corrupted_lines.add(i)
                    break
                else:
                    stack.pop()
    print(f"part 1: {result_part_1}")

    # part 2
    score = {
        "(": 1,
        "[": 2,
        "{": 3,
        "<": 4
    }
    all_total_points = []
    for i, row in enumerate(input_data):
        if i in corrupted_lines:
            continue
        total_points = 0
        stack = []
        for c in row:
            if c in "([{<":
                stack.append(c)
            else:
                stack.pop()
        for c in stack[::-1]:
            total_points *= 5
            total_points += score[c]
        all_total_points.append(total_points)
    all_total_points.sort()
    result_part_2 = all_total_points[len(all_total_points) // 2]
    print(f"part 2: {result_part_2}")


if __name__ == "__main__":
    for input_filename in [
        "sample.txt",
        "input.txt"
    ]:
        print(f"-- {input_filename} --")
        main(input_filename)
