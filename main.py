from random import randint

fieldSize = 0


def printField(field):
    for i in range(fieldSize):
        for j in range(fieldSize):
            print(field[i][j], end=' ')
        print()
    print("==========")


def down(field):
    for i in range(fieldSize - 1, -1, -1):
        for j in range(fieldSize):
            if field[i][j] != 0:
                i1 = i
                while i1 < fieldSize - 1 and field[i1 + 1][j] == 0:
                    field[i1 + 1][j] = field[i1][j]
                    field[i1][j] = 0
                    i1 += 1
                if i1 < fieldSize - 1 and field[i1][j] == field[i1 + 1][j]:
                    field[i1 + 1][j] += field[i1][j]
                    if field[i1 + 1][j] == 2048:
                        print("Поздравляем!Вы прошли игру!")
                        exit(0)
                    field[i1][j] = 0


def rotateRight(field):
    field1 = [[0 for i in range(fieldSize)] for i in range(fieldSize)]
    for i in range(fieldSize):
        for j in range(fieldSize):
            field1[j][fieldSize - i - 1] = field[i][j]  #
    field.clear()
    field = [[0 for i in range(fieldSize)] for i in range(fieldSize)]
    for i in range(fieldSize):
        for j in range(fieldSize):
            field[i][j] = field1[i][j]
    return field1


def gen(field):
    while 1:
        x, y = randint(0, fieldSize - 1), randint(0, fieldSize - 1)
        if (field[x][y] == 0):
            field[x][y] = 2
            return


print("Управление:\n\tВниз - d\n\tВверх - u\n\tВправо - r\n\tВлево - l")
print("Пожалуйста введите размерность поля")
fieldSize = int(input())
field = [[0 for i in range(fieldSize)] for i in range(fieldSize)]
while True:
    gen(field)
    printField(field)
    c = input()
    if c == 'd':
        down(field)
    elif c == 'l':
        for i in range(3):
            field = rotateRight(field)
        down(field)
        field = rotateRight(field)
    elif c == 'r':
        field = rotateRight(field)
        down(field)
        for i in range(3):
            field = rotateRight(field)
    elif c == 'u':
        for i in range(2):
            field = rotateRight(field)
        down(field)
        for i in range(2):
            field = rotateRight(field)
