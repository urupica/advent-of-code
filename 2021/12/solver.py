from collections import defaultdict


count = 0
neighbors = defaultdict(list)


def search(path, allow_twice=False, already_visited_twice=False):
    global count
    head = path[-1]
    if head == "end":
        count += 1
        return

    for neigh in neighbors[head]:
        visiting_twice = False
        if neigh[0].islower() and neigh in path:
            if neigh == "start" or not allow_twice or already_visited_twice:
                continue
            else:
                visiting_twice = True
        path.append(neigh)
        search(path, allow_twice=allow_twice, already_visited_twice=already_visited_twice or visiting_twice)
        path.pop()


def main(filename):
    global count, neighbors
    neighbors = defaultdict(list)
    with open(filename) as input_file:
        for line in input_file:
            v1, v2 = line.strip().split("-")
            neighbors[v1].append(v2)
            neighbors[v2].append(v1)

    count = 0
    search(["start"])
    print(f"part 1: {count}")

    count = 0
    search(["start"], allow_twice=True)
    print(f"part 2: {count}")


if __name__ == "__main__":
    for input_filename in [
        "sample.txt",
        "input.txt"
    ]:
        print(f"-- {input_filename} --")
        main(input_filename)
