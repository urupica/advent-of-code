def apply_instruction(instructions, accumulator, current_line):
    inst, val = instructions[current_line]
    if inst == "acc":
        accumulator += val
        current_line += 1
    elif inst == "jmp":
        current_line += val
    else:
        current_line += 1
    return accumulator, current_line


def main(filename):
    with open(filename) as input_file:
        instructions = []
        for line in input_file:
            inst, val = line.strip().split()
            instructions.append([inst, int(val)])

    accumulator = 0
    visited_lines = set()
    current_line = 0
    while current_line not in visited_lines:
        visited_lines.add(current_line)
        accumulator, current_line = apply_instruction(instructions, accumulator, current_line)
    print(f"part 1: {accumulator}")

    result_part_2 = None
    jmp_nop_lines = [(i, inst) for i, (inst, _) in enumerate(instructions) if inst in ["jmp", "nop"]]
    for i, instruction in jmp_nop_lines:
        instructions[i][0] = "nop" if instruction == "jmp" else "jmp"

        accumulator = 0
        current_line = 0
        visited_lines = set()
        while current_line not in visited_lines and current_line < len(instructions):
            visited_lines.add(current_line)
            accumulator, current_line = apply_instruction(instructions, accumulator, current_line)

        instructions[i][0] = instruction

        if current_line == len(instructions):
            result_part_2 = accumulator
            break
    print(f"part 2: {result_part_2}")


if __name__ == "__main__":
    for input_filename in [
        "sample.txt",
        "input.txt"
    ]:
        print(f"-- {input_filename} --")
        main(input_filename)
