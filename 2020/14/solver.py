import re
from itertools import product


def main(filename):
    operations = []
    with open(filename) as input_file:
        for line in input_file:
            line = line.strip()
            if line.startswith("mask"):
                operations.append(("mask", line[len("mask = "):]))
            else:
                addr, val = map(int, re.match(r"mem\[(\d+)\] = (\d+)", line).groups())
                operations.append(("mem", addr, val))

    mem = {}
    mask_and = mask_or = None
    for op in operations:
        if op[0] == "mask":
            mask_and = int("".join("1" if c == "X" else "0" for c in op[1]), 2)
            mask_or = int("".join("0" if c == "X" else c for c in op[1]), 2)
        else:
            addr, val = op[1:]
            val &= mask_and
            val |= mask_or
            mem[addr] = val
    result_part_1 = sum(mem.values())
    print(f"part 1: {result_part_1}")

    mem = {}
    mask_and = mask_or = mask_float = None
    for op in operations:
        if op[0] == "mask":
            mask_and = int("".join("1" if c == "0" else "0" for c in op[1]), 2)
            mask_or = int("".join("1" if c == "1" else "0" for c in op[1]), 2)
            mask_float = [i for i in range(36) if op[1][35 - i] == "X"]
        else:
            addr, val = op[1:]
            addr &= mask_and
            addr |= mask_or
            for variant in product((0, 1), repeat=len(mask_float)):
                mem[addr + sum(v * 2**i for i, v in zip(mask_float, variant))] = val
    result_part_2 = sum(mem.values())
    print(f"part 2: {result_part_2}")


if __name__ == "__main__":
    for input_filename in [
        "sample.txt",
        "input.txt"
    ]:
        print(f"-- {input_filename} --")
        main(input_filename)
