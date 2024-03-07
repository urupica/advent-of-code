import operator
from collections import defaultdict
from functools import reduce


def parse_input_part_1(filename):
    workflows = defaultdict(list)
    ratings = []
    with open(filename) as input_file:
        is_workflow = True
        for row in input_file:
            row = row.strip()
            if not row:
                is_workflow = False
            elif is_workflow:
                workflow_name, rules = row[:-1].split("{")
                for rule in rules.split(","):
                    if ":" in rule:
                        condition, target = rule.split(":")
                        if "<" in condition:
                            category, value = condition.split("<")
                            workflows[workflow_name].append((lambda part, cat=category, val=value: part[cat] < int(val), target))
                        else:
                            assert ">" in condition
                            category, value = condition.split(">")
                            workflows[workflow_name].append((lambda part, cat=category, val=value: part[cat] > int(val), target))
                    else:
                        target = rule
                        workflows[workflow_name].append((lambda part: True, target))
            else:
                part_ratings = {}
                for category_rating in row[1:-1].split(","):
                    category, rating = category_rating.split("=")
                    part_ratings[category] = int(rating)
                ratings.append(part_ratings)
    return workflows, ratings


def parse_input_part_2(filename):
    workflows = defaultdict(list)
    with open(filename) as input_file:
        for row in input_file:
            row = row.strip()
            if not row:
                break
            workflow_name, rules = row[:-1].split("{")
            for rule in rules.split(","):
                if ":" in rule:
                    condition, target = rule.split(":")
                    workflows[workflow_name].append((condition, target))
                else:
                    target = rule
                    workflows[workflow_name].append((None, target))
    return workflows


def main(filename):
    # part 1
    workflows, ratings = parse_input_part_1(filename)
    total = 0
    for part_ratings in ratings:
        workflow_name = "in"
        while workflow_name not in {"A", "R"}:
            for condition, target in workflows[workflow_name]:
                if condition(part_ratings):
                    workflow_name = target
                    break
        if workflow_name == "A":
            total += sum(part_ratings.values())
    print(f"part 1: {total}")

    # part 2
    workflows = parse_input_part_2(filename)
    total = 0
    pool = [(("in", 0), {"x": (1, 4000), "m": (1, 4000), "a": (1, 4000), "s": (1, 4000)})]
    while pool:
        (workflow_name, i), limits = pool.pop()

        if workflow_name in {"A", "R"}:
            if workflow_name == "A":
                total += reduce(operator.mul, (mx - mn + 1 for _, (mn, mx) in limits.items()))
            continue

        condition, target = workflows[workflow_name][i]

        if condition is None:
            pool.append(((target, 0), limits))
            continue

        if "<" in condition:
            category, value = condition.split("<")
            value = int(value)
            mn, mx = limits[category]
            if mn < value:
                limits_copy = dict(limits)
                limits_copy[category] = (mn, min(mx, value - 1))
                pool.append(((target, 0), limits_copy))
            if mx >= value:
                limits_copy = dict(limits)
                limits_copy[category] = (max(mn, value), mx)
                pool.append(((workflow_name, i + 1), limits_copy))
        else:
            assert ">" in condition
            category, value = condition.split(">")
            value = int(value)
            mn, mx = limits[category]
            if mx > value:
                limits_copy = dict(limits)
                limits_copy[category] = (max(mn, value + 1), mx)
                pool.append(((target, 0), limits_copy))
            if mn <= value:
                limits_copy = dict(limits)
                limits_copy[category] = (mn, min(mx, value))
                pool.append(((workflow_name, i + 1), limits_copy))

    print(f"part 2: {total}")


if __name__ == "__main__":
    main("input.txt")
