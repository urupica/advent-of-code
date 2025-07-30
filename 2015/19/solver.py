from collections import defaultdict

fastest = None


def count_molecules(molecule, replacements):
    found_molecules = set()

    for orig, dest_list in replacements.items():
        orig_len = len(orig)
        for i in range(len(molecule)):
            if molecule[i:i + orig_len] == orig:
                for dest in dest_list:
                    found_molecules.add(molecule[:i] + dest + molecule[i + orig_len:])
    return len(found_molecules)


def find_fastest_creation(molecule, replacements):
    replacements_reversed = {}
    for orig, dest_list in replacements.items():
        for dest in dest_list:
            if orig != dest:
                assert dest not in replacements_reversed
                replacements_reversed[dest] = orig
    count = 0
    replacements_reversed = sorted(replacements_reversed.items(), key=lambda a: -len(a[0]))
    while molecule != "e":
        for orig, dest in replacements_reversed:
            if orig in molecule:
                molecule = molecule.replace(orig, dest, 1)
                count += 1
                break
    return count

def solve(filename):
    global fastest
    replacements = defaultdict(list)
    molecule = None
    with open(filename) as input_file:
        for line in input_file:
            line = line.strip()
            if not line:
                continue
            if " => " in line:
                orig, dest = line.split(" => ")
                replacements[orig].append(dest)
            else:
                molecule = line

    result_part_1 = count_molecules(molecule, replacements)
    print(f"part 1: {result_part_1}")

    fastest = None
    result_part_2 = find_fastest_creation(molecule, replacements)
    print(f"part 2: {result_part_2}")


def main():
    for filename in [
        "sample.txt",
        "input.txt"
    ]:
        print(f"-- {filename} --")
        solve(filename)


if __name__ == "__main__":
    main()
