SOURCE_FILE = 'day_7_input.txt'


def sum_distance(point: int, position_list: list[int]) -> int:
    total_distance = 0
    for this_position in position_list:
        dist = abs(point - this_position)
        total_distance += (dist * (dist + 1)) / 2
    return total_distance


def main():
    # read the file
    with open(SOURCE_FILE) as f:
        positions = [int(x) for x in f.readline().split(',')]

    result = min([sum_distance(i, positions) for i in range(2000)])
    print(result)


if __name__ == "__main__":
    main()
