#  https://adventofcode.com/2021/day/25

SOURCE_FILE = 'day_25_input.txt'


def step(start_grid: dict) -> int:
    y_size = len(start_grid)
    x_size = len(start_grid[1])
    move_east = set()
    for y_pos, line in start_grid.items():
        for x_pos, char in line.items():
            if char == '>' and ((x_pos < x_size and start_grid[y_pos][x_pos+1] == '.') or (x_pos == x_size and start_grid[y_pos][1] == '.')):
                move_east.add((x_pos, y_pos))
    for sc in move_east:
        if sc[0] == x_size:
            start_grid[sc[1]][1] = '>'
        else:
            start_grid[sc[1]][sc[0] + 1] = '>'
        start_grid[sc[1]][sc[0]] = '.'

    move_south = set()
    for y_pos, line in start_grid.items():
        for x_pos, char in line.items():
            if char == 'v' and ((y_pos < y_size and start_grid[y_pos+1][x_pos] == '.') or (y_pos == y_size and start_grid[1][x_pos] == '.')):
                move_south.add((x_pos, y_pos))
    for sc in move_south:
        if sc[1] == y_size:
            start_grid[1][sc[0]] = 'v'
        else:
            start_grid[sc[1]+1][sc[0]] = 'v'
        start_grid[sc[1]][sc[0]] = '.'

    return len(move_south) + len(move_east)


def main():
    with open(SOURCE_FILE) as f:
        lines = f.read().splitlines()
    grid = {x: {y: char for y, char in enumerate(line, start=1)} for x, line in enumerate(lines, start=1)}

    i = 0
    while True:
        i += 1
        moves = step(grid)
        if moves == 0:
            print(i)
            break


if __name__ == "__main__":
    main()
