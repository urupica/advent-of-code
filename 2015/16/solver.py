import re


def solve(filename):
    aunts = []
    with open(filename) as input_file:
        for line in input_file:
            line = line.strip()
            aunt = {}
            for compund in [
                "children",
                "cats",
                "samoyeds",
                "pomeranians",
                "akitas",
                "vizslas",
                "goldfish",
                "trees",
                "cars",
                "perfumes",
            ]:
                result = re.search(rf"{compund}: (\d+)", line)
                if result:
                    aunt[compund] = int(result.group(1))
            aunts.append(aunt)

    detected_aunt = {
        "children": 3,
        "cats": 7,
        "samoyeds": 2,
        "pomeranians": 3,
        "akitas": 0,
        "vizslas": 0,
        "goldfish": 5,
        "trees": 3,
        "cars": 2,
        "perfumes": 1,
    }
    for n, aunt in enumerate(aunts, start=1):
        if all(detected_aunt[k] == v for k, v in aunt.items()):
            print(f"part 1: {n}")

    for n, aunt in enumerate(aunts, start=1):
        if all(
                (
                    detected_aunt[k] < v if k in ["cats", "trees"]
                    else detected_aunt[k] > v if k in ["pomeranians", "goldfish"]
                    else detected_aunt[k] == v
                )
            for k, v in aunt.items()
        ):
            print(f"part 2: {n}")



def main():
    for filename in [
        "input.txt"
    ]:
        print(f"-- {filename} --")
        solve(filename)


if __name__ == "__main__":
    main()
