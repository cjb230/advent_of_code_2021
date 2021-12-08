#  https://adventofcode.com/2021/day/8
SOURCE_FILE = 'day_8_input.txt'


def main():
    # read the file
    with open(SOURCE_FILE) as f:
        displays = f.read().splitlines()
    outputs = [display[61:].split() for display in displays]
    output_lengths = [[len(char) for char in output] for output in outputs]
    result = sum([sum([1 for length in length_set if length in (2, 4, 3, 7)]) for length_set in output_lengths])

    print(result)


if __name__ == "__main__":
    main()
