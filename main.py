#! python3

ROW_LEN = 3
Symbols = [" ", "O", "X"]

def init_board():
    return [0,0,0,0,0,0,0,0,0]

def print_board(board):
    for elem in range(len(board)):
        symbol = Symbols[board[elem]]

        if elem % ROW_LEN == 0 and elem != 0:
            print("\n______\n" + symbol, end='')
        elif elem == 0:
            print(symbol, end='')
        else:
            print("|" + symbol, end='')



if __name__ == "__main__":
    board = init_board()
    print_board(board)

    while(True):
        
