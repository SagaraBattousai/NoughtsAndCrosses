#! python3

ROW_LEN = 3
SYMBOLS = [" ", "O", "X"]
KEY = {"O" : 1, "X" : 2}
NUM_PLAYERS = 2
NUM_DIAGONALS = 2

#should pass around like with board
WINNER_BOARD = [0] * (ROW_LEN * 2 + NUM_DIAGONALS)

#could be global but safer not
def init_board():
    return [0] * (ROW_LEN * ROW_LEN)

def print_board(board):
    print("   1   2   3") #Removed expand tabs
    i = 1
    for elem in range(len(board)):
        symbol = SYMBOLS[board[elem]]

        if elem % ROW_LEN == 0 and elem != 0:
            print("\n  ___________\n" + str(i) + "  " + symbol, end='')
            i += 1
        elif elem == 0:
            print(str(i) + "  " + symbol, end='')
            i += 1
        else:
            print(" | " + symbol, end='')
    print("\n")


#Should throw error, Not recurse and return false, no error? but bad!
def make_move(player, board):
    try:
        move = input("player {}, make your move: ".format(player))
    except EOFError:
        print("Exiting game:") #Could say who is most likly to win or quitter lost
        exit(0)

    if move.lower() == "help":
        print("please type two numbers, row followed by " +
         "column, with or without space") 
        move = input("player {}, make your move: ".format(player))

    location = move.strip()
    location_size = len(location)

    if location_size != 2:
        size = "few" if  location_size < 2 else "many" #shouldnt add space incase reuse
        print("too " + size + " numbers, please use only two, " +
                "one for row followed by one for column")
        make_move(player, board)
        return

#    index = get_board_location(move.strip())
    row = int(location[0]) - 1
    column = int(location[1]) - 1

    if row < 0 or row >= ROW_LEN:
        print("row should be between 0 and " + str(ROW_LEN - 1))
        make_move(player, board)
        return

    if column < 0 or column >= ROW_LEN:
        print("column should be between 0 and " + str(ROW_LEN - 1))
        make_move(player, board)
        return
    index = ROW_LEN * row + column

    if board[index] == 0:
        board[index] = player
    else:
        print("player {}, you cant move there! Someone else ".format(player) +
                "is there, please choose again:")
        make_move(player, board)
        return
    return game_over(player, row, column)


#Use later when update to use class' and custom exceptions
# def get_board_location(location):
#     row = int(location[0]) - 1
#     column = int(location[1]) - 1

#     if
    
#     return ROW_LEN * row + column




    


def game_over(player, row, column):
    #Since 2 players (1 and 2) and want -1 and 1
    #first make distance = 2 (1 and 2 have distance 1)
    #1*2 = 2, 2*2 = 4, so now have 2 and 4 (distance 2)
    #now - 3 to get -1 and 1
    value = player * NUM_PLAYERS - (NUM_PLAYERS + 1)

    index = row
    print(WINNER_BOARD)
    print(index)

    WINNER_BOARD[index] += value
    if abs(WINNER_BOARD[index]) >= ROW_LEN:
        return True

    index = ROW_LEN + column

    WINNER_BOARD[index] += value
    if abs(WINNER_BOARD[index]) >= ROW_LEN:
        return True

    if row == column:
        index = 2 * ROW_LEN

        WINNER_BOARD[index] += value
        if abs(WINNER_BOARD[index]) >= ROW_LEN:
            return True
    if (ROW_LEN - 1 - column) == row:
        index = 2 * ROW_LEN + 1

        WINNER_BOARD[index] += value
        if abs(WINNER_BOARD[index]) >= ROW_LEN:
            return True




    return False

def display_winner(winner):
    print("MEEEE")
    pass




if __name__ == "__main__":
    board = init_board()
    i = 0;
    while(True):
        print_board(board)

        player = (i % NUM_PLAYERS) + 1
        end = make_move(player, board)

        if end:
            display_winner(player)
            break;
        i += 1
