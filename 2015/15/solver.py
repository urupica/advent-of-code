import re


def create_amounts(size, total, partial=(), calories=None):
    if len(partial) == size - 1:
        amounts = partial + (total - sum(partial),)
        if not calories or sum(a * b for a, b in zip(amounts, calories)) == 500:
            yield amounts
    else:
        for n in range(total - sum(partial) + 1):
            yield from create_amounts(size, total, partial + (n,), calories=calories)


def find_best(ingredients, add_calories=False):
    if add_calories:
        calories = tuple(cal for *_, cal in ingredients)
    else:
        calories = None

    best = 0
    for amounts in create_amounts(len(ingredients), 100, calories=calories):
        total = 1
        for i in range(4):
            total *= max(sum(amount * properties[i] for amount, properties in zip(amounts, ingredients)), 0)
        best = max(best, total)
    return best


def solve(filename):
    ingredients = []
    with open(filename) as input_file:
        for line in input_file:
            line = line.strip()
            pattern = r"capacity (-?\d+), durability (-?\d+), flavor (-?\d+), texture (-?\d+), calories (-?\d+)"
            properties = tuple(map(int, re.search(pattern, line).groups()))
            ingredients.append(properties)

    best = find_best(ingredients)
    print(f"part 1: {best}")

    best = find_best(ingredients, add_calories=True)
    print(f"part 2: {best}")


def main():
    for filename in [
        "sample.txt",
        "input.txt"
    ]:
        print(f"-- {filename} --")
        solve(filename)


if __name__ == "__main__":
    main()
    # print(list(create_amounts(2, 100, calories=(3, 8))))
