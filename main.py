#! python3

ROW_LEN = 3
Symbols = [" ", "O", "X"]
NUM_PLAYERS = 2

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


def make_move(player):
    pass

def game_over():
    return True, 0

def display_winner(winner):
    pass




if __name__ == "__main__":
    board = init_board()
    i = 0;
    while(True):
        print_board(board)
        make_move(i % NUM_PLAYERS)
        end, winner = game_over()
        if end:
            display_winner(winner)
            break;
