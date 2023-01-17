def intro():
    print('-------------------')
    print('  Добро пожаловать ')
    print('      в игру       ')
    print(' "крестики-нолики" ')
    print('-------------------')
    print(' формат ввода: x y ')
    print(' x - номер строки  ')
    print(' y - номер столбца ')


def show():    # выводим поле на экран
    print()
    print('    | 0 | 1 | 2 | ')
    print('  --------------- ')
    for i, row in enumerate(field):
        row_str = f'  {i} | {" | ".join(row)} | '
        print(row_str)
        print('  --------------- ')
    print()


def ask():    # ввод координат и проверка введенных данных
    while True:
        cords = input('         Ваш ход: ').split()

        if len(cords) != 2:
            print(' Введите 2 координаты! ')
            continue

        x, y = cords

        if not (x.isdigit()) or not (y.isdigit()):
            print(' Введите числа! ')
            continue

        x, y = int(x), int(y)

        if 0 > x or x > 2 or 0 > y or y > 2:
            print(' Координаты вне диапазона! ')
            continue

        if field[x][y] != ' ':
            print(' Клетка занята! ')
            continue

        return x, y


def check_win():    # проверка на выигрышную комбинацию
    for i in range(3):  # проверка строк
        symbols = []
        for j in range(3):
            symbols.append(field[i][j])
        if symbols == ['X', 'X', 'X']:
            print('Выиграл крестик!')
            return True
        if symbols == ['0', '0', '0']:
            print('Выиграл нолик!')
            return True

    for i in range(3):   # проверка столбцов
        symbols = []
        for j in range(3):
            symbols.append(field[j][i])
        if symbols == ['X', 'X', 'X']:
            print('Выиграл крестик!')
            return True
        if symbols == ['0', '0', '0']:
            print('Выиграл нолик!')
            return True

    symbols = []   # проверка диагоналей
    for i in range(3):
        symbols.append(field[i][i])
    if symbols == ['X', 'X', 'X']:
        print('Выиграл крестик!')
        return True
    if symbols == ['0', '0', '0']:
        print('Выиграл нолик!')
        return True

    symbols = []
    for i in range(3):
        symbols.append(field[i][2-i])
    if symbols == ['X', 'X', 'X']:
        print('Выиграл крестик!')
        return True
    if symbols == ['0', '0', '0']:
        print('Выиграл нолик!')
        return True

    return False


intro()
field = [[' '] * 3 for i in range(3)]  # игровое поле
num = 0
while True:
    num += 1

    show()

    if num % 2 == 1:     # порядок игры
        print(' Ходит крестик!')
    else:
        print(' Ходит нолик!')

    x, y = ask()

    if num % 2 == 1:
        field[x][y] = 'X'
    else:
        field[x][y] = '0'

    if check_win():
        break

    if num == 9:
        print(' Ничья!')
        break
