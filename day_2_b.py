SOURCE_FILE = 'day_2_input.txt'


def main():
    with open(SOURCE_FILE) as f:
        course = [line for line in f.readlines()]
    h_pos = 0
    aim = 0
    depth = 0
    for num, step in enumerate(course):
        chunks = step.split()
        instruction = chunks[0]
        units = int(chunks[1])
        if instruction == 'forward':
            h_pos += units
            depth += units * aim
        elif instruction == 'up':
            aim -= units
        elif instruction == 'down':
            aim += units
        else:
            exit('WTF')

    print(h_pos * depth)


if __name__ == "__main__":
    main()
