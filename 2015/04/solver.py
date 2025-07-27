import hashlib

def solve(filename):
    with open(filename) as input_file:
        for line in input_file:
            line = line.strip()

    n = 1
    part1_found = False
    while True:
        md5sum = hashlib.md5(f"{line}{n}".encode('utf-8')).hexdigest()
        if md5sum.startswith("0" * 5) and not part1_found:
            print(f"part 1: {n}")
            part1_found = True
        if md5sum.startswith("0" * 6):
            print(f"part 2: {n}")
            break
        n += 1


def main():
    for filename in [
        "sample.txt",
        "input.txt"
    ]:
        print(f"-- {filename} --")
        solve(filename)


if __name__ == "__main__":
    main()
