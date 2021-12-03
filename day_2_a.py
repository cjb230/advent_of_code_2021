SOURCE_FILE = 'day_2_input.txt'


def main():
    with open(SOURCE_FILE) as f:
        course = [line for line in f.readlines()]
    total_distances = {'forward': 0, 'up': 0, 'down': 0}
    for num, step in enumerate(course):
        chunks = step.split()
        total_distances[chunks[0]] += int(chunks[1])
    depth = total_distances['down'] - total_distances['up']
    print(depth * total_distances['forward'])


if __name__ == "__main__":
    main()
