import json


int_sum = 0
def traverse(data, ignore_red=False):
    global int_sum
    if isinstance(data, list):
        for x in data:
            traverse(x, ignore_red=ignore_red)
    elif isinstance(data, dict):
        if ignore_red and "red" in data.values():
            return
        for x in data.values():
            traverse(x, ignore_red=ignore_red)
    elif isinstance(data, int):
        int_sum += data


def solve(filename):
    global int_sum
    with open(filename) as input_file:
        data = json.loads(next(input_file).strip())

    int_sum = 0
    traverse(data)
    print(f"part 1: {int_sum}")

    int_sum = 0
    traverse(data, ignore_red=True)
    print(f"part 2: {int_sum}")


def main():
    for filename in [
        "sample.txt",
        "input.txt"
    ]:
        print(f"-- {filename} --")
        solve(filename)


if __name__ == "__main__":
    main()
