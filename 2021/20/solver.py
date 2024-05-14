def apply_enhancement(input_image, enhancement_string):
    border_val = input_image[0][0]
    if input_image[0][0] == 0 and enhancement_string[0] == 1 or input_image[0][0] == 1 and enhancement_string[-1] == 0:
        border_val = (input_image[0][0] + 1) % 2

    output_image = [[border_val] * (len(input_image[0]) + 6) for _ in range(len(input_image) + 6)]
    for i in range(1, len(input_image) - 1):
        for j in range(1, len(input_image[0]) - 1):
            index = sum(
                input_image[i - 1 + ii][j - 1 + jj] * 2 ** (3 * (2 - ii) + (2 - jj))
                for ii in range(3)
                for jj in range(3)
            )
            output_image[i + 3][j + 3] = enhancement_string[index]

    return output_image


def main(filename):
    with open(filename) as input_file:
        enhancement_string = [0 if x == "." else 1 for x in input_file.readline().strip()]
        input_file.readline()
        input_image = [[0] * 3 + [0 if x == "." else 1 for x in line.strip()] + [0] * 3 for line in input_file]

    for _ in range(3):
        input_image.insert(0, [0] * len(input_image[0]))
        input_image.append([0] * len(input_image[0]))

    for _ in range(2):
        input_image = apply_enhancement(input_image, enhancement_string)

    result_part_1 = sum(sum(row) for row in input_image)
    print(f"part 1: {result_part_1}")

    for _ in range(48):
        input_image = apply_enhancement(input_image, enhancement_string)

    result_part_2 = sum(sum(row) for row in input_image)
    print(f"part 2: {result_part_2}")


if __name__ == "__main__":
    for input_filename in [
        "sample.txt",
        "input.txt"
    ]:
        print(f"-- {input_filename} --")
        main(input_filename)
