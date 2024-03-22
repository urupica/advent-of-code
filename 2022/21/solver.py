from functools import cache
from collections import deque

monkey_yell = None
monkey_operations = None


@cache
def get_monkey_yell(monkey):
    if monkey in monkey_yell:
        return monkey_yell[monkey]

    monkey1, monkey2, operation = monkey_operations[monkey]
    yell1 = get_monkey_yell(monkey1)
    yell2 = get_monkey_yell(monkey2)
    if operation == "+":
        return yell1 + yell2
    if operation == "-":
        return yell1 - yell2
    if operation == "*":
        return yell1 * yell2
    return yell1 // yell2


def solve():
    parent = {}
    queue = deque(["root"])
    operations_stack = []
    while queue:
        monkey = queue.popleft()
        # print("  ", monkey)
        if monkey in monkey_yell:
            continue
        monkey1, monkey2, operation = monkey_operations[monkey]
        queue.extend([monkey1, monkey2])
        operations_stack.append((monkey1, monkey2, operation))
        parent[monkey1] = monkey
        parent[monkey2] = monkey

    operations = []
    target = None
    while operations_stack:
        monkey1, monkey2, operation = operations_stack.pop()
        yell1 = monkey_yell[monkey1]
        yell2 = monkey_yell[monkey2]
        if yell1 is None or yell2 is None:
            if yell1 is None:
                if operation == "+":
                    operations.append(("-", yell2))
                elif operation == "-":
                    operations.append(("+", yell2))
                elif operation == "*":
                    operations.append(("/", yell2))
                elif operation == "/":
                    operations.append(("*", yell2))
                else:
                    target = yell2
            else:
                if operation == "+":
                    operations.append(("-", yell1))
                elif operation == "-":
                    operations.append(("-2", yell1))
                elif operation == "*":
                    operations.append(("/", yell1))
                elif operation == "/":
                    operations.append(("/2", yell1))
                else:
                    target = yell1
            monkey_yell[parent[monkey1]] = None
        else:
            if operation == "+":
                parent_yell = yell1 + yell2
            elif operation == "-":
                parent_yell = yell1 - yell2
            elif operation == "*":
                parent_yell = yell1 * yell2
            else:
                parent_yell = yell1 // yell2
            monkey_yell[parent[monkey1]] = parent_yell

    while operations:
        operation, yell = operations.pop()
        if operation == "+":
            target += yell
        elif operation == "-":
            target -= yell
        elif operation == "*":
            target *= yell
        elif operation == "/":
            target //= yell
        elif operation == "-2":
            target = yell - target
        else:
            target = yell // target

    return target


def main(filename):
    global monkey_yell, monkey_operations
    monkey_yell = {}
    monkey_operations = {}
    with open(filename) as input_file:
        for line in input_file:
            monkey, value = line.strip().split(": ")
            try:
                number = int(value)
                monkey_yell[monkey] = number
            except ValueError:
                monkey1, operation, monkey2 = value.split()
                monkey_operations[monkey] = (monkey1, monkey2, operation)

    get_monkey_yell.cache_clear()
    result_part_1 = get_monkey_yell("root")
    print(f"part 1: {result_part_1}")

    monkey_yell["humn"] = None
    monkey_operations["root"] = monkey_operations["root"][:-1] + ("=",)
    result_part_2 = solve()
    print(f"part 2: {result_part_2}")


if __name__ == "__main__":
    for input_filename in [
        "sample.txt",
        "input.txt"
    ]:
        print(f"-- {input_filename} --")
        main(input_filename)
