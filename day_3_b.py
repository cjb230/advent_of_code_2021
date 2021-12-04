import copy

SOURCE_FILE = 'day_3_input.txt'


def convert(binary_dict: dict) -> int:
    length = len(binary_dict)
    total = 0
    for i in range(length):
        total += binary_dict[i] * pow(2, (length - 1 - i))
    return total


def main():
    with open(SOURCE_FILE) as f:
        oxygen_base = {i: {j: int(digit) for j, digit in enumerate(line.strip())} for i, line in enumerate(f.readlines())}
    co2_base = copy.deepcopy(oxygen_base)
    oxygen_base_done = False
    co2_base_done = False
    for i in range(12):
        if not oxygen_base_done:
            readings = len(oxygen_base)
            position_total = 0
            for key, line in oxygen_base.items():
                position_total += line[i]
            most_common_bit = 1 if position_total >= (readings / 2) else 0
            keys_to_remove = []
            for key, line in oxygen_base.items():
                if line[i] == (1 - most_common_bit):
                    keys_to_remove.append(key)
            for key in keys_to_remove:
                del oxygen_base[key]
            if len(oxygen_base) == 1:
                oxygen_base_done = True
                oxygen_rating = convert(list(oxygen_base.values())[0])

        if not co2_base_done:
            readings = len(co2_base)
            position_total = 0
            for key, line in co2_base.items():
                position_total += line[i]
            most_common_bit = 1 if position_total >= (readings / 2) else 0
            keys_to_remove = []
            for key, line in co2_base.items():
                if line[i] == most_common_bit:
                    keys_to_remove.append(key)
            for key in keys_to_remove:
                del co2_base[key]
            if len(co2_base) == 1:
                co2_base_done = True
                co2_rating = convert(list(co2_base.values())[0])

    if co2_base_done and oxygen_base_done:
        print(oxygen_rating * co2_rating)
        exit(0)


if __name__ == "__main__":
    main()
