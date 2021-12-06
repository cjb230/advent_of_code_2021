SOURCE_FILE = 'day_6_input.txt'


def descendants_grid() -> dict[dict[int]]:
    results = {day: {age: None for age in range(9)} for day in range(257)}

    for age in range(9):
        results[256][age] = 1
    for day in range(255, -1, -1):
        results[day][0] = results[day + 1][6] + results[day + 1][8]
        for age in range(1, 9):
            if age > 0:
                results[day][age] = results[day+1][age-1]
    return results


def main():
    # read the file
    with open(SOURCE_FILE) as f:
        current_ages = [int(x) for x in f.readline().split(',')]

    grid = descendants_grid()
    result = sum([grid[0][age] for age in current_ages])
    print(result)


if __name__ == "__main__":
    main()
