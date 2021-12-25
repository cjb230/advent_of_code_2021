#  https://adventofcode.com/2021/day/13

SOURCE_FILE = 'day_13_input.txt'


def fold(original_dot_set, fold_axis, fold_line):
    new_dot_set = set()
    for this_dot in original_dot_set:
        if (fold_axis == 'x' and fold_line < this_dot[0]) or (fold_axis == 'y' and fold_line < this_dot[1]):
            if fold_axis == 'x':
                new_dot = ((2*fold_line)-this_dot[0], this_dot[1])
            else:
                new_dot = (this_dot[0], (2*fold_line)-this_dot[1])
            new_dot_set.add(new_dot)
        else:
            new_dot_set.add(this_dot)
    return new_dot_set


def main():
    dots = set()
    folds = []
    folds_completed = 0
    target_dots = True
    with open(SOURCE_FILE) as f:
        lines = f.read().splitlines()

    for line in lines:
        if line == '':
            target_dots = False
            continue
        if target_dots:
            ordinates = line.split(',')
            dot = tuple(int(ord) for ord in ordinates)
            dots.add(dot)
        else:
            chunks = line[11:].split('=')
            fold_direction = chunks[0]
            fold_ordinate = int(chunks[1])
            folds.append((fold_direction, fold_ordinate))

    for this_fold in folds:
        print('folds completed = ', folds_completed , '  total dots = ', len(dots))
        dots = fold(dots, this_fold[0], this_fold[1])
        folds_completed += 1
        print('folds completed = ', folds_completed , '  total dots = ', len(dots))
        break


if __name__ == "__main__":
    main()
