#  https://adventofcode.com/2021/day/10
SOURCE_FILE = 'day_10_input.txt'

CHAR_PAIRS = {'{': '}', '(': ')', '<': '>', '[': ']'}
ERROR_SCORES = {')': 3, ']': 57, '}': 1197, '>': 25137}


def main():
    # read the file
    with open(SOURCE_FILE) as f:
        code_lines = f.read().splitlines()

    error_chars = []
    for x, code_line in enumerate(code_lines):
        stack = {}
        depth = 0
        for char in code_line:
            if char in CHAR_PAIRS:
                depth += 1
                stack[depth] = char
            elif char in CHAR_PAIRS.values():
                last_opened = stack[depth]
                if CHAR_PAIRS[last_opened] == char:
                    del stack[depth]
                    depth -= 1
                else:
                    error_chars.append(char)
                    break

    print(sum(ERROR_SCORES[char] for char in error_chars))


if __name__ == "__main__":
    main()
