

theBoard = {'7': ' ', '8': ' ', '9': ' ',
            '4': ' ', '5': ' ', '6': ' ',
            '1': ' ', '2': ' ', '3': ' '}


board_keys = []

for key in theBoard:

    board_keys.append(key)
        

def printBoard(board):

    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])

def game():

    turn = 'X'

    count = 0

    for i in range(10):

        printBoard(theBoard)
        print('It is your turn, ' + turn + '. Where would you like to move?')

        move = input()

        if theBoard[move] == ' ':
            
            theBoard[move] = turn

            count += 1
        
        else:

            print("That place has already been taken.\nWhere do you want to move?")

            continue

        if count >= 5:

            if theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ':

                printBoard(theBoard)

                print('Game over\n')

                print(' **** '   + turn + ' won ****')

                break

            elif theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ':

                printBoard(theBoard)

                print('Game over\n')

                print(' **** ' + turn + ' won ****')

                break
            
            elif theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ':

                printBoard(theBoard)

                print('Game over\n')

                print(' **** ' + turn + ' won ****')

                break

            elif theBoard['1'] == theBoard['4'] == theBoard['7'] != ' ':

                printBoard(theBoard)

                print('Game over\n')

                print(' **** ' + turn + ' won ****')

                break

            elif theBoard['2'] == theBoard['5'] == theBoard['8'] != ' ':

                printBoard(theBoard)

                print('Game over\n')

                print(' **** ' + turn + ' won ****')

                break

            elif theBoard['3'] == theBoard['6'] == theBoard['9'] != ' ':

                printBoard(theBoard)

                print('Game over\n')

                print(' **** ' + turn + ' won ****')

                break

            elif theBoard['7'] == theBoard['5'] == theBoard['3'] != ' ':

                printBoard(theBoard)

                print('Game over\n')

                print(' **** ' + turn + ' won ****')

                break

            elif theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ':

                printBoard(theBoard)

                print('Game over\n')

                print(' **** ' + turn + ' won ****')

                break
        
        if count == 9:
            print("\nGame Over!\n")
            print("It's a tie!")

        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'
        
    restart = input("Do you want to play again? (y/n)? ")
    if restart == "y" or restart == "Y":
        for key in board_keys:
            theBoard[key] = " "
        
        game()

if __name__ == "__main__":
    game()
        

