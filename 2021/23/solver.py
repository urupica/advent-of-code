ENERGY_PER_STEP = {"A": 1, "B": 10, "C": 100, "D": 1_000}
ADDITIONAL_ROOMS = (("D", "D"), ("C", "B"), ("B", "A"), ("A", "C"))


def get_target_positions(i, hall):
    entrance = 2 + 2 * i
    if not hall[entrance]:
        for side_range in [range(entrance - 1, -1, -1), range(entrance + 1, 11)]:
            for k in side_range:
                if hall[k]:
                    break
                if k in [0, 10] or k % 2 == 1:
                    yield k, abs(entrance - k)


def get_neighbors(rooms_hall):
    rooms, hall = rooms_hall[:4], rooms_hall[4:]

    # try to move an amphipod from the hall to its room
    for k, x in enumerate(hall):
        if x:
            for side_range in [range(k - 1, -1, -1), range(k + 1, 11)]:
                for kk in side_range:
                    if hall[kk]:
                        break
                    if 2 <= kk <= 8 and kk % 2 == 0:
                        i = (kk - 2) // 2
                        if "ABCD"[i] == x and not rooms[i][0]:
                            room = rooms[i]
                            if all(y == x for y in room if y):
                                j = 0
                                while j + 1 < len(room) and not room[j + 1]:
                                    j += 1
                                rooms_new = rooms[:i] + ((None,) * j + (x,) + room[j + 1:],) + rooms[i + 1:]
                                hall_new = hall[:k] + (None,) + hall[k + 1:]
                                energy = (abs(k - kk) + j + 1) * ENERGY_PER_STEP[x]
                                yield rooms_new + hall_new, energy
                                # if we can move an amphipod from the hall to a room
                                # there's no need to check other options
                                return

    # move amphipods from the rooms to the hall
    for i, room in enumerate(rooms):
        for j, x in enumerate(room):
            if x:
                if x != "ABCD"[i] or any(y != "ABCD"[i] for y in room[j + 1:]):
                    for k, steps in get_target_positions(i, hall):
                        rooms_new = rooms[:i] + ((None,) * (j + 1) + room[j + 1:],) + rooms[i + 1:]
                        hall_new = hall[:k] + (x,) + hall[k + 1:]
                        energy = (j + 1 + steps) * ENERGY_PER_STEP[x]
                        yield rooms_new + hall_new, energy
                break


def find_min_total_energy(rooms_hall):
    pool = {rooms_hall}
    visited = set()
    dist = {rooms_hall: 0}
    while True:
        rooms_hall = min(pool, key=dist.get)
        pool.remove(rooms_hall)
        if rooms_hall in visited:
            continue
        visited.add(rooms_hall)

        rooms, hall = rooms_hall[:4], rooms_hall[4:]
        room_length = len(rooms[0])
        if rooms == (("A",) * room_length, ("B",) * room_length, ("C",) * room_length, ("D",) * room_length):
            return dist[rooms_hall]

        for rooms_hall_neigh, dist_neigh in get_neighbors(rooms_hall):
            if rooms_hall_neigh in visited:
                continue
            if rooms_hall_neigh not in dist:
                dist[rooms_hall_neigh] = dist[rooms_hall] + dist_neigh
            else:
                dist[rooms_hall_neigh] = min(dist[rooms_hall_neigh], dist[rooms_hall] + dist_neigh)
            pool.add(rooms_hall_neigh)


def main(filename):
    rooms = [[None] * 2 for _ in range(4)]
    with open(filename) as input_file:
        for k, line in enumerate(input_file):
            if 2 <= k <= 3:
                for i, x in enumerate([line[3], line[5], line[7], line[9]]):
                    rooms[i][k - 2] = x

    # part 1
    rooms = tuple(tuple(room) for room in rooms)
    hall = (None,) * 11
    min_total_energy = find_min_total_energy(rooms + hall)
    print(f"part 1: {min_total_energy}")

    # part 2
    # rooms = tuple((room[0], room2[0], room2[1], room[1]) for room, room2 in zip(rooms, ADDITIONAL_ROOMS))
    # hall = (None,) * 11
    # min_total_energy = find_min_total_energy(rooms + hall)
    # print(f"part 2: {min_total_energy}")


if __name__ == "__main__":
    for input_filename in [
        "sample.txt",
        "input.txt"
    ]:
        print(f"-- {input_filename} --")
        main(input_filename)
