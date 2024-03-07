from functools import cache


@cache
def count(springs, records):
    if not springs and not records:
        return 1

    if not springs and records:
        return 0

    if springs and not records:
        return int(not any("#" in spr for spr in springs))

    if sum(len(spring) for spring in springs) < sum(records):
        return 0

    spr = springs[0]
    rec = records[0]

    ret = 0
    if "#" not in spr:
        ret += count(springs[1:], records)

    i = 0
    j = rec
    while j <= len(spr):
        if i > 0 and spr[i - 1] == "#":
            break
        if j == len(spr) or (j < len(spr) and spr[j] == "?"):
            new_springs = ((spr[j + 1:],) if len(spr) > j + 1 else ()) + springs[1:]
            new_records = records[1:]
            ret += count(new_springs, new_records)
        i += 1
        j += 1
    return ret


def main():
    total = 0
    with open("input.txt") as input_file:
        for row in input_file:
            row = row.strip()
            springs, records = row.split()

            # unfold, only necessary in part 2
            springs = "?".join([springs] * 5)
            records = ",".join([records] * 5)

            springs = tuple(group for group in springs.split(".") if len(group) > 0)
            records = tuple(int(record) for record in records.split(","))
            total += count(springs, records)

    print(total)


if __name__ == "__main__":
    main()
