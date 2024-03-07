import operator
from collections import defaultdict
from functools import reduce

import numpy as np


flip_flop_states = {}
conjunction_states = {}


def parse_input(filename):
    connections = {}
    with open(filename) as input_file:
        for row in input_file:
            row = row.strip()
            source, destinations = row.split(" -> ")
            if source.startswith("%"):
                connections[source[1:]] = ("flip-flop", destinations.split(", "))
            elif source.startswith("&"):
                connections[source[1:]] = ("conjunction", destinations.split(", "))
            else:
                assert source == "broadcaster"
                connections[source] = (None, destinations.split(", "))
    return connections


def set_default_states(connections):
    global flip_flop_states, conjunction_states
    flip_flop_states = {
        source: "off"
        for source, (source_type, _) in connections.items()
        if source_type == "flip-flop"
    }
    conjunction_states = defaultdict(dict)
    for source, (_, destinations) in connections.items():
        for dest in destinations:
            if dest in connections and connections[dest][0] == "conjunction":
                conjunction_states[dest][source] = "low"


def get_parents_map(connections):
    parents_map = defaultdict(list)
    for source, (_, destinations) in connections.items():
        for dest in destinations:
            parents_map[dest].append(source)
    return parents_map


def main():
    connections = parse_input("input.txt")
    set_default_states(connections)
    counter = {"low": 0, "high": 0}
    part_1_result = None
    cycles = 1
    prev_highs = {"hn": [], "fz": [], "xf": [], "mp": []}
    part_2_result = None
    while part_1_result is None or part_2_result is None:
        pool = [("broadcaster", "low", "button")]
        while pool:
            pool_next = []
            for source, strength, prev in pool:
                # for part 2
                if strength == "high" and prev in prev_highs:
                    prev_highs[prev].append(cycles)
                    if all(prev_highs.values()) and part_2_result is None:
                        part_2_result = np.lcm.reduce([x[0] for x in prev_highs.values()])

                # for part 1
                counter[strength] += 1
                if source not in connections:
                    continue
                source_type, destinations = connections[source]
                if source_type is None:
                    assert source == "broadcaster"
                    pool_next.extend([(dest, strength, source) for dest in destinations])
                elif source_type == "flip-flop":
                    if strength == "low":
                        flip_flop_states[source] = "on" if flip_flop_states[source] == "off" else "off"
                        out_strength = "high" if flip_flop_states[source] == "on" else "low"
                        pool_next.extend([(dest, out_strength, source) for dest in destinations])
                else:
                    assert source_type == "conjunction"
                    conjunction_states[source][prev] = strength
                    if all(s == "high" for s in conjunction_states[source].values()):
                        out_strength = "low"
                    else:
                        out_strength = "high"
                    pool_next.extend([(dest, out_strength, source) for dest in destinations])
            pool = pool_next
        if cycles == 1_000:
            part_1_result = reduce(operator.mul, counter.values())
        cycles += 1

    print(f"part 1: {part_1_result}")
    print(f"part 2: {part_2_result}")


if __name__ == "__main__":
    main()
