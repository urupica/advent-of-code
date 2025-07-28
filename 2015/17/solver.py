from collections import defaultdict

count = defaultdict(int)


def search(containers, liters, i=0, used=0):
    if liters == 0:
        count[used] += 1
        return
    if i == len(containers):
        return
    search(containers, liters, i + 1, used=used)
    size = containers[i]
    if liters - size >= 0:
        search(containers, liters - size, i + 1, used=used + 1)


def solve(filename):
    with open(filename) as input_file:
        containers = tuple(map(int, input_file))

    count.clear()
    liters = 150 if filename == "input.txt" else 25
    search(containers, liters)

    result_part_1 = sum(count.values())
    print(f"part 1: {result_part_1}")

    result_part_2 = count[min(count)]
    search(containers, liters)
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
