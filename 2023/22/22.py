from collections import defaultdict


def main1():
    bricks = []
    with open("input.txt") as input_file:
        for i, row in enumerate(input_file):
            start, end = row.strip().split("~")
            start = tuple(map(int, start.split(",")))
            end = tuple(map(int, end.split(",")))
            bricks.append((i, start, end))


    # level => coords => brick#
    level_map = defaultdict(dict)
    # brick# => (level_low, low_coords, level_high, high_coords)
    brick_map = {}

    # populate the data structures
    for n, start, end in bricks:
        if start == end:
            level_map[start[2]][start[:2]] = n
            brick_map[n] = (start[2], {start[:2]}, start[2], {start[:2]})
        else:
            index = [i for i in range(3) if start[i] != end[i]][0]
            if index == 2:
                mn = min(start[2], end[2])
                mx = max(start[2], end[2])
                level_map[mn][start[:2]] = n
                level_map[mx][start[:2]] = n
                brick_map[n] = (mn, {start[:2]}, mx, {start[:2]})
            else:
                coords_set = set()
                for x in range(min(start[index], end[index]), max(start[index], end[index]) + 1):
                    if index == 0:
                        coords_set.add((x, start[1]))
                    else:
                        coords_set.add((start[0], x))
                for coords in coords_set:
                    level_map[start[2]][coords] = n
                brick_map[n] = (start[2], coords_set, start[2], coords_set)

    # for z, data in level_map.items():
    #     print(z, data)

    # let all bricks fall until they are blocked
    found = True
    while found:
        found = None
        for n, (n_low, n_low_coords_set, n_high, n_high_coords_set) in brick_map.items():
            if n_low == 1:
                continue
            if not set(level_map[n_low - 1]).intersection(n_low_coords_set):
                found = (n, (n_low, n_low_coords_set, n_high, n_high_coords_set))
                # print(f"moving down {'ABCDEFG'[n]}")
                # print("moving down", n, n_low)
                break
        if found:
            n, (n_low, n_low_coords_set, n_high, n_high_coords_set) = found
            brick_map[n] = (n_low - 1, n_low_coords_set, n_high - 1, n_high_coords_set)
            for coords in n_low_coords_set:
                del level_map[n_low][coords]
                level_map[n_low - 1][coords] = n
            if n_low < n_high:
                for coords in n_high_coords_set:
                    del level_map[n_high][coords]
                    level_map[n_high - 1][coords] = n

    # print("finished moving.")

    # for z, data in level_map.items():
    #     print(z, data)

    # part 1: find bricks that can be desintegrated
    can_be_desintegrated = {n: True for n in brick_map}
    for n, (n_low, n_low_coords_set, n_high, n_high_coords_set) in brick_map.items():
        if n_low == 1:
            continue
        is_supported_by = set()
        for coords in set(level_map[n_low - 1]).intersection(n_low_coords_set):
            is_supported_by.add(level_map[n_low - 1][coords])
        if len(is_supported_by) == 1:
            m = list(is_supported_by)[0]
            can_be_desintegrated[m] = False
    # print(can_be_desintegrated)
    # for n, v in can_be_desintegrated.items():
    #     print("ABCDEFG"[n], v)
    total = sum(can_be_desintegrated.values())
    print(f"part 1: {total}")

    # part 2
    is_only_support_for = {n: [] for n in brick_map}
    is_support_for = {n: [] for n in brick_map}
    is_supported_by = {n: [] for n in brick_map}
    for n, (n_low, n_low_coords_set, n_high, n_high_coords_set) in brick_map.items():
        if n_low == 1:
            continue
        is_supported_by_list = set()
        for coords in set(level_map[n_low - 1]).intersection(n_low_coords_set):
            is_supported_by_list.add(level_map[n_low - 1][coords])
        if len(is_supported_by_list) == 1:
            m = list(is_supported_by_list)[0]
            is_only_support_for[m].append(n)
        for m in is_supported_by_list:
            is_support_for[m].append(n)
            is_supported_by[n].append(m)
    # print(can_be_desintegrated)
    # for n, v in can_be_desintegrated.items():
    #     print("ABCDEFG"[n], v)

    # print("--- only support:")
    # for m, lst in is_only_support_for.items():
    #     print(m, lst)
    # print("----- support for:")
    # for m, lst in is_support_for.items():
    #     print(m, lst)
    # print("----- supported by:")
    # for m, lst in is_supported_by.items():
    #     print(m, lst)

    total = 0
    for n, v in can_be_desintegrated.items():
        if v:
            continue
        # print("checking for", n)
        is_supported_by_copy = {m: list(lst) for m, lst in is_supported_by.items()}
        pool = set()
        for m in is_support_for[n]:
            is_supported_by_copy[m].remove(n)
            pool.add(m)
        removed = 0
        while pool:
            found = None
            for m in pool:
                if not is_supported_by_copy[m]:
                    found = m
                    break
            if found is None:
                break
            m = found
            for k in is_support_for[m]:
                is_supported_by_copy[k].remove(m)
                pool.add(k)
            pool.remove(m)
            # print("  removing", m)
            total += 1
            removed += 1

        print(f"checked {n}, removed: {removed}")

    print(f"part 2: {total}")


def main2():
    pass


if __name__ == "__main__":
    main1()
