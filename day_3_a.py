SOURCE_FILE = 'day_3_input.txt'


def main():
    with open(SOURCE_FILE) as f:
        diagnostic_report_numbers = [line for line in f.readlines()]
    half_report_length = len(diagnostic_report_numbers) / 2
    position_ones = {i: 0 for i in range(12)}
    gamma = 0
    for this_line in diagnostic_report_numbers:
        for i in range(12):
            if this_line[i] == '1':
                position_ones[i] += 1
    for i in range(12):
        if position_ones[i] > half_report_length:
            gamma += pow(2, 11-i)
    epsilon = pow(2, 12) - 1 - gamma
    print(gamma * epsilon)


if __name__ == "__main__":
    main()
