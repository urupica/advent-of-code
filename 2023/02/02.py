import operator
from functools import reduce


def main1():
    total = 0
    with open("input.txt") as input_file:
        for i, line in enumerate(input_file, start=1):
            prefix = f"Game {i}: "
            assert line.startswith(prefix)
            line = line.strip()
            line = line.replace(prefix, "")
            parts = [part.strip() for part in line.split(";")]
            possible = True
            for part in parts:
                counts = [count.strip() for count in part.split(",")]
                for count in counts:
                    if count.endswith(" red"):
                        number = int(count.replace(" red", ""))
                        if number > 12:
                            possible = False
                            break
                    elif count.endswith(" green"):
                        number = int(count.replace(" green", ""))
                        if number > 13:
                            possible = False
                            break
                    elif count.endswith(" blue"):
                        number = int(count.replace(" blue", ""))
                        if number > 14:
                            possible = False
                            break
                if not possible:
                    break
            if possible:
                total += i
    print(total)


def main2():
    total = 0
    with open("input.txt") as input_file:
        for i, line in enumerate(input_file, start=1):
            prefix = f"Game {i}: "
            assert line.startswith(prefix)
            line = line.strip()
            line = line.replace(prefix, "")
            parts = [part.strip() for part in line.split(";")]
            maximum = {"red": 0, "green": 0, "blue": 0}
            for part in parts:
                counts = [count.strip() for count in part.split(",")]
                for count in counts:
                    if count.endswith(" red"):
                        number = int(count.replace(" red", ""))
                        maximum["red"] = max(maximum["red"], number)
                    elif count.endswith(" green"):
                        number = int(count.replace(" green", ""))
                        maximum["green"] = max(maximum["green"], number)
                    elif count.endswith(" blue"):
                        number = int(count.replace(" blue", ""))
                        maximum["blue"] = max(maximum["blue"], number)
            power = reduce(operator.mul, maximum.values(), 1)
            total += power
    print(total)


if __name__ == "__main__":
    main2()
