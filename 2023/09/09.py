def main1():
    total = 0
    with open("input.txt") as input_file:
        for row in input_file:
            sequences = [[int(x) for x in row.strip().split()]]
            while not all(x == 0 for x in sequences[-1]):
                last_row = sequences[-1]
                sequences.append([b - a for a, b in zip(last_row[:-1], last_row[1:])])
            sequences[-1].append(0)
            i = len(sequences) - 2
            while i >= 0:
                sequences[i].append(sequences[i][-1] + sequences[i + 1][-1])
                i -= 1
            total += sequences[0][-1]
    print(total)


def main2():
    total = 0
    with open("input.txt") as input_file:
        for row in input_file:
            sequences = [[int(x) for x in row.strip().split()]]
            while not all(x == 0 for x in sequences[-1]):
                last_row = sequences[-1]
                sequences.append([b - a for a, b in zip(last_row[:-1], last_row[1:])])
            sequences[-1].insert(0, 0)
            i = len(sequences) - 2
            while i >= 0:
                sequences[i].insert(0, sequences[i][0] - sequences[i + 1][0])
                i -= 1
            total += sequences[0][0]
    print(total)


if __name__ == "__main__":
    main2()
