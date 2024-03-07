def _return_digit_or_none(line, i):
    if line[i].isdigit():
        return int(line[i])

    digits_as_letters = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for digit, word in enumerate(digits_as_letters, start=1):
        if word == line[i:i + len(word)]:
            return digit


def main():
    total = 0

    with open("input.txt") as input_file:
        for line in input_file:
            for i in range(len(line)):
                digit_or_none = _return_digit_or_none(line, i)
                if digit_or_none is not None:
                    total += 10 * digit_or_none
                    break

            for i in range(len(line) - 1, -1, -1):
                digit_or_none = _return_digit_or_none(line, i)
                if digit_or_none is not None:
                    total += digit_or_none
                    break

    print(total)


if __name__ == "__main__":
    main()
