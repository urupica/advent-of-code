from collections import deque
from itertools import islice, combinations
from string import ascii_lowercase


def get_next_char(char):
    return ascii_lowercase[ascii_lowercase.index(char) + 1]


def get_next_password(password):
    if password[-1] != "z":
        password = password[:-1] + get_next_char(password[-1])
    else:
        password = password[:-1] + "a"
        i = len(password) - 2
        while True:
            if password[i] != "z":
                password = password[:i] + get_next_char(password[i]) + password[i + 1:]
                break
            else:
                password = password[:i] + "a" + password[i + 1:]
            i -= 1
    return password


def sliding_window(iterable, n):
    iterator = iter(iterable)
    window = deque(islice(iterator, n - 1), maxlen=n)
    for x in iterator:
        window.append(x)
        yield "".join(window)


def is_valid(password):
    return all(
        [
            any(window in password for window in sliding_window(ascii_lowercase, 3)),
            all(x not in password for x in "iol"),
            any(x*2 in password and y*2 in password for x, y in combinations(ascii_lowercase, 2)),
        ]
    )


def get_next_valid_password(password):
    while True:
        password = get_next_password(password)
        if is_valid(password):
            return password


def solve(filename):
    with open(filename) as input_file:
        password = next(input_file).strip()

    password = get_next_valid_password(password)
    print(f"part 1: {password}")

    password = get_next_valid_password(password)
    print(f"part 2: {password}")


def main():
    for filename in [
        "sample.txt",
        "input.txt"
    ]:
        print(f"-- {filename} --")
        solve(filename)


if __name__ == "__main__":
    main()
