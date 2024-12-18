def get_shortest_path(size, blocked):
    dist = {(0, 0): 0}
    visited = set()
    while True:
        pool = set(dist).difference(visited)
        if not pool:
            return None

        v = min(pool, key=dist.get)
        visited.add(v)

        if v == (size - 1, size - 1):
            return dist[v]

        i, j = v
        for ii, jj in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
            if 0 <= ii < size and 0 <= jj < size:
                w = (ii, jj)
                if (w not in dist or dist[v] + 1 < dist[w]) and w not in blocked:
                    dist[w] = dist[v] + 1

def get_first_blocking_byte_position(byte_positions, size):
    i, j = 0, len(byte_positions)
    while i <= j:
        k = (i + j) // 2
        if get_shortest_path(size, set(byte_positions[:k])) is None:
            j = k - 1
        else:
            i = k + 1
    return byte_positions[j]


def main(filename):
    with open(filename) as input_file:
        byte_positions = [tuple(map(int, line.strip().split(","))) for line in input_file]

    size, bytes_count = {
        "sample.txt": (7, 12),
        "input.txt": (71, 1024)
    }[filename]

    path_length = get_shortest_path(size, set(byte_positions[:bytes_count]))
    print(f"part 1: {path_length}")

    a, b = get_first_blocking_byte_position(byte_positions, size)
    print(f"part 2: {a},{b}")


if __name__ == "__main__":
    for input_filename in [
        "sample.txt",
        "input.txt"
    ]:
        print(f"-- {input_filename} --")
        main(input_filename)
