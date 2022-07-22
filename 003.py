# Создайте программу для игры в ""Крестики-нолики""


from audioop import cross
from functions import draw_status
from random import randint
import time


sizeX = 3
sizeY = 3


def bot_choise(data: list) -> tuple:
    while True:
        x = randint(0, 2)
        y = randint(0, 2)
        if data[x][y] == '.':
            return x, y


def player_choise(data: list) -> list:
    x = input('Your position -> ')
    return x.split()


def main():
    data = []
    for i in range(sizeX):
        data.append(['.' for i in range(sizeY)])

    draw_status(data)

    cross = player_choise(data)
    data[int(cross[1])-1][int(cross[0])-1] = 'X'

    for i in range(5):
        draw_status(data)
        nulls = bot_choise(data)
        data[nulls[0]][nulls[1]] = '0'
        cross = player_choise(data)
        draw_status(data)
        data[int(cross[0])][int(cross[1])] = 'X'


if __name__ == '__main__':
    main()