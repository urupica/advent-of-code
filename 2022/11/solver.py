import operator
from functools import reduce


class Monkey:
    lcm = None

    def __init__(self, items, operation, divisor, targets):
        self.items_1 = list(items)
        self.items_2 = list(items)
        self.operation = operation
        self.divisor = divisor
        self.targets = targets
        self.inspected_items_1 = 0
        self.inspected_items_2 = 0

    def apply_operation(self, item, is_part_1=True):
        op, val = self.operation
        if op == "+":
            if val == "old":
                item += item
            else:
                item += int(val)
        else:
            if val == "old":
                item *= item
            else:
                item *= int(val)

        if is_part_1:
            item //= 3

        test_result = item % self.divisor == 0

        target = {
            True: self.targets[0],
            False: self.targets[1],
        }[test_result]

        return target, item % self.lcm


def main(filename):
    monkeys = []

    with open(filename) as input_file:
        items = operation = divisor = target_true = None
        for line_count, line in enumerate(input_file):
            line = line.strip()
            if line_count % 7 == 1:
                items = list(int(n) for n in line[16:].split(", "))
            elif line_count % 7 == 2:
                op = line[21]
                val = line[23:]
                operation = (op, val)
            elif line_count % 7 == 3:
                divisor = int(line[19:])
            elif line_count % 7 == 4:
                target_true = int(line[25:])
            elif line_count % 7 == 5:
                target_false = int(line[25:])
                targets = (target_true, target_false)
                monkey = Monkey(items, operation, divisor, targets)
                monkeys.append(monkey)
                items = operation = divisor = target_true = None

    Monkey.lcm = reduce(operator.mul, (monkey.divisor for monkey in monkeys))

    for round_counter in range(10_000):
        for monkey in monkeys:
            if round_counter < 20:
                while monkey.items_1:
                    item = monkey.items_1.pop(0)
                    target_monkey_id, item = monkey.apply_operation(item)
                    monkeys[target_monkey_id].items_1.append(item)
                    monkey.inspected_items_1 += 1

            while monkey.items_2:
                item = monkey.items_2.pop(0)
                target_monkey_id, item = monkey.apply_operation(item, is_part_1=False)
                monkeys[target_monkey_id].items_2.append(item)
                monkey.inspected_items_2 += 1

    ins1, ins2 = sorted(monkey.inspected_items_1 for monkey in monkeys)[-2:]
    result_part_1 = ins1 * ins2

    ins1, ins2 = sorted(monkey.inspected_items_2 for monkey in monkeys)[-2:]
    result_part_2 = ins1 * ins2

    print(f"part 1: {result_part_1}")
    print(f"part 2: {result_part_2}")


if __name__ == "__main__":
    for name in [
        "sample.txt",
        "input.txt"
    ]:
        print(f"-- {name} --")
        main(name)
