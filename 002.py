# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. 
# Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

from functions import get_number
from random import randint as rd


data = {
    'all_candies': 100,
    'min': 1,
    'max': 28,
    'who': 'Player',
    'winner': '',
    'input_text': 'Input count of candies -> ',
    'error_text': 'Wrong input. Please input the number between 1 and 28 -> '
}


def bot_choose(count, min=1, max=28) -> int:
    if count - max == 0:
        return max
    choice = (count % max) - 1
    if choice < min: 
        choice = rd(min, max+1)
    return choice


def get_status(candies, count, who) -> str:
    return f'{who} takes - {count}. On the table {candies} candies'


def main(data: dict):
    print(f'On the table {data["all_candies"]} candies')
    while data['all_candies'] > 0:
        if data['who'] == 'Player':
            print()
            choose = get_number(data['input_text'], data['error_text'], data['min'], data['max'])
        else:
            choose = bot_choose(data['all_candies'], data['min'], data['max'])
        data['all_candies'] -= choose
        if data['all_candies'] == 0: data['winner'] = data['who']
        if data['all_candies'] < data['max']: data['max'] = data['all_candies'] 
        print(get_status(data['all_candies'], choose, data['who']))
        if data['who'] == 'Player': data['who'] = 'Bot'
        else: data['who'] = 'Player'
    print(f'The winner is {data["winner"]}')


if __name__ == '__main__':
    main(data)