def main():
    with open("input.txt") as input_file:
        total_calories = []
        inventory = []
        for line in input_file:
            line = line.strip()
            if line:
                inventory.append(int(line))
            else:
                total_calories.append(sum(inventory))
                inventory = []

    total_calories.append(sum(inventory))
    total_calories.sort()

    print(f"part 1: {total_calories[-1]}")
    print(f"part 2: {sum(total_calories[-3:])}")


if __name__ == "__main__":
    main()
