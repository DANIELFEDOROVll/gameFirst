import os
import random

score = 0
var = True
kor_player = [2, 2]

Player = '&'

rows = 10
columns = 30


def draw(row, col, player_kordinate, eat_kor):
    for i in range(row):
        for j in range(col):

            if eat_kor[0] == i and eat_kor[1] == j:
                print('*', end='')

            elif player_kordinate[0] == i and player_kordinate[1] == j:
                print(Player, end='')

            elif i == 0 or i == row - 1:
                print('#', end='')

            else:
                if j == 0 or j == col - 1:
                    print('#', end='')
                else:
                    print(" ", end='')

        print()


rx = random.randint(1, rows - 2)
ry = random.randint(1, columns - 2)

while var:
    print("Score:", score)

    # Условия выхода за стенку
    if kor_player[0] == 0:
        print("Вам нельзя выходить за поле!")
        kor_player[0] += 1

    elif kor_player[0] == rows - 1:
        print("Вам нельзя выходить за поле!")
        kor_player[0] -= 1

    elif kor_player[1] == 0:
        print("Вам нельзя выходить за поле!")
        kor_player[1] += 1

    elif kor_player[1] == columns - 1:
        print("Вам нельзя выходить за поле!")
        kor_player[1] -= 1

    else:
        print()

    draw(rows, columns, kor_player, [rx, ry])

    inpt = input("Куда двигаемся?: ")

    # Условия передвежения персонажа
    if inpt == "d":
        kor_player[1] += 1

    elif inpt == "a":
        kor_player[1] -= 1

    elif inpt == "w":
        kor_player[0] -= 1

    elif inpt == "s":
        kor_player[0] += 1

    if rx == kor_player[0] and ry == kor_player[1]:
        score += 1
        rx = random.randint(1, rows - 2)
        ry = random.randint(1, columns - 2)

    os.system("cls")

    # Условие выхода из цикла
    if inpt.lower() == 'exit':
        var = False

