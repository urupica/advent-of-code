from dataclasses import dataclass


@dataclass
class Obstruction:
    i: int
    j: int
    size: int

    def overlaps(self, other):
        if self.size == 1:
            return self.i == other.i and self.j == other.j
        return self.i == other.i and abs(self.j - other.j) <= 1

    def overlaps_after_move(self, other, direction):
        other_i, other_j = {
            "v": (other.i + 1, other.j),
            "^": (other.i - 1, other.j),
            ">": (other.i, other.j + 1),
            "<": (other.i, other.j - 1),
        }[direction]
        if self.size == 1:
            return self.i == other_i and self.j == other_j
        return self.i == other_i and abs(self.j - other_j) <= 1

    def contains(self, coordinates):
        i, j = coordinates
        if self.size == 1:
            return self.i == i and self.j == j
        return self.i == i and self.j <= j <= self.j + 1

    def move(self, direction):
        if direction == "v":
            self.i += 1
        elif direction == "^":
            self.i -= 1
        elif direction == ">":
            self.j += 1
        else:
            self.j -= 1

    def copy(self):
        return Obstruction(self.i, self.j, self.size)

    def __hash__(self):
        return self.i * 100 + self.j


def simulate(walls, boxes, robot, movements, size):
    for direction in movements:
        robot_next = {
            "v": (robot[0] + 1, robot[1]),
            "^": (robot[0] - 1, robot[1]),
            ">": (robot[0], robot[1] + 1),
            "<": (robot[0], robot[1] - 1),
        }[direction]
        if not any(box.contains(robot_next) for box in boxes) and not any(wall.contains(robot_next) for wall in walls):
            # next position is free, just move.
            robot = robot_next
            continue

        if any(wall.contains(robot_next) for wall in walls):
            # next position is blocked by a wall, do nothing.
            continue

        pool = [next(box for box in boxes if box.contains(robot_next))]
        visited = set()
        can_move = True
        while pool:
            box = pool.pop()
            if box in visited:
                continue
            visited.add(box)
            if any(w.overlaps_after_move(box, direction) for w in walls):
                can_move = False
                break
            for box_obstructing in [b for b in boxes if b.overlaps_after_move(box, direction)]:
                if box_obstructing not in pool and box_obstructing not in visited:
                    pool.append(box_obstructing)
        if can_move:
            for box in visited:
                box.move(direction)
            robot = robot_next


def gps_sum(boxes):
    return sum(100 * box.i + box.j for box in boxes)


def main(filename):
    walls = []
    boxes = []
    robot = None
    movements = ""

    # size = 2 if filename == "input.txt" else 1
    with open(filename) as input_file:
        is_grid_input = True
        for i, line in enumerate(input_file):
            line = line.strip()
            if not line:
                is_grid_input = False
            elif is_grid_input:
                for j, x in enumerate(line):
                    if x == "#":
                        walls.append(Obstruction(i, j, 1))
                    elif x == "O":
                        boxes.append(Obstruction(i, j, 1))
                    elif x == "@":
                        robot = (i, j)
            else:
                movements += line

    boxes_copy = [box.copy() for box in boxes]
    simulate(walls, boxes_copy, robot, movements, 1)
    result_part_1 = gps_sum(boxes_copy)
    print(f"part 1: {result_part_1}")

    for obj in boxes + walls:
        obj.j *= 2
        obj.size = 2
    robot = (robot[0], robot[1] * 2)

    simulate(walls, boxes, robot, movements, 2)
    result_part_2 = gps_sum(boxes)
    print(f"part 2: {result_part_2}")


if __name__ == "__main__":
    for input_filename in [
        "sample.txt",
        "input.txt"
    ]:
        print(f"-- {input_filename} --")
        main(input_filename)
