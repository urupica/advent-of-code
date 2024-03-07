def main(filename):
    with open(filename) as input_file:
        length = None
        stacks1 = None
        stacks2 = None
        is_arrangement = True
        for line in input_file:
            # part 1
            if length is None:
                length = len(line) // 4
                stacks1 = [[] for _ in range(length)]
                stacks2 = [[] for _ in range(length)]

            if not line.strip():
                is_arrangement = False
            elif is_arrangement:
                parts = [line[4 * k:4 * (k + 1)].strip() for k in range(length)]
                if parts[0] == "1":
                    continue
                for i, part in enumerate(parts):
                    if part:
                        stacks1[i].insert(0, part[1:-1])
                        stacks2[i].insert(0, part[1:-1])
            else:
                parts = line.strip().split()
                amount, from_stack, to_stack = int(parts[1]), int(parts[3]) - 1, int(parts[5]) - 1
                for _ in range(amount):
                    stacks1[to_stack].append(stacks1[from_stack].pop())
                stacks2[to_stack].extend(stacks2[from_stack][-amount:])
                del stacks2[from_stack][-amount:]

        part_1_top_crates = ""
        part_2_top_crates = ""
        for stack1, stack2 in zip(stacks1, stacks2):
            if stack1:
                part_1_top_crates += stack1[-1]
            if stack2:
                part_2_top_crates += stack2[-1]

    print(f"part 1: {part_1_top_crates}")
    print(f"part 2: {part_2_top_crates}")


if __name__ == "__main__":
    for filename in ["sample.txt", "input.txt"]:
        print(f"-- {filename} --")
        main(filename)
