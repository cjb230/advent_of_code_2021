#  https://adventofcode.com/2021/day/10
import statistics

SOURCE_FILE = 'day_10_input.txt'

CHAR_PAIRS = {'{': '}', '(': ')', '<': '>', '[': ']'}
ERROR_SCORES = {'(': 1, '[': 2, '{': 3, '<': 4}


def completion_score(open_stack: dict) -> int:
    stack_size = len(open_stack)
    score = 0
    for i in range(stack_size, 0, -1):
        score *= 5
        score += ERROR_SCORES[open_stack[i]]
    return score


def main():
    # read the file
    with open(SOURCE_FILE) as f:
        code_lines = f.read().splitlines()

    autocomplete_scores = []
    for x, code_line in enumerate(code_lines):
        stack = {}
        depth = 0
        line_corrupt = False
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
                    line_corrupt = True
                    break
        if not line_corrupt:
            autocomplete_scores.append(completion_score(stack))

    print(statistics.median(autocomplete_scores))


if __name__ == "__main__":
    main()
