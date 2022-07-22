# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. 
# Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота

from functions import get_number
from random import randint as rd


def player_choose(min=1, max=28) -> int:
    count = 0
    while min <= count <= max:
        count = get_number('Input count of candies -> ', 'Wrong input. Please input the number between 1 and 28 -> ')
    return count


def bot_choose(min=1, max=28) -> int:
    return rd(min, max+1)


def get_status(candies) -> str:
    return f'On the table {candies} candies'


def main():
    
    all_candies = 2021
    max_round = 28
    bot_choose = 28
    player_choose = 28

    while all_candies != 0:
        all_candies -= bot_choose()
        print(get_status(all_candies))
        all_candies -= player_choose()

    # print('The winner is -> ', winner)


if __name__ == '__main__':
    main()