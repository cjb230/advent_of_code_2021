"""
The obvious memory improvement for this one is to only write non-zero numbers of vents, and avoid creating a million-
element dict of dicts. But it's fast enough anyway!
"""

SOURCE_FILE = 'day_5_input.txt'


def pos_string_to_nums(position_string: str) -> dict:
    number_strings = position_string.split(',')
    x_pos = int(number_strings[0])
    y_pos = int(number_strings[1])
    return {'x': x_pos, 'y': y_pos}


def points_from_line(line_def: list[dict]) -> list:
    points = []
    if line_def[0]['x'] == line_def[1]['x']:  # vertical
        ord_min = min(line_def[0]['y'], line_def[1]['y'])
        ord_max = max(line_def[0]['y'], line_def[1]['y'])
        points = [{'x': line_def[0]['x'], 'y': i} for i in range(ord_min, ord_max+1)]
    elif line_def[0]['y'] == line_def[1]['y']:  # horizontal
        ord_min = min(line_def[0]['x'], line_def[1]['x'])
        ord_max = max(line_def[0]['x'], line_def[1]['x'])
        points = [{'x': i, 'y': line_def[0]['y']} for i in range(ord_min, ord_max+1)]
    else:  # diagonal
        if line_def[0]['x'] < line_def[1]['x']:
            leftmost = line_def[0]
            rightmost = line_def[1]
        else:
            leftmost = line_def[1]
            rightmost = line_def[0]
        if leftmost['y'] < rightmost['y']:
            vertical_lr_step = 1
        else:
            vertical_lr_step = -1
        for steps, x in enumerate(range(leftmost['x'], rightmost['x']+1)):
            points.append({'x': x, 'y': leftmost['y']+(steps * vertical_lr_step)})
    return points


def main():
    lines = []
    vent_map = {x: {y: 0 for y in range(1000)} for x in range(1000)}

    # read the file
    with open(SOURCE_FILE) as f:
        line_strings = f.read().splitlines()

    # parse the file to a list of non-diagonal lines
    for line_string in line_strings:
        chunks = line_string.split(' ')
        pos_1 = pos_string_to_nums(chunks[0])
        pos_2 = pos_string_to_nums(chunks[2])
        lines.append([pos_1, pos_2])

    # for each line, mark the vent locations on the vent map
    for line in lines:
        for point in points_from_line(line):
            vent_map[point['x']][point['y']] += 1

    total_intersections = 0
    for x in vent_map:
        for y, val in vent_map[x].items():
            if val > 1:
                total_intersections += 1
    print(total_intersections)


if __name__ == "__main__":
    main()
