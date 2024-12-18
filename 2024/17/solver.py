import re


def get_combo_operand(operand, registers):
    assert operand <= 6
    if operand <= 3:
        return operand
    return registers[operand - 4]


def execute(opcode, operand, registers):
    return_value = None
    next_index = None

    if opcode == 0:
        registers[0] //= (2 ** get_combo_operand(operand, registers))
    elif opcode == 1:
        registers[1] ^= operand
    elif opcode == 2:
        registers[1] = get_combo_operand(operand, registers) % 8
    elif opcode == 3:
        if registers[0] != 0:
            next_index = operand
    elif opcode == 4:
        registers[1] ^= registers[2]
    elif opcode == 5:
        return_value = get_combo_operand(operand, registers) % 8
    elif opcode == 6:
        registers[1] = registers[0] // (2 ** get_combo_operand(operand, registers))
    elif opcode == 7:
        registers[2] = registers[0] // (2 ** get_combo_operand(operand, registers))

    return return_value, next_index


def run_program(registers, program):
    output = []
    i = 0
    while i < len(program):
        opcode, operand = program[i:i + 2]
        return_value, next_index = execute(opcode, operand, registers)
        if next_index is not None:
            i = next_index
        else:
            i += 2
        if return_value is not None:
            output.append(return_value)
    return output


def brute_force_solution(registers, program):
    a = 1
    while True:
        registers[0] = a
        if run_program(registers, program) == program:
            return a
        a += 1


def get_goal_candidates():
    # this is hard-coded for input.txt
    candidates = {goal: [] for goal in range(8)}
    mask_length = 10
    for a in range(2 ** mask_length):
        c = a // (2 ** ((a % 8) ^ 2))
        b = (a % 8) ^ 2 ^ c ^ 7
        mask = tuple(map(int, (bin(a)[:1:-1])))
        mask += (0,) * (mask_length - len(mask))
        candidates[b % 8].append(mask)
    return candidates


def search(program, candidates, prefix=(), step=0):
    # look for solutions for input.txt
    goal = program[step]
    for mask in candidates[goal]:
        prefix_mask = tuple(prefix)
        valid = True
        for i, x in enumerate(mask):
            ii = i + 3 * step
            if ii >= len(prefix_mask):
                prefix_mask += (x,)
            elif prefix_mask[ii] != x:
                valid = False
                break
        if valid:
            if step == len(program) - 1:
                solution_candidate = sum(x * 2**i for i, x in enumerate(prefix_mask))
                registers = [solution_candidate, 0, 0]
                output = run_program(registers, program)
                if output == program:
                    yield solution_candidate
            else:
                yield from search(program, candidates, prefix_mask, step+1)


def main(filename):
    with open(filename) as input_file:
        register_data, program_data = input_file.read().split("\n\n")

    registers = list(map(int, re.findall(r"Register .: (\d+)", register_data)))
    program = list(map(int, re.findall(r"(\d+),?", program_data)))

    output = run_program(registers, program)
    result_part_1 = ",".join(map(str, output))
    print(f"part 1: {result_part_1}")

    if filename == "sample.txt":
        result_part_2 = brute_force_solution(registers, program)
    else:
        candidates = get_goal_candidates()
        result_part_2 = min(search(program, candidates))
    print(f"part 2: {result_part_2}")


if __name__ == "__main__":
    for input_filename in [
        "sample.txt",
        "input.txt"
    ]:
        print(f"-- {input_filename} --")
        main(input_filename)
