# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

import random

candiesNum = 2021
candiesMax = 28

print(f"Правила игры:\n\
\tНа столе лежит {candiesNum} конфета.\n\
\tИграют два игрока делая ход друг после друга.\n\
\tПервый ход определяется жеребьёвкой. За один ход можно забрать не более чем {candiesMax} конфет.\n\
\tВсе конфеты оппонента достаются сделавшему последний ход.\n\
\tСколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?")

print("Режим игры:\n\
    \t1 - Человек против Человека\n\
    \t2 - Человек против бота\n\
    \t3 - Человек против бота с 'интеллектом'\
    ")
mode = int(input("Введите режим: "))

def move(playerNum, candiesNum, mode):
    while (True):
        if mode == 2 and playerNum==1:          # bot mode
            if candiesMax>candiesNum:
                candiesLimit = candiesNum
            else:
                candiesLimit = candiesMax
            candies = random.randint(1,candiesLimit)
            print(f"Ходит бот. Берет {candies} конфет")
        
        elif mode == 3 and playerNum==1:            # smart bot mode
            if candiesNum <= candiesMax:            # take all candies!!!
                candies = candiesNum
            else:
                remainder = candiesNum % candiesMax
                if remainder==0 or remainder == 1 :    # no matter how much candies we take
                    candies = random.randint(1,candiesMax)
                else:
                    candies = remainder - 1
            print(f"Ходит бот. Берет {candies} конфет")
        
        else:                               # human mode
            candies = int(input(f"Ходит Игрок {playerNum+1}, сколько конфет берем? "))
        
        if 0<candies<=28 and candiesNum>=candies:
            candiesNum -= candies
            break
        else:
            print("Ошибка ввода. Повторите!")
            continue
    print(f"Осталось {candiesNum} конфет")
    return candiesNum
            
playerNum = random.randint(0,1)
print(f"Первым ходит Игрок {playerNum+1}!")

if mode == 1:
    while(candiesNum):
        candiesNum = move(playerNum,candiesNum)
        if candiesNum == 0:
            break
        playerNum = (playerNum+1)%2
else:
    while(candiesNum):
        candiesNum = move(playerNum,candiesNum, mode)
        if candiesNum == 0:
            break
        playerNum = (playerNum+1)%2
        
if (mode==2 or mode==3) and playerNum==1:
    print(f"Выиграл бот!")
else:
    print(f"Выиграл Игрок {playerNum+1}!")

