import operator
import re
from functools import reduce


CHRISTMAS_TREE = """
###############################
#                             #
#                             #
#                             #
#                             #
#              #              #
#             ###             #
#            #####            #
#           #######           #
#          #########          #
#            #####            #
#           #######           #
#          #########          #
#         ###########         #
#        #############        #
#          #########          #
#         ###########         #
#        #############        #
#       ###############       #
#      #################      #
#        #############        #
#       ###############       #
#      #################      #
#     ###################     #
#    #####################    #
#             ###             #
#             ###             #
#             ###             #
#                             #
#                             #
#                             #
#                             #
###############################
""".strip()


def part_1(robots, width, height):
    steps = 100
    width_half = (width + 1) // 2
    height_half = (height + 1) // 2
    quadrants = [0] * 4
    for px, py, vx, vy in robots:
        x = (px + steps * vx) % width
        y = (py + steps * vy) % height
        if x % width_half < width_half - 1 and y % height_half < height_half - 1:
            quadrants[x // width_half + 2 * (y // height_half)] += 1
    return reduce(operator.mul, quadrants, 1)


def part_2(robots, width, height):
    # find positions where no robots overlap, this seems to be a reasonable assumption
    n = 1
    while True:
        positions = {
            ((px + n * vx) % width, (py + n * vy) % height)
            for px, py, vx, vy in robots
        }
        if len(positions) == len(robots):
            return n, positions
        n += 1


def contains_christmas_tree(positions, width, height):
    tree_rows = CHRISTMAS_TREE.split("\n")
    tree_height = len(tree_rows)
    tree_width = len(tree_rows[0])
    tree_row_positions = [
        [x for x, c in enumerate(row) if c == "#"]
        for y, row in enumerate(tree_rows)
    ]

    return any(
        all(
            {(a + x, b + y) for x in row}.issubset(positions)
            for y, row in enumerate(tree_row_positions)
        )
        for b in range(height - (tree_height - 1))
        for a in range(width - (tree_width - 1))
    )


def main(filename):
    with open(filename) as input_file:
        robots = [
            list(map(int, re.match(r"p=(\d+),(\d+) v=([-+]?\d+),([-+]?\d+)", line).groups()))
            for line in input_file
        ]

    if filename == "sample.txt":
        width, height = 11, 7
    else:
        width, height = 101, 103

    result_part_1 = part_1(robots, width, height)
    print(f"part 1: {result_part_1}")

    # these result actually only make sense for input.txt
    result_part_2, positions = part_2(robots, width, height)
    if filename == "input.txt":
        assert contains_christmas_tree(positions, width, height)
    print(f"part 2: {result_part_2}")


if __name__ == "__main__":
    for input_filename in [
        "sample.txt",
        "input.txt"
    ]:
        print(f"-- {input_filename} --")
        main(input_filename)
