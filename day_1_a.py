SOURCE_FILE = 'day_1_input.txt'


def main():
    with open(SOURCE_FILE) as f:
        depths = {key: (int(this_string)) for key, this_string in enumerate(f.readlines())}
    result = 0
    for i in range(1, 2000):
        if depths[i] > depths[i-1]:
            result += 1
    print(result)


if __name__ == "__main__":
    main()
