from math import sqrt, ceil, floor


def main1():
    times = distances = None
    with open("input.txt") as input_file:
        for row in input_file:
            if row.startswith("Time:"):
                row = row.replace("Time:", "").strip()
                times = [int(x) for x in row.split()]
            elif row.startswith("Distance:"):
                row = row.replace("Distance:", "").strip()
                distances = [int(x) for x in row.split()]

    result = 1
    for time, distance in zip(times, distances):
        radicand = (time / 2) ** 2 - distance
        if radicand < 0:
            result *= 0
        else:
            min_time = ceil(time / 2 - sqrt(radicand))
            max_time = floor(time / 2 + sqrt(radicand))
            if min_time ** 2 - time * min_time + distance == 0:
                min_time += 1
            if max_time ** 2 - time * max_time + distance == 0:
                max_time -= 1
            result *= (max_time - min_time + 1)
    print(result)


def main2():
    time = distance = None
    with open("input.txt") as input_file:
        for row in input_file:
            if row.startswith("Time:"):
                row = row.replace("Time:", "").strip()
                time = int("".join(row.split()))
            elif row.startswith("Distance:"):
                row = row.replace("Distance:", "").strip()
                distance = int("".join(row.split()))

    radicand = (time / 2) ** 2 - distance
    if radicand < 0:
        result = 0
    else:
        min_time = ceil(time / 2 - sqrt(radicand))
        max_time = floor(time / 2 + sqrt(radicand))
        if min_time ** 2 - time * min_time + distance == 0:
            min_time += 1
        if max_time ** 2 - time * max_time + distance == 0:
            max_time -= 1
        result = (max_time - min_time + 1)
    print(result)


if __name__ == "__main__":
    main2()
