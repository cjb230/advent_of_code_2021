#  https://adventofcode.com/2021/day/8#part2
SOURCE_FILE = 'day_8_input.txt'


def solve(line: dict[str]) -> int:
    inputs = line['input']
    outputs = line['output']
    segment_translator = {'ABCEFG': 0, 'CF': 1, 'ACDEG': 2, 'ACDFG': 3, 'BCDF': 4,
                          'ABDFG': 5, 'ABDEFG': 6, 'ACF': 7, 'ABCDEFG': 8, 'ABCDFG': 9}

    inputs_by_length = {2: [], 3: [], 4: [], 5: [], 6: [], 7: []}
    inputs_by_frequency = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0}
    for this_input in inputs:
        inputs_by_length[len(this_input)].append(this_input)
        for this_char in this_input:
            inputs_by_frequency[this_char] += 1

    unscrambler = {'a': None, 'b': None, 'c': None, 'd': None, 'e': None, 'f': None, 'g': None}
    scrambler = {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None, 'G': None}

    # the segment in the three-segment number but not the two-segment number is A
    three_seg = inputs_by_length[3].pop()
    two_seg = inputs_by_length[2].pop()
    top_segment = list(set(three_seg) - set(two_seg)).pop()
    unscrambler[top_segment] = 'A'
    scrambler['A'] = top_segment

    # three more segments can be identified directly by their frequency
    # and the segment that appears eight times and isn't A is C
    for input_char, frequency in inputs_by_frequency.items():
        if frequency == 4:
            unscrambler[input_char] = 'E'
            scrambler['E'] = input_char
        elif frequency == 6:
            unscrambler[input_char] = 'B'
            scrambler['B'] = input_char
        elif frequency == 9:
            unscrambler[input_char] = 'F'
            scrambler['F'] = input_char
        elif frequency == 8:
            if unscrambler[input_char] != 'A':
                unscrambler[input_char] = 'C'
                scrambler['C'] = input_char

    # of the two segments still unknown, the segment that appears in 4 is D
    four_segment = inputs_by_length[4].pop()
    for char in four_segment:
        if unscrambler[char] is None:
            unscrambler[char] = 'D'
            scrambler['D'] = char

    # the last unknown segment is G
    for input_char, unscrambled in unscrambler.items():
        if unscrambled is None:
            unscrambler[input_char] = 'G'
            scrambler['G'] = input_char

    result = 0
    for position, this_digit in enumerate(outputs):
        translation = ''
        for scrambled_segment in this_digit:
            translation += unscrambler[scrambled_segment]
        sorted_translation = "".join(sorted(translation))
        translation_digit = segment_translator[sorted_translation]
        result += pow(10, 3-position) * translation_digit
    return result


def main():
    # read the file
    with open(SOURCE_FILE) as f:
        displays = f.read().splitlines()
    signals = [display[:58].split() for display in displays]
    outputs = [display[61:].split() for display in displays]
    io = {i: {'input': io_data[0], 'output': io_data[1]} for i, io_data in enumerate(zip(signals, outputs))}

    result = 0
    for line in io.values():
        result += solve(line)

    print(result)


if __name__ == "__main__":
    main()
