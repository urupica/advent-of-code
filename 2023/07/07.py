from collections import Counter
from functools import cmp_to_key


def hand_compare_1(hand1, hand2):
    def rank_counter(c):
        if len(c) == 5:
            return 1
        if len(c) == 4:
            return 2
        if len(c) == 3 and max(c.values()) == 2:
            return 3
        if len(c) == 3 and max(c.values()) == 3:
            return 4
        if len(c) == 2 and max(c.values()) == 3:
            return 5
        if len(c) == 2 and max(c.values()) == 4:
            return 6
        return 7

    c1 = Counter(hand1[0])
    c2 = Counter(hand2[0])
    r1 = rank_counter(c1)
    r2 = rank_counter(c2)
    if r1 > r2:
        return 1
    if r1 < r2:
        return -1

    cards = "23456789TJQKA"
    for x1, x2 in zip(hand1[0], hand2[0]):
        if x1 != x2:
            return cards.index(x1) - cards.index(x2)

    return 0


def hand_compare_2(hand1, hand2):
    def rank_counter(c):
        if len(c) == 5:
            return 1
        if len(c) == 4:
            return 2
        if len(c) == 3 and max(c.values()) == 2:
            return 3
        if len(c) == 3 and max(c.values()) == 3:
            return 4
        if len(c) == 2 and max(c.values()) == 3:
            return 5
        if len(c) == 2 and max(c.values()) == 4:
            return 6
        return 7

    h1 = list(hand1[0])
    h2 = list(hand2[0])
    j1 = j2 = 0
    while "J" in h1:
        h1.remove("J")
        j1 += 1
    while "J" in h2:
        h2.remove("J")
        j2 += 1

    c1 = Counter(h1)
    c2 = Counter(h2)
    if j1 == 5:
        c1["A"] = 5
    elif j1 > 0:
        k = max(c1, key=c1.get)
        c1[k] += j1
    if j2 == 5:
        c2["A"] = 5
    elif j2 > 0:
        k = max(c2, key=c2.get)
        c2[k] += j2

    r1 = rank_counter(c1)
    r2 = rank_counter(c2)
    if r1 > r2:
        return 1
    if r1 < r2:
        return -1

    cards = "J23456789TQKA"
    for x1, x2 in zip(hand1[0], hand2[0]):
        if x1 != x2:
            return cards.index(x1) - cards.index(x2)

    return 0


def main1():
    hands = []
    with open("input.txt") as input_file:
        for row in input_file:
            row = row.strip()
            hand, bid = [x.strip() for x in row.split()]
            bid = int(bid)
            hands.append((hand, bid))

    hands.sort(key=cmp_to_key(hand_compare_1))

    total = 0
    for r, (_, bid) in enumerate(hands, start=1):
        total += r * bid
    print(total)


def main2():
    hands = []
    with open("input.txt") as input_file:
        for row in input_file:
            row = row.strip()
            hand, bid = [x.strip() for x in row.split()]
            bid = int(bid)
            hands.append((hand, bid))

    hands.sort(key=cmp_to_key(hand_compare_2))

    total = 0
    for r, (_, bid) in enumerate(hands, start=1):
        total += r * bid
    print(total)


if __name__ == "__main__":
    main2()
