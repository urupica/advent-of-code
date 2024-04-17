import operator
from functools import reduce


def count_version_numbers(packet, start=0):
    version = int(packet[start:start + 3], 2)
    type_id = int(packet[start + 3:start + 6], 2)
    current = start + 6
    if type_id == 4:
        # literal value
        total_length = 6
        while True:
            first_bit = packet[current]
            current += 5
            total_length += 5
            if first_bit == "0":
                break
        return version, start + total_length
    else:
        # operator
        length_type_id = packet[current]
        current += 1
        if length_type_id == "0":
            total_length = int(packet[current:current + 15], 2)
            current += 15
            new_start_max = current + total_length
            all_subpacket_versions_count = 0
            while current < new_start_max:
                subpacket_version_count, new_start = count_version_numbers(packet, current)
                all_subpacket_versions_count += subpacket_version_count
                current = new_start
            return version + all_subpacket_versions_count, current
        else:
            number_of_sub_packets = int(packet[current:current + 11], 2)
            current += 11
            all_subpacket_versions_count = 0
            for _ in range(number_of_sub_packets):
                subpacket_version_count, new_start = count_version_numbers(packet, current)
                all_subpacket_versions_count += subpacket_version_count
                current = new_start
            return version + all_subpacket_versions_count, current


def compute_value(packet, start=0):
    type_id = int(packet[start + 3:start + 6], 2)
    current = start + 6
    if type_id == 4:
        # literal value
        total_length = 6
        literal_value_bin = ""
        while True:
            first_bit = packet[current]
            literal_value_bin += packet[current + 1:current + 5]
            current += 5
            total_length += 5
            if first_bit == "0":
                break
        literal_value = int(literal_value_bin, 2)
        return literal_value, start + total_length
    else:
        # operator
        length_type_id = packet[current]
        current += 1
        all_subpacket_values = []
        if length_type_id == "0":
            total_length = int(packet[current:current + 15], 2)
            current += 15
            new_start_max = current + total_length
            while current < new_start_max:
                subpacket_value, new_start = compute_value(packet, current)
                all_subpacket_values.append(subpacket_value)
                current = new_start
        else:
            number_of_sub_packets = int(packet[current:current + 11], 2)
            current += 11
            for _ in range(number_of_sub_packets):
                subpacket_value, new_start = compute_value(packet, current)
                all_subpacket_values.append(subpacket_value)
                current = new_start
        if type_id == 0:
            return sum(all_subpacket_values), current
        elif type_id == 1:
            return reduce(operator.mul, all_subpacket_values), current
        elif type_id == 2:
            return min(all_subpacket_values), current
        elif type_id == 3:
            return max(all_subpacket_values), current
        elif type_id == 5:
            return int(all_subpacket_values[0] > all_subpacket_values[1]), current
        elif type_id == 6:
            return int(all_subpacket_values[0] < all_subpacket_values[1]), current
        else:
            return int(all_subpacket_values[0] == all_subpacket_values[1]), current


def main(filename):
    with open(filename) as input_file:
        packet = input_file.readline().strip()
    packet_bin = format(int(packet, 16), "b")
    if len(packet_bin) % 4 != 0:
        packet_bin = "0" * ((len(packet_bin) // 4 + 1) * 4 - len(packet_bin)) + packet_bin
    assert len(packet_bin) % 4 == 0

    result_part_1, _ = count_version_numbers(packet_bin)
    print(f"part 1: {result_part_1}")

    result_part_2, _ = compute_value(packet_bin)
    print(f"part 2: {result_part_2}")


if __name__ == "__main__":
    for input_filename in [
        "sample.txt",
        "input.txt"
    ]:
        print(f"-- {input_filename} --")
        main(input_filename)
