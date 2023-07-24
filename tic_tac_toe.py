board = [" " for _ in range(9)]

def print_board():
    row1 = "| {} | {} | {} |".format(board[0], board[1], board[2])
    row2 = "| {} | {} | {} |".format(board[3], board[4], board[5])
    row3 = "| {} | {} | {} |".format(board[6], board[7], board[8])

    print()
    print(row1)
    print("-------------")
    print(row2)
    print("-------------")
    print(row3)
    print()

def player_move(icon):
    if icon == "X":
        print("Now it's your turn.")
    elif icon == "O":
        print("It's the other turn.")
    
    choice = int(input("Enter your move (1-9): "))
    if board[choice - 1] == " ":
        board[choice - 1] = icon
    else:
        print()
        print("That space is taken!")

def is_win(icon):
    if (board[0] == icon and board[1] == icon and board[2] == icon) or \
       (board[3] == icon and board[4] == icon and board[5] == icon) or \
       (board[6] == icon and board[7] == icon and board[8] == icon) or \
       (board[0] == icon and board[3] == icon and board[6] == icon) or \
       (board[1] == icon and board[4] == icon and board[7] == icon) or \
       (board[2] == icon and board[5] == icon and board[8] == icon) or \
       (board[0] == icon and board[4] == icon and board[8] == icon) or \
       (board[2] == icon and board[4] == icon and board[6] == icon):
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
    player_move("X")
    print_board()
    if is_win("X"):
        print("Congrats, You Win!")
        break
    elif is_draw():
        print("It's a draw!")
        break
    player_move("O")
    if is_win("O"):
        print_board()
        print("You Lose!")
        break
    elif is_draw():
        print("It's a draw!")
        break