def main1():
    total = 0
    with open("input.txt") as input_file:
        rows = [line.strip() for line in input_file]
        for i, row in enumerate(rows):
            j = 0
            while j < len(row):
                if not row[j].isdigit():
                    j += 1
                    continue
                k = j + 1
                while k < len(row) and row[k].isdigit():
                    k += 1
                symbol_found = False
                for ii in range(max(0, i - 1), min(len(rows), i + 2)):
                    for jj in range(max(0, j - 1), min(len(row), k + 1)):
                        if rows[ii][jj] not in "0123456789.":
                            symbol_found = True
                            break
                    if symbol_found:
                        break
                if symbol_found:
                    number = int(row[j:k])
                    total += number
                j = k
    print(total)


def main2():
    total = 0
    with open("input.txt") as input_file:
        rows = [line.strip() for line in input_file]
        numbers = []
        for i, row in enumerate(rows):
            j = 0
            while j < len(row):
                if not row[j].isdigit():
                    j += 1
                    continue
                k = j + 1
                while k < len(row) and row[k].isdigit():
                    k += 1
                symbol_found = False
                for ii in range(max(0, i - 1), min(len(rows), i + 2)):
                    for jj in range(max(0, j - 1), min(len(row), k + 1)):
                        if rows[ii][jj] not in "0123456789.":
                            symbol_found = True
                            break
                    if symbol_found:
                        break
                if symbol_found:
                    number = int(row[j:k])
                    numbers.append((i, j, k - 1, number))
                j = k

        for ii, row in enumerate(rows):
            for jj, x in enumerate(row):
                if x == "*":
                    adjacent_numbers = []
                    for i, j, k, number in numbers:
                        if abs(i - ii) <= 1 and j - 1 <= jj <= k + 1:
                            adjacent_numbers.append(number)
                    if len(adjacent_numbers) == 2:
                        total += adjacent_numbers[0] * adjacent_numbers[1]

    print(total)


if __name__ == "__main__":
    main2()
