class Player:
    def __init__(self, name, sign):
        self.name = name
        self.sign = sign


def read_players():
    first_player_name = input(f'Player one name: ')
    second_player_name = input(f'Player two name: ')

    while True:
        first_player_sign = input(f'{first_player_name} would you like to play with "X" or "O"? ').upper()
        if first_player_sign == 'X' or first_player_sign == 'O':
            break

    second_player_sign = 'O' if first_player_sign == 'X' else 'X'

    return Player(first_player_name, first_player_sign), Player(second_player_name, second_player_sign)


def print_board_numeration():
    print('This is the numeration of the board:')
    print('|  1  |  2  |  3  |')
    print('|  4  |  5  |  6  |')
    print('|  7  |  8  |  9  |')


def init_board():
    size = 3
    result = []
    for _ in range(size):
        result.append([None] * size)
    return result


def is_valid_position(board, board_mapper, position):
    if position < 1 or position > 9:
        return False
    row, col = board_mapper[position]
    return board[row][col] is None


def print_board(board):
    for row in board:
        print('|  ', end='')
        print('  |  '.join([x if x is not None else ' ' for x in row]), end='')
        print('  |')


first_player, second_player = read_players()

print_board_numeration()

print(f'{first_player.name} starts first!')

board = init_board()
board_mapper = {
    1: [0, 0],
    2: [0, 1],
    3: [0, 2],
    4: [1, 0],
    5: [1, 1],
    6: [1, 2],
    7: [2, 0],
    8: [2, 1],
    9: [2, 2],
}

turn = 1

while True:
    current_player = first_player if turn % 2 != 0 else second_player
    position = int(input(f'{current_player.name} choose a free position [1-9]: '))

    if not is_valid_position(board, board_mapper, position):
        continue

    row, col = board_mapper[position]
    board[row][col] = current_player.sign

    print_board(board)

    turn += 1
