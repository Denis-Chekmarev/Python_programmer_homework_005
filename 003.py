# Создайте программу для игры в ""Крестики-нолики""


from random import choice
from os import system 
import time
from turtle import position


data = {
    'sizex': 3,
    'sizey': 3,
    'player_symbol': 'X',
    'bot_symbol': '0',
    'field': [], 
    'game': 'play'
}


def init_field(data: dict) -> dict:
    for i in range(data['sizex']):
        data['field'].append(['.' for i in range(data['sizey'])])
    return data


def draw_status(data: dict):
    system('cls')
    print('\n')
    for i in range(len(data['field'])):
        print('\t', end='')
        for j in range(len(data['field'][0])):
            print(data['field'][i][j], end='\t')
        print('\n\n')


def bot_choise(data: dict) -> tuple:
    positions = get_free_positions(data)
    if positions == None:
        return data
    zero = choice(positions)
    data['field'][zero[0]][zero[1]] = data['bot_symbol']
    draw_status(data)
    time.sleep(0.5)
    return data


def player_choise(data: dict) -> list:
    x = input('Your position -> ')
    zero = tuple(map(int, x.split()))
    data['field'][zero[1]-1][zero[0]-1] = data['player_symbol']
    draw_status(data)
    time.sleep(0.5)
    return data


def get_free_positions(data: dict) -> tuple:
    result = []
    for i in range(data['sizex']):
        for j in range(data['sizey']):
            if data['field'][i][j] == '.':
                result.append((i, j))
    return result
    

def main(data: dict) -> None:
    data = init_field(data)

    # side = input('Would you want to play zeroes(yes, no): ')
    # if side.lower() == 'yes':
    #     data['player_symbol'] = '0'
    #     data['bot_symbol'] = 'X'

    while data['game'] == 'play':
        if get_free_positions(data) == None:
            data['win'] == 'nobody'
        draw_status(data)
        data = player_choise(data)
        data = bot_choise(data)

    print(data['win'])

if __name__ == '__main__':
    main(data)