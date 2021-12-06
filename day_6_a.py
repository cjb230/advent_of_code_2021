SOURCE_FILE = 'day_6_input.txt'


def next_day(current_fish_ages: list[int]) -> list[int]:
    result = []
    for fish_age in current_fish_ages:
        if fish_age > 0:
            result.append(fish_age-1)
        else:
            result.append(6)
            result.append(8)
    return result


def main():
    # read the file
    with open(SOURCE_FILE) as f:
        current_ages = [int(x) for x in f.readline().split(',')]
    for i in range(1, 81):
        new_ages = next_day(current_ages)
        current_ages = new_ages
    print(len(current_ages))


if __name__ == "__main__":
    main()
