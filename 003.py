# Создайте программу для игры в ""Крестики-нолики""


from os import system


field = [' ' for x in range(1, 10)]


def draw_field(field: list) -> None:
    system('cls')
    print('-------------')
    for i in range(3):
        print(f'| {field[0+i*3]} | {field[1+i*3]} | {field[2+i*3]} |')
        print('-------------')


def player_choise(symbol: str, board: list) -> int:
    valid = False
    while not valid:
        player_input = input(f'Chose the place for {symbol} -> ')
        try:
            player_input = int(player_input)
        except ValueError:
            print('Wrong input. Please input the number from 1 to 9 --> ')
            continue
        if 1 <= player_input <= 9:
            if str(board[player_input-1]) == ' ':
                valid = True
            else:
                print('This element is not empty. Try again --> ')
        else: 
            print('Wrong input. Input the number from 1 to 9 --> ')
    return player_input
    

def is_win(board):
    win_coords = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for elem in win_coords:
        if board[elem[0]] == board[elem[1]] == board[elem[2]]:
            return board[elem[0]]
    return False


def main(field):
    counter = 0
    win = False
    symbol = 'X'
    while not win:
        draw_field(field)
        if counter % 2:
            field[player_choise(symbol, field) - 1] = symbol
            symbol = 'X'
        else:
            field[player_choise(symbol, field) - 1] = symbol
            symbol = '0'
        counter += 1
        if counter > 4:
            temp = is_win(field)
            if temp:
                print(f'{temp} is win')
                win = True
                break
        if counter == 9:
            print('Nobody win')
            break


main(field)