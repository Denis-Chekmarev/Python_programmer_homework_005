from os import system


def get_number(text: str, error_text = 'Wrong input. Try again -> ') -> int:
    print(text, end='')
    while True:
        numb = input()
        if numb.isdigit():
            numb = float(numb)
            return numb
        else:
            print(error_text, end='')


def draw_status(data: list):
    system('cls')
    print('\t1\t2\t3')
    for i in range(len(data)):
        print(f'{i+1}\t', end='')
        for j in range(len(data[0])):
            print(data[i][j], end='\t')
        print('\n\n')


def read_file(filename: str) -> str:
    res = ''
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            res += line
    return res


def write_file(filename: str, text: str) -> None:
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(text)
