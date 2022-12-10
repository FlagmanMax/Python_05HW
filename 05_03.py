# Создайте программу для игры в ""Крестики-нолики"".
import random

board = list(range(1,10))

def print_board(board):
    for i in range(3):
        print("-------------", end="\n")
        print(f"| {board[3*i]} | {board[3*i+1]} | {board[3*i+2]} |")
    print("-------------", end="\n")

def input_value(board, player): 
    while True:
        print(f"Очередь игрока {player}, куда сделаем ход?")
        val = int(input())
        if (val<1) and (val>9):
            print("Ошибка ввода. Попробуйте еще раз")
            continue
        elif val in board:
            if player == 1:
                board[val-1] = 'X'
            else:
                board[val-1] = 'O'
            break
        else:
            print("Ошибка ввода. Попробуйте еще раз")
            continue
    return board

def check_board(board):
    win = 0
    winner = ((0,1,2),(3,4,5),(6,7,8),(0,4,8),(2,4,6),(0,3,6),(1,4,7),(2,5,8))
    for tu in winner:
        if board[tu[0]] == board[tu[1]] == board[tu[2]]:
            win = 1
            break
    return win

move = 9
win = 0
player = random.randint(0,1)
print_board(board)

while move:
    board = input_value(board, player+1)
    print_board(board)
    
    if check_board(board):
        win = 1
        break
    
    move -= 1
    player = (player+1)%2

if win > 0:
    print(f"Победил игрок {player+1}")
else:
    print("Ничья")
    

