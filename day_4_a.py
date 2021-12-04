SOURCE_FILE = 'day_4_input.txt'


def main():
    call_position = {}
    call_order = {}
    with open(SOURCE_FILE) as f:
        call_string = f.readline()
        remainder = f.readlines()
    for position, string in enumerate(call_string.split(',')):
        call_position[int(string)] = position + 1
        call_order[position + 1] = int(string)
    board_number = 0
    boards = {i: {'layout': {j: None for j in range(1, 26)},
                  'call_order': {j: None for j in range(1, 26)},
                  'completion_turn': {'rows': {j: None for j in range(1, 6)},
                                      'columns': {j: None for j in range(1, 6)}},
                  'quickest_row': None,
                  'quickest_row_turns': None,
                  'quickest_col': None,
                  'quickest_col_turns': None,
                  'completion': None
                  } for i in range(1, 101)}

    for this_line in remainder:
        if this_line == '\n':
            board_number += 1
            board_position = 1
        else:
            numbers = this_line.split()
            for number in numbers:
                boards[board_number]['layout'][board_position] = int(number)
                board_position += 1

    fastest_board = None
    fastest_board_completion = 101
    for board_key, board_dict in boards.items():
        for i in range(1, 26):
            board_dict['call_order'][i] = call_position[board_dict['layout'][i]]
        for i in range(1, 6):
            board_dict['completion_turn']['rows'][i] = max(board_dict['call_order'][1 + (5 * (i - 1))], board_dict['call_order'][2 + (5 * (i - 1))], board_dict['call_order'][3 + (5 * (i - 1))], board_dict['call_order'][4 + (5 * (i - 1))], board_dict['call_order'][5 + (5 * (i - 1))])
            if i == 1 or board_dict['completion_turn']['rows'][i] < board_dict['quickest_row_turns']:
                board_dict['quickest_row_turns'] = board_dict['completion_turn']['rows'][i]
                board_dict['quickest_row'] = i
            board_dict['completion_turn']['columns'][i] = max(board_dict['call_order'][i], board_dict['call_order'][i + 5], board_dict['call_order'][i + 10], board_dict['call_order'][i + 15], board_dict['call_order'][i + 20])
            if i == 1 or board_dict['completion_turn']['columns'][i] < board_dict['quickest_col_turns']:
                board_dict['quickest_col_turns'] = board_dict['completion_turn']['columns'][i]
                board_dict['quickest_col'] = i
        board_dict['completion'] = min(board_dict['quickest_row_turns'], board_dict['quickest_col_turns'])
        if board_dict['completion'] < fastest_board_completion:
            fastest_board_completion = board_dict['completion']
            fastest_board = board_key

    numbers_called = [number for position, number in call_order.items() if position <= fastest_board_completion]
    last_number_called = call_order[fastest_board_completion]
    winning_board_numbers = list(boards[fastest_board]['layout'].values())
    unmarked_numbers = list(set(winning_board_numbers) - set(numbers_called))
    score = last_number_called * sum(unmarked_numbers)
    print(score)


if __name__ == "__main__":
    main()
