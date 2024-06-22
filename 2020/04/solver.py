import re


def main(filename):
    with open(filename) as input_file:
        passports = []
        current_passport = []
        for line in input_file:
            line = line.strip()
            if not line:
                passports.append(dict(current_passport))
                current_passport = []
            else:
                parts = line.split()
                for part in parts:
                    current_passport.append((part[:3], part[4:]))
        if current_passport:
            passports.append(dict(current_passport))

    result_part_1 = sum(
        {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}.issubset(passport)
        for passport in passports
    )

    result_part_2 = 0
    for passport in passports:
        if not {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}.issubset(passport):
            continue

        result = re.match(r"^([0-9]{4})$", passport["byr"])
        if not result or not 1290 <= int(result.group(1)) <= 2002:
            continue

        result = re.match(r"^([0-9]{4})$", passport["iyr"])
        if not result or not 2010 <= int(result.group(1)) <= 2020:
            continue

        result = re.match(r"^([0-9]{4})$", passport["eyr"])
        if not result or not 2020 <= int(result.group(1)) <= 2030:
            continue

        result = re.match(r"^([0-9]+)(cm|in)$", passport["hgt"])
        if not result:
            continue
        hgt = int(result.group(1))
        unit = result.group(2)
        if unit == "cm" and not 150 <= hgt <= 193:
            continue
        if unit == "in" and not 59 <= hgt <= 76:
            continue

        if not re.match(r"^#[0-9a-f]{6}$", passport["hcl"]):
            continue

        if not re.match(r"^amb|blu|brn|gry|grn|hzl|oth$", passport["ecl"]):
            continue

        if not re.match(r"^\d{9}$", passport["pid"]):
            continue

        result_part_2 += 1

    print(f"part 1: {result_part_1}")
    print(f"part 2: {result_part_2}")


if __name__ == "__main__":
    for input_filename in [
        "sample.txt",
        "input.txt"
    ]:
        print(f"-- {input_filename} --")
        main(input_filename)
