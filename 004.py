# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# AAAAAAAABCCCC -> 8×A, B, 4×C


def code(text: str) -> str:
    res = ''
    count = 0
    for i in range(len(text)):
        if i == len(text)-1:
            res += f'{count}x{text[i]}, '
            return res[:-2]
        if text[i] == text[i+1]:
            count += 1
        else:
            count +=1 
            res += f'{count}x{text[i]}, '
            count = 0


# def decode(text: str) -> str:
#     foo = lambda x: [''.join(x[-1]) for i in range(int(x[0]))]
#     return ''.join(map(foo, text.split(', ')))



# with open('file.txt', 'r') as file:
#     text = file.readline()

# codding = code(text)
# # decodding = decode(codding)

# print(f'Origin text - {text}')
# print(f'Codding text - {codding}')
# # print(f'Decodding text - {decodding}')


x = '4xA'
res = ''

print(res)