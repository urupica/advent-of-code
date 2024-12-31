import re
from collections import defaultdict


def parse(filename):
    wire_inputs = {}
    gates = defaultdict(list)
    with open(filename) as input_file:
        wire_input_data, gates_data  = input_file.read().split("\n\n")
        for wire_input in wire_input_data.split("\n"):
            wire, value = wire_input.strip().split(": ")
            wire_inputs[wire] = bool(int(value))
        for gate in gates_data.split("\n"):
            input_wire1, operation, input_wire2, output_wire = re.search(
                r"(.{3}) (AND|XOR|OR) (.{3}) -> (.{3})", gate.strip()
            ).groups()
            gates[tuple(sorted((input_wire1, input_wire2)))].append([operation, output_wire])
    return wire_inputs, gates


def solve_part_1(wire_inputs, gates):
    input_wire_pool = list(gates)
    while input_wire_pool:
        for w1, w2 in list(input_wire_pool):
            if w1 in wire_inputs and w2 in wire_inputs:
                for op, wo in gates[(w1, w2)]:
                    if op == "AND":
                        wire_inputs[wo] = wire_inputs[w1] and wire_inputs[w2]
                    elif op == "OR":
                        wire_inputs[wo] = wire_inputs[w1] or wire_inputs[w2]
                    else:
                        wire_inputs[wo] = wire_inputs[w1] != wire_inputs[w2]
                input_wire_pool.remove((w1, w2))
                break

    result_part_1 = sum(
        2 ** int(wire[1:])
        for wire, value in wire_inputs.items()
        if value and wire.startswith("z")
    )
    return result_part_1


