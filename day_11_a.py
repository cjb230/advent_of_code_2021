#  https://adventofcode.com/2021/day/11
SOURCE_FILE = 'day_11_input.txt'


def display(state: dict) -> None:
    for row in range(1, 11):
        line = ""
        for col in range(1, 11):
            line += str(state[row][col]).ljust(3)
        print(line)


def process_flashes(start_state: dict, flashes: set) -> dict:
    for this_flash in flashes:
        row, col = this_flash[0], this_flash[1]
        for row_offset in [-1, 0, 1]:
            for col_offset in [-1, 0, 1]:
                if not (row_offset == 0 and col_offset == 0):
                    try:
                        start_state[row+row_offset][col+col_offset] += 1
                    except KeyError:
                        pass
    return start_state


def step(initial_state: dict, step_number: int) -> dict:
    new_state = {row: {col: (val+1) for col, val in vals.items()} for row, vals in initial_state.items()}
    flashed = set()
    flashes = 0
    while True:
        flashes_to_process = set()
        for row in range(1, 11):
            for col in range(1, 11):
                if new_state[row][col] > 9:
                    if (row, col) not in flashed:
                        flashes_to_process.add((row, col))
        if flashes_to_process:
            new_state = process_flashes(new_state, flashes_to_process)
            flashes += len(flashes_to_process)
            flashed = flashed.union(flashes_to_process)
        else:
            break
    for this_octopus in flashed:
        new_state[this_octopus[0]][this_octopus[1]] = 0
    return {'flashes': flashes, 'end_state': new_state}


def main():
    # read the file
    with open(SOURCE_FILE) as f:
        energy_levels_start = {row: {col: int(char) for col, char in enumerate(content, start=1)} for row, content in enumerate(f.read().splitlines(), start=1)}

    states = {0: energy_levels_start}
    flashes = 0
    for i in range(1, 101):
        step_result = step(states[i-1], i)
        flashes += step_result['flashes']
        states[i] = step_result['end_state']

    print(flashes)


if __name__ == "__main__":
    main()
