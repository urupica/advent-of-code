def main(filename):
    with open(filename) as input_file:
        groups = [group.split("\n") for group in input_file.read().strip().split("\n\n")]

    result_part_1 = 0
    result_part_2 = 0
    for group in groups:
        questions = set()
        for answer in group:
            questions.update(answer)
        result_part_1 += len(questions)
        result_part_2 += len([q for q in questions if all(q in answer for answer in group)])

    print(f"part 1: {result_part_1}")
    print(f"part 2: {result_part_2}")


if __name__ == "__main__":
    for input_filename in [
        "sample.txt",
        "input.txt"
    ]:
        print(f"-- {input_filename} --")
        main(input_filename)