all_gates = []
pointers = {}
or_wires = {}
xor_and_wires = {}
result_part_2 = None
def search(step=0, carries=(), fixed=(), swapped=()):
    global result_part_2

    if result_part_2 or len(swapped) > 8:
        return

    if step == 0:
        xor_gate = next(gate for gate in pointers[("x00", "y00")] if gate[2] == "XOR")
        if xor_gate[3] == "z00":
            search(step=1, carries=carries, fixed=fixed+("z00",), swapped=swapped)
        else:
            z_gate = next(gate for gate in all_gates if gate[3] == "z00")
            xor_gate[3], z_gate[3] = z_gate[3], xor_gate[3]
            search(step=1, carries=carries, fixed=fixed + ("z00",), swapped=swapped+(z_gate[3], xor_gate[3]))
            xor_gate[3], z_gate[3] = z_gate[3], xor_gate[3]
        return

    if step == 1:
        and_gate = next(gate for gate in pointers[("x00", "y00")] if gate[2] == "AND")
        wire = and_gate[3]
        search(step=5, carries=carries+(wire,), fixed=fixed+(wire,), swapped=swapped)
        for other_wire in xor_and_wires:
            if other_wire == wire or wire in fixed or wire in swapped:
                continue
            other_gate = next(gate for gate in all_gates if gate[3] == other_wire)
            and_gate[3], other_gate[3] = other_gate[3], and_gate[3]
            search(step=5, carries=carries+(other_wire,), fixed=fixed+(other_wire,), swapped=swapped+(other_gate[3], and_gate[3]))
            and_gate[3], other_gate[3] = other_gate[3], and_gate[3]
        return


    index = step // 5
    xor_gate = next(gate for gate in pointers[(f"x{index:>02d}", f"y{index:>02d}")] if gate[2] == "XOR")
    and_gate = next(gate for gate in pointers[(f"x{index:>02d}", f"y{index:>02d}")] if gate[2] == "AND")
    key = tuple(sorted([xor_gate[3], carries[index - 1]]))
    xor_gate_2 = next((gate for gate in pointers[key] if gate[2] == "XOR"), None)
    and_gate_2 = next((gate for gate in pointers[key] if gate[2] == "AND"), None)

    if step % 5 == 0:
        wire = xor_gate[3]
        if wire in xor_and_wires:
            search(step=step + 1, carries=carries, fixed=fixed+(wire,), swapped=swapped)
        if len(swapped) <= 6:
            for other_wire in xor_and_wires:
                if other_wire == wire or other_wire in fixed or other_wire in swapped:
                    continue
                other_gate = next(gate for gate in all_gates if gate[3] == other_wire)
                xor_gate[3], other_gate[3] = other_gate[3], xor_gate[3]
                search(step=step + 1, carries=carries, fixed=fixed+(other_wire,), swapped=swapped+(other_gate[3], xor_gate[3]))
                xor_gate[3], other_gate[3] = other_gate[3], xor_gate[3]

    elif step % 5 == 1:
        wire = and_gate[3]
        if wire in or_wires:
            search(step=step + 1, carries=carries, fixed=fixed+(wire,), swapped=swapped)
        if len(swapped) <= 6:
            for other_wire in or_wires:
                if other_wire == wire or other_wire in fixed or other_wire in swapped:
                    continue
                other_gate = next(gate for gate in all_gates if gate[3] == other_wire)
                and_gate[3], other_gate[3] = other_gate[3], and_gate[3]
                search(step=step + 1, carries=carries, fixed=fixed+(other_wire,), swapped=swapped+(other_gate[3], and_gate[3]))
                and_gate[3], other_gate[3] = other_gate[3], and_gate[3]

    elif step % 5 == 2:
        if not xor_gate_2:
            return
        wire = f"z{index:>02d}"
        if xor_gate_2[3] == wire:
            search(step=step + 1, carries=carries, fixed=fixed + (wire,), swapped=swapped)
        elif len(swapped) <= 6:
            z_gate = next(gate for gate in all_gates if gate[3] == wire)
            xor_gate_2[3], z_gate[3] = z_gate[3], xor_gate_2[3]
            search(step=step + 1, carries=carries, fixed=fixed + (wire,), swapped=swapped + (z_gate[3], xor_gate_2[3]))
            xor_gate_2[3], z_gate[3] = z_gate[3], xor_gate_2[3]

    elif step % 5 == 3:
        if not and_gate_2:
            return
        wire = and_gate_2[3]
        if wire in or_wires:
            search(step=step + 1, carries=carries, fixed=fixed + (wire,), swapped=swapped)
        if len(swapped) <= 6:
            for other_wire in or_wires:
                if other_wire == wire or other_wire in fixed or other_wire in swapped:
                    continue
                other_gate = next(gate for gate in all_gates if gate[3] == other_wire)
                and_gate_2[3], other_gate[3] = other_gate[3], and_gate_2[3]
                search(step=step + 1, carries=carries, fixed=fixed+(other_wire,), swapped=swapped+(other_gate[3], and_gate_2[3]))
                and_gate_2[3], other_gate[3] = other_gate[3], and_gate_2[3]

    else:
        if not and_gate_2:
            return
        or_gate = next((gate for gate in pointers[tuple(sorted([and_gate[3], and_gate_2[3]]))] if gate[2] == "OR"), None)
        if not or_gate:
            return
        if index == 44:
            if or_gate[3] == "z45":
                result_part_2 = ",".join(sorted(swapped))
            return
        wire = or_gate[3]
        if wire in xor_and_wires:
            search(step=step + 1, carries=carries + (wire,), fixed=fixed + (wire,), swapped=swapped)
        if len(swapped) <= 6:
            for other_wire in xor_and_wires:
                if other_wire == wire or other_wire in fixed or other_wire in swapped:
                    continue
                other_gate = next(gate for gate in all_gates if gate[3] == other_wire)
                or_gate[3], other_gate[3] = other_gate[3], or_gate[3]
                search(step=step + 1, carries=carries + (other_wire,), fixed=fixed+(other_wire,), swapped=swapped+(other_gate[3], or_gate[3]))
                or_gate[3], other_gate[3] = other_gate[3], or_gate[3]


def solve_part_2(gates):
    global all_gates, pointers, or_wires, xor_and_wires

    all_gates = []
    pointers = defaultdict(list)
    all_wires = set()
    for (w1, w2), outputs in gates.items():
        for op, w3 in outputs:
            gate = [w1, w2, op, w3]
            all_gates.append(gate)
            pointers[(w1, w2)].append(gate)
            all_wires.update([w for w in [w1, w2, w3] if w[0] not in "xyz"])

    xor_and_wires = {}
    or_wires = {}
    for wire in all_wires:
        connected_gates = [gate for gate in all_gates if wire in gate[:2]]
        if len(connected_gates) == 1:
            or_wires[wire] = connected_gates
        else:
            xor_and_wires[wire] = connected_gates

    search()


def solve(filename):
    global result_part_2

    wire_inputs, gates = parse(filename)

    result_part_1 = solve_part_1(wire_inputs, gates)
    print(f"part 1: {result_part_1}")

    result_part_2 = None
    if filename == "input.txt":
        # solution doesn't work for sample.txt
        solve_part_2(gates)
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
