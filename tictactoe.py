import random
import sys


board = [" "for i in range(9)]  # Creating an array size of 9
print("TIC TAC TOE")

#Printing the TIC TAC TOE board

def print_board():
    row1 = "| {} | {} | {} |".format(board[0], board[1], board[2])
    row2 = "| {} | {} | {} |".format(board[3], board[4], board[5])
    row3 = "| {} | {} | {} |".format(board[6], board[7], board[8])
    print(row1)
    print(row2)
    print(row3)
    print()

#player_move() method will ask player to enter the position number


def player_move(icon):
    if icon == "X":
        var = "A"
    elif icon == "O":
        var = "B"
    print(" {} turn! ".format(var))
    choice1 = int(input("Enter Your move(1-9) ").strip())
    if(choice1 > 0 and choice1 <= 9):
        if(board[choice1-1] == " "):
            board[choice1-1] = icon
        else:
            print()
            print("oops, Space already filled!")
            print()
            player_move(icon)
    else:
        print("Inalid move. Please Try again!")
        player_move(icon)

#is_win(): This function having all possibilities for win. If any one possibliity is true it returns true


def is_win(icon):
    if(board[0] == icon and board[1] == icon and board[2] == icon) or\
        (board[3] == icon and board[4] == icon and board[5] == icon) or\
            (board[6] == icon and board[7] == icon and board[8] == icon) or\
        (board[0] == icon and board[3] == icon and board[6] == icon) or\
        (board[1] == icon and board[4] == icon and board[7] == icon) or\
        (board[2] == icon and board[5] == icon and board[8] == icon) or\
        (board[0] == icon and board[4] == icon and board[8] == icon) or\
            (board[2] == icon and board[4] == icon and board[6] == icon):
        return True
    else:
        return False

#is_draw(): This function will check status of draw


def is_draw():
    if(" " not in board):
        return True
    else:
        return False


while True:
    print_board()
    player_move("X")
    print_board()
    #Here, If statement will check "X" meets is_win() or not
    if(is_win("X")):
        print("Player X wins!")
        sys.exit()
    #if "X" didn't meet the is_win(), Then it will check is_draw() status
    elif(is_draw()):
        print("It's Draw")
        sys.exit()  # if function excecuted succefully it will exit.
    #if is_draw() is also didn't pass then it will move to next player

    #same as "X" here it will go with "O"
    player_move("O")
    if(is_win("O")):
        print_board()
        print("Player O wins!")
        sys.exit()
    elif(is_draw()):
        print("It's Draw")
        sys.exit()
