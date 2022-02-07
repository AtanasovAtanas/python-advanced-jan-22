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


first_player, second_player = read_players()

print_board_numeration()

print(f'{first_player.name} starts first!')