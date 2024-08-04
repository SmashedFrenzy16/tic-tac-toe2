
def check_grid(move, grid):
    if move == 1:
        if grid[0][0] == "X" or grid[0][0] == "O":
            return False
        else:
            return True
    elif move == 2:
        if grid[0][1] == "X" or grid[0][1] == "O":
            return False
        else:
            return True
    elif move == 3:
        if grid[0][2] == "X" or grid[0][2] == "O":
            return False
        else:
            return True
    elif move == 4:
        if grid[1][0] == "X" or grid[1][0] == "O":
            return False
        else:
            return True
    elif move == 5:
        if grid[1][1] == "X" or grid[1][1] == "O":
            return False
        else:
            return True
    elif move == 6:
        if grid[1][2] == "X" or grid[1][2] == "O":
            return False
        else:
            return True
    elif move == 7:
        if grid[2][0] == "X" or grid[2][0] == "O":
            return False
        else:
            return True
    elif move == 8:
        if grid[2][1] == "X" or grid[2][1] == "O":
            return False
        else:
            return True
    elif move == 9:
        if grid[2][2] == "X" or grid[2][2] == "O":
            return False
        else:
            return True

def check_win_x():

    if grid[0][0] == "X" and grid[0][1] == "X" and grid[0][2] == "X":
        return True
    elif grid[1][0] == "X" and grid[1][1] == "X" and grid[1][2] == "X":
        return True
    elif grid[2][0] == "X" and grid[2][1] == "X" and grid[2][2] == "X":
        return True
    elif grid[0][0] == "X" and grid[1][0] == "X" and grid[2][0] == "X":
        return True
    elif grid[0][1] == "X" and grid[1][1] == "X" and grid[2][1] == "X":
        return True
    elif grid[0][2] == "X" and grid[1][2] == "X" and grid[2][2] == "X":
        return True
    elif grid[0][0] == "X" and grid[1][1] == "X" and grid[2][2] == "X":
        return True
    elif grid[0][2] == "X" and grid[1][1] == "X" and grid[2][0] == "X":
        return True

def check_win_o():

    if grid[0][0] == "O" and grid[0][1] == "O" and grid[0][2] == "O":
        return True
    elif grid[1][0] == "O" and grid[1][1] == "O" and grid[1][2] == "O":
        return True
    elif grid[2][0] == "O" and grid[2][1] == "O" and grid[2][2] == "O":
        return True
    elif grid[0][0] == "O" and grid[1][0] == "O" and grid[2][0] == "O":
        return True
    elif grid[0][1] == "O" and grid[1][1] == "O" and grid[2][1] == "O":
        return True
    elif grid[0][2] == "O" and grid[1][2] == "O" and grid[2][2] == "O":
        return True
    elif grid[0][0] == "O" and grid[1][1] == "O" and grid[2][2] == "O":
        return True
    elif grid[0][2] == "O" and grid[1][1] == "O" and grid[2][0] == "O":
        return True
    else:
        return False

grid = [
    ["", "", ""],
    ["", "", ""],
    ["", "", ""],
]

for element in grid:

    print(element)


while True:

    player1 = input("Player 1, enter the square you would like to mark: ")

    if player1 == "1" and check_grid(int(player1), grid) == True:
        grid[0][0] = "X"
    elif player1 == "2":
        grid[0][1] = "X"
    elif player1 == "3":
        grid[0][2] = "X"
    elif player1 == "4":
        grid[1][0] = "X"
    elif player1 == "5":
        grid[1][1] = "X"
    elif player1 == "6":
        grid[1][2] = "X"
    elif player1 == "7":
        grid[2][0] = "X"
    elif player1 == "8":
        grid[2][1] = "X"
    elif player1 == "9":
        grid[2][2] = "X"

    for element in grid:

        print(element)

    if check_win_x() == True:
        print("Player 1 wins!")
        break
    elif check_win_o() == True:
        print("Player 2 wins!")
        break

    player2 = input("Player 2, enter the square you would like to mark: ")

    if player2 == "1" and check_grid(int(player2), grid) == True:
        grid[0][0] = "O"
    elif player2 == "2":
        grid[0][1] = "O"
    elif player2 == "3":
        grid[0][2] = "O"
    elif player2 == "4":
        grid[1][0] = "O"
    elif player2 == "5":
        grid[1][1] = "O"
    elif player2 == "6":
        grid[1][2] = "O"
    elif player2 == "7":
        grid[2][0] = "O"
    elif player2 == "8":
        grid[2][1] = "O"
    elif player2 == "9":
        grid[2][2] = "O"

    for element in grid:

        print(element)

    if check_win_x() == True:
        print("Player 1 wins!")
        break
    elif check_win_o() == True:
        print("Player 2 wins!")
        break
