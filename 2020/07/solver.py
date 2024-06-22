import re


def contains_shiny_gold_bag(bags, bag_color):
    return any(
        bag_color_inside == "shiny gold" or contains_shiny_gold_bag(bags, bag_color_inside)
        for bag_color_inside in bags[bag_color]
    )


def count_bags_inside(bags, bag_color):
    return sum(
        count + count * count_bags_inside(bags, bag_color_inside)
        for bag_color_inside, count in bags[bag_color].items()
    )


def main(filename):
    with open(filename) as input_file:
        bags = {}
        for line in input_file:
            line = line.strip()
            result = re.match(r"([a-z ]+) bags contain? (.+)\.", line)
            bag_color, bags_inside = result.groups()
            bags[bag_color] = {}
            if bags_inside != "no other bags":
                for count, bag_inside_color in re.findall(r"(\d+) ([a-z ]+) bags?", bags_inside):
                    bags[bag_color][bag_inside_color] = int(count)

    result_part_1 = sum(contains_shiny_gold_bag(bags, bag_color) for bag_color in bags)
    print(f"part 1: {result_part_1}")

    result_part_2 = count_bags_inside(bags, "shiny gold")
    print(f"part 2: {result_part_2}")


if __name__ == "__main__":
    for input_filename in [
        "sample.txt",
        "input.txt"
    ]:
        print(f"-- {input_filename} --")
        main(input_filename)
