from functools import cache

neigh = {}

@cache
def count_paths_1(v):
    if v == "out":
        return 1
    if v not in neigh:
        return 0
    return sum(count_paths_1(w) for w in neigh[v])

@cache
def count_paths_2(v, visited_dac=False, visited_fft=False):
    if v == "out":
        return int(visited_dac and visited_fft)
    if v not in neigh:
        return 0
    return sum(count_paths_2(w, visited_dac or v == "dac", visited_fft or v == "fft") for w in neigh[v])


def solve(filename):
    neigh.clear()
    with open(filename) as input_file:
        for line in input_file:
            line = line.strip()
            source, targets = line.split(":")
            neigh[source] = tuple(target.strip() for target in targets.split())

    if filename in ["sample.txt", "input.txt"]:
        count_paths_1.cache_clear()
        result_part_1 = count_paths_1("you")
        print(f"part 1: {result_part_1}")

    if filename in ["sample2.txt", "input.txt"]:
        count_paths_2.cache_clear()
        result_part_2 = count_paths_2("svr")
        print(f"part 2: {result_part_2}")


def main():
    for filename in [
        "sample.txt",
        "sample2.txt",
        "input.txt"
    ]:
        print(f"-- {filename} --")
        solve(filename)


if __name__ == "__main__":
    main()
