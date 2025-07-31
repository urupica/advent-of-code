from math import ceil

SHOP = """Weapons:    Cost  Damage  Armor
Dagger        8     4       0
Shortsword   10     5       0
Warhammer    25     6       0
Longsword    40     7       0
Greataxe     74     8       0

Armor:      Cost  Damage  Armor
Leather      13     0       1
Chainmail    31     0       2
Splintmail   53     0       3
Bandedmail   75     0       4
Platemail   102     0       5

Rings:      Cost  Damage  Armor
Damage +1    25     1       0
Damage +2    50     2       0
Damage +3   100     3       0
Defense +1   20     0       1
Defense +2   40     0       2
Defense +3   80     0       3
"""


def solve(filename):
    with open(filename) as input_file:
        for i, line in enumerate(input_file):
            if i == 0:
                boss_hit_points = int(line.strip().replace("Hit Points: ", ""))
            elif i == 1:
                damage = int(line.strip().replace("Damage: ", ""))
            else:
                armor = int(line.strip().replace("Armor: ", ""))

    shop_weapons = []
    shop_armour = []
    shop_rings = []
    lines = SHOP.split("\n")
    for lst, lower, upper, offset in [
        (shop_weapons, 1, 5, 1),
        (shop_armour, 8, 12, 1),
        (shop_rings, 15, 20, 2),
    ]:
        for line in lines[lower:upper + 1]:
            lst.append(list(map(int, line.split()[offset:])))
    shop_armour.append((0, 0, 0))
    shop_rings.append((0, 0, 0))

    best = 1_000
    worst = 0
    for w_c, w_d, w_a in shop_weapons:
        for a_c, a_d, a_a in shop_armour:
            for i, (r1_c, r1_d, r1_a) in enumerate(shop_rings):
                for j, (r2_c, r2_d, r2_a) in enumerate(shop_rings):
                    if i == j:
                        continue
                    cost = w_c + a_c + r1_c + r2_c
                    my_damage = w_d + a_d + r1_d + r2_d
                    my_armor = w_a + a_a + r1_a + r2_a
                    my_hits = max(1, my_damage - armor)
                    boss_hits = max(1, damage - my_armor)
                    my_hit_count = ceil(boss_hit_points / my_hits)
                    boss_hit_count = ceil(100 / boss_hits)
                    if my_hit_count <= boss_hit_count:
                        best = min(best, cost)
                    else:
                        worst = max(worst, cost)

    print(f"part 1: {best}")
    print(f"part 2: {worst}")


def main():
    for filename in [
        # "sample.txt",
        "input.txt"
    ]:
        print(f"-- {filename} --")
        solve(filename)


if __name__ == "__main__":
    main()
