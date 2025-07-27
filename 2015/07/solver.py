def simulate(commands, values):
    while commands:
        to_remove = []
        for left, variable_dest in commands:
            if " " not in left:
                if left.isdigit() or left in values:
                    values[variable_dest] = int(left) if left.isdigit() else values[left]
                    to_remove.append((left, variable_dest))
            elif "LSHIFT" in left:
                source, amount = left.split(" LSHIFT ")
                if source.isdigit() or source in values:
                    values[variable_dest] = (int(source) if source.isdigit() else values[source]) << int(amount)
                    to_remove.append((left, variable_dest))
            elif "RSHIFT" in left:
                source, amount = left.split(" RSHIFT ")
                if source.isdigit() or source in values:
                    values[variable_dest] = (int(source) if source.isdigit() else values[source]) >> int(amount)
                    to_remove.append((left, variable_dest))
            elif "AND" in left:
                source_1, source_2 = left.split(" AND ")
                if (source_1.isdigit() or source_1 in values) and (source_2.isdigit() or source_2 in values):
                    source_1 = int(source_1) if source_1.isdigit() else values[source_1]
                    source_2 = int(source_2) if source_2.isdigit() else values[source_2]
                    values[variable_dest] = source_1 & source_2
                    to_remove.append((left, variable_dest))
            elif "OR" in left:
                source_1, source_2 = left.split(" OR ")
                if (source_1.isdigit() or source_1 in values) and (source_2.isdigit() or source_2 in values):
                    source_1 = int(source_1) if source_1.isdigit() else values[source_1]
                    source_2 = int(source_2) if source_2.isdigit() else values[source_2]
                    values[variable_dest] = source_1 | source_2
                    to_remove.append((left, variable_dest))
            elif "NOT" in left:
                source = left.replace("NOT ", "")
                if source.isdigit() or source in values:
                    values[variable_dest] = (2 ** 16 - 1) ^ (int(source) if source.isdigit() else values[source])
                    to_remove.append((left, variable_dest))
            else:
                raise NotImplementedError
        for x in to_remove:
            commands.remove(x)


def solve(filename):
    with open(filename) as input_file:
        commands = [tuple(line.strip().split(" -> ")) for line in input_file]

    values = {}
    simulate(list(commands), values)
    result_part_1 = values.get("a")
    print(f"part 1: {result_part_1}")

    values = {"b": result_part_1}
    commands = [(left, variable_dest) for left, variable_dest in commands if not left.isdigit() or variable_dest != "b"]
    simulate(commands, values)
    result_part_2 = values.get("a")
    print(f"part 2: {result_part_2}")


def main():
    for filename in [
        "sample.txt",
        "input.txt"
    ]:
        print(f"-- {filename} --")
        solve(filename)


if __name__ == "__main__":
    main()
