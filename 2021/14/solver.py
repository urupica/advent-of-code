from collections import Counter
from functools import cache

insertions = {}


@cache
def get_insertion_counter(pair, steps):
    if steps == 0 or pair not in insertions:
        return Counter()

    counter = Counter(insertions[pair])
    counter.update(get_insertion_counter(pair[0] + insertions[pair], steps - 1))
    counter.update(get_insertion_counter(insertions[pair] + pair[1], steps - 1))
    return counter


def main(filename):
    global insertions
    with open(filename) as input_file:
        template = input_file.readline().strip()
        input_file.readline()
        insertions = {}
        for line in input_file:
            pair, insertion = line.strip().split(" -> ")
            insertions[pair] = insertion

    for part, steps in enumerate([10, 40], start=1):
        get_insertion_counter.cache_clear()
        counter = Counter(template)
        for pair in [template[i:i + 2] for i in range(len(template) - 1)]:
            counter.update(get_insertion_counter(pair, steps))

        result = max(counter.values()) - min(counter.values())
        print(f"part {part}: {result}")


if __name__ == "__main__":
    for input_filename in [
        "sample.txt",
        "input.txt"
    ]:
        print(f"-- {input_filename} --")
        main(input_filename)
