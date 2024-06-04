print('Добро пожаловать в игру "Крестики Нолики"!')
print('Обратите внимание!!! \nНумерация строк и столбцов начинается с 0 до 2!')

tablo = [
    ['-', '-', '-'],
    ['-', '-', '-'],
    ['-', '-', '-']
]

def tablo_print(tablo):
    for row in tablo:
        for cell in row:
            print(cell, end=' ')
        print()

def check_win(tablo, user):

    if tablo[0][0] == user and tablo[1][1] == user and tablo[2][2] == user:
        return True
    if tablo[0][2] == user and tablo[1][1] == user and tablo[2][0] == user:
        return True

    for row in tablo:
        if row.count(user) == 3:
            return True

    for i in range(3):
        if tablo[0][i] == user and tablo[1][i] == user and tablo[2][i] == user:
            return True

user_ = 'X'

while True:
    tablo_print(tablo)
    print('Ход игрока', user_)

    try:
        row = int(input('Введите номер строки: '))
    except ValueError as e:
        print('Вы ввели некорректный номер строки. Попробуйте еще раз!')
        row = int(input('Введите номер строки: '))

    try:
        col = int(input('Введите номер столбца: '))
    except ValueError as e:
        print('Вы ввели некорректный номер столбца. Попробуйте еще раз!')
        col = int(input('Введите номер столбца: '))


    while row > 2:
        print('Вы ввели некорректный номер строки. Попробуйте еще раз!')
        row = int(input('Введите номер строки: '))

    while row < 0:
        print('Вы ввели некорректный номер строки. Попробуйте еще раз!')
        row = int(input('Введите номер строки: '))

    while col > 2:
        print('Вы ввели некорректный номер столбца. Попробуйте еще раз!')
        col = int(input('Введите номер столбца: '))

    while col < 0:
        print('Вы ввели некорректный номер столбца. Попробуйте еще раз!')
        col = int(input('Введите номер столбца: '))

    if tablo[row][col] != '-':
        print('Место занято. Выберите другое место!')
        continue

    tablo[row][col] = user_

    if check_win(tablo,user_):
        tablo_print(tablo)
        print('Победил Игрок', user_)
        break

    if all([cell != '-' for row in tablo for cell in row]):
        print('Ничья')
        tablo_print(tablo)
        break

    user_ = '0' if user_ == 'X' else 'X'
