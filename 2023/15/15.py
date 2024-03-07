def parse_input():
    with open("input.txt") as input_file:
        return [step.strip() for step in input_file.read().strip().split(",")]


def get_hash(label):
    return sum(ord(x) * 17**(len(label) - i) for i, x in enumerate(label)) % 256


def main():
    sequence = parse_input()

    # part 1
    result = sum(get_hash(step) for step in sequence)
    print(f"part 1: {result}")

    # part 2
    boxes = [{} for _ in range(256)]
    for step in sequence:
        if "=" in step:
            label, focal_length = step.split("=")
            boxes[get_hash(label)][label] = int(focal_length)
        else:
            assert step.endswith("-")
            label = step[:-1]
            boxes[get_hash(label)].pop(label, None)
    result = 0
    for i, box in enumerate(boxes):
        for j, (_, focal_length) in enumerate(box.items()):
            result += (i + 1) * (j + 1) * focal_length
    print(f"part 2: {result}")


if __name__ == "__main__":
    main()
