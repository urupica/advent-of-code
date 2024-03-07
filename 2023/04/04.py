import re
from collections import defaultdict


def main1():
    total = 0
    with open("input.txt") as input_file:
        for i, row in enumerate(input_file, start=1):
            row = re.sub("Card\s+\d+:", "", row, 1)
            winning, have = [part.strip() for part in row.split("|")]
            winning = {int(part) for part in winning.split()}
            have = [int(part) for part in have.split()]
            winning_numbers = len([n for n in have if n in winning])
            if winning_numbers > 0:
                total += 2 ** (winning_numbers - 1)
    print(total)


def main2():
    card_count = defaultdict(int)
    with open("input.txt") as input_file:
        for i, row in enumerate(input_file, start=1):
            card_count[i] += 1
            row = re.sub("Card\s+\d+:", "", row, 1)
            winning, have = [part.strip() for part in row.split("|")]
            winning = {int(part) for part in winning.split()}
            have = [int(part) for part in have.split()]
            winning_numbers = len([n for n in have if n in winning])
            for j in range(i + 1, i + winning_numbers + 1):
                card_count[j] += card_count[i]
    print(sum(card_count.values()))


if __name__ == "__main__":
    main2()
