from collections import defaultdict


def get_invalid_indexes(rules, numbers):
    indexes = {n: i for i, n in enumerate(numbers)}
    for i, n in enumerate(numbers):
        for m in rules[n]:
            j = indexes.get(m)
            if j is not None and j < i:
                return j, i
    return None


def repair(rules, numbers):
    has_been_repaired = False
    while True:
        invalid_indexes = get_invalid_indexes(rules, numbers)
        if invalid_indexes is None:
            break

        j, i = invalid_indexes
        numbers[:] = numbers[:j] + [numbers[i]] + numbers[j + 1:i] + [numbers[j]] + numbers[i + 1:]
        has_been_repaired = True
    return has_been_repaired


def sum_middle_numbers(orders):
    return sum(numbers[len(numbers) // 2] for numbers in orders)


def main(filename):
    rules = defaultdict(list)
    orders = []
    is_rules_section = True
    with open(filename) as input_file:
        for line in input_file:
            line = line.strip()
            if not line:
                is_rules_section = False
            elif is_rules_section:
                n, m = map(int, line.split("|"))
                rules[n].append(m)
            else:
                numbers = list(map(int, line.split(",")))
                orders.append(numbers)

    valid_orders = []
    repaired_orders = []
    for numbers in orders:
        has_been_repaired = repair(rules, numbers)
        if not has_been_repaired:
            valid_orders.append(numbers)
        else:
            repaired_orders.append(numbers)

    result_part_1 = sum_middle_numbers(valid_orders)
    print(f"part 1: {result_part_1}")

    result_part_2 = sum_middle_numbers(repaired_orders)
    print(f"part 2: {result_part_2}")


if __name__ == "__main__":
    for input_filename in [
        "sample.txt",
        "input.txt"
    ]:
        print(f"-- {input_filename} --")
        main(input_filename)
