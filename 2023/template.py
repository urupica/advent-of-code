def main1():
    total = 0

    with open("sample.txt") as input_file:
        for row in input_file:
            row = row.strip()

    print(total)


def main2():
    pass


if __name__ == "__main__":
    main1()
