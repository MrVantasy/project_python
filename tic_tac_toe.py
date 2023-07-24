import time
import random

print("\nWelcome to the Tic-Tac-Toe Games!\n")
time.sleep(1)

board = ["", " ", " ", " ", " ", " ", " ", " ", " ", " "]

def print_board():
    row1 = "| {} | {} | {} |".format(board[1], board[2], board[3])
    row2 = "| {} | {} | {} |".format(board[4], board[5], board[6])
    row3 = "| {} | {} | {} |".format(board[7], board[8], board[9])

    print()
    print(row1)
    print("-------------")
    print(row2)
    print("-------------")
    print(row3)
    print()

def player_bot_move(icon):
    if icon == "X":
        print("Now it's your turn.")
        time.sleep(1)
        choice = int(input("Enter your move (1-9): "))
    
        if board[choice] == " ":
            board[choice] = icon
        else:
            print("That space is not empty!")
            time.sleep(1)
    elif icon == "O":
        print("It's the other turn.")
        time.sleep(1)
        bot_choice = random.randint(1, 9)
    
        if board[bot_choice] == " ":
            board[bot_choice] = icon
        else:
            print("That space is not empty!")
            time.sleep(1)

def is_win(icon):
    if (board[1] == icon and board[2] == icon and board[3] == icon) or \
       (board[4] == icon and board[5] == icon and board[6] == icon) or \
       (board[7] == icon and board[8] == icon and board[9] == icon) or \
       (board[1] == icon and board[4] == icon and board[7] == icon) or \
       (board[2] == icon and board[5] == icon and board[8] == icon) or \
       (board[3] == icon and board[6] == icon and board[9] == icon) or \
       (board[1] == icon and board[5] == icon and board[9] == icon) or \
       (board[3] == icon and board[5] == icon and board[7] == icon):
        return True
    else:
        return False

def is_draw():
    if " " not in board:
        return True
    else:
        return False

while True:
    print_board()
    player_bot_move("X")
    print_board()
    if is_win("X"):
        print("Congrats, You Win!")
        break
    elif is_draw():
        print("Tie!")
        break
    player_bot_move("O")
    if is_win("O"):
        print_board()
        print("You Lose!")
        break
    elif is_draw():
        print("Tie!")
        break