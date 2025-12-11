mem = {}
def count_paths_1(neigh, v):
    if v == "out":
        return 1
    if v not in neigh:
        return 0
    if v in mem:
        return mem[v]
    ret = sum(count_paths_1(neigh, w) for w in neigh[v])
    mem[v] = ret
    return ret


def count_paths_2(neigh, v, visited_dac, visited_fft):
    if v == "out":
        return int(visited_dac and visited_fft)
    if v not in neigh:
        return 0
    if (v, visited_dac, visited_fft) in mem:
        return mem[(v, visited_dac, visited_fft)]
    ret = sum(count_paths_2(neigh, w, visited_dac or v == "dac", visited_fft or v == "fft") for w in neigh[v])
    mem[(v, visited_dac, visited_fft)] = ret
    return ret


def solve(filename):
    global mem
    neigh = {}
    with open(filename) as input_file:
        for line in input_file:
            line = line.strip()
            source, targets = line.split(":")
            neigh[source] = tuple(target.strip() for target in targets.split())

    if filename in ["sample.txt", "input.txt"]:
        mem = {}
        result_part_1 = count_paths_1(neigh, "you")
        print(f"part 1: {result_part_1}")

    if filename in ["sample2.txt", "input.txt"]:
        mem = {}
        result_part_2 = count_paths_2(neigh, "svr", False, False)
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
