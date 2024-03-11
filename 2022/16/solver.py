import re
from functools import cache


valves = {}


def parse_input(filename):
    global valves
    valves = {}
    with open(filename) as input_file:
        for line in input_file:
            line = line.strip()
            # e.g. "Valve AA has flow rate=0; tunnels lead to valves DD, II, BB"
            # or   "Valve JJ has flow rate=21; tunnel leads to valve II"
            _, name, rate, neigh = re.split("Valve | has flow rate=|; tunnels? leads? to valves? ", line)
            valves[name] = {
                "rate": int(rate),
                "direct_neighbors": tuple(neigh.split(", ")),
                "distances": {}  # to all operational valves, will be populated later
            }


def compute_distances():
    operational_valves = {name for name, data in valves.items() if data["rate"] > 0}
    unvisited_operational_valves = set(operational_valves) | {"AA"}  # we start at AA
    while unvisited_operational_valves:
        operational_valve = unvisited_operational_valves.pop()
        distances = {name: len(valves) for name in valves}
        distances[operational_valve] = 0
        unvisited = set(distances)
        current = operational_valve
        while unvisited:
            for neighbor in valves[current]["direct_neighbors"]:
                distances[neighbor] = min(distances[neighbor], distances[current] + 1)
            unvisited.remove(current)
            if current in operational_valves.difference({operational_valve}):
                valves[operational_valve]["distances"][current] = distances[current]
            current = min(unvisited, key=distances.get, default=None)


@cache
def find_max_pressure(vertex="AA", steps=0, opened=(), max_steps=30):
    # perform a recursive graph traverse
    opened = tuple(sorted(opened + (vertex,)))
    max_pressure = 0
    for neighbor, distance in valves[vertex]["distances"].items():
        if neighbor not in opened:
            steps_neighbor = steps + distance + 1
            if steps_neighbor < max_steps:
                max_pressure = max(
                    max_pressure,
                    (
                        (max_steps - steps_neighbor) * valves[neighbor]["rate"]
                        + find_max_pressure(neighbor, steps_neighbor, opened, max_steps)
                    )
                )
    return max_pressure


@cache
def find_max_pressure_with_elephant(vertex="AA", steps=0, opened=()):
    # perform a recursive graph traverse, but at each step we let the elephant traverse the rest of the graph
    max_steps = 26
    opened = tuple(sorted(opened + (vertex,)))
    # let elephant find the max pressure visiting the remaining vertices
    max_pressure = find_max_pressure(opened=opened, max_steps=max_steps)
    for neighbor, distance in valves[vertex]["distances"].items():
        if neighbor not in opened:
            steps_neighbor = steps + distance + 1
            if steps_neighbor < max_steps:
                max_pressure = max(
                    max_pressure,
                    (
                        (max_steps - steps_neighbor) * valves[neighbor]["rate"]
                        + find_max_pressure_with_elephant(neighbor, steps_neighbor, opened)
                    )
                )
    return max_pressure


def main(filename):
    parse_input(filename)
    compute_distances()

    # part 1
    find_max_pressure.cache_clear()
    print(f"part 1: {find_max_pressure()}")

    # part 2
    find_max_pressure.cache_clear()
    find_max_pressure_with_elephant.cache_clear()
    print(f"part 2: {find_max_pressure_with_elephant()}")


if __name__ == "__main__":
    for input_filename in [
        "sample.txt",
        "input.txt"
    ]:
        print(f"-- {input_filename} --")
        main(input_filename)
