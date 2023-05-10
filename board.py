from pieces import *


chess_letters = ["X", "A", "B", "C", "D", "E", "F", "G", "H"]


def initialize_board():
    board = create_board()
    create_axes(board)
    add_pieces(board)

    return board


def create_board():
    board = []

    for i in range(0, 9):
        row = []
        for j in range(0, 9):
            row.append(GamePiece("Empty", "-", i, j))
        board.append(row)

    return board


def create_axes(board):
    for i, row in enumerate(board):
        for j, col in enumerate(row):
            if i == 0:
                board[i][j].symbol = chess_letters[j]
            elif j == 0:
                board[i][j].symbol = abs(i - 8) + 1

    board[0][0].symbol = " "


def add_pieces(board):
    # normal player's pieces below

    # Pawns
    for i in range(1, 9):
        board[7][i] = Pawn(6, 1)

    # Rooks
    board[8][1] = Rook(8, 1)
    board[8][8] = Rook(8, 1)

    # Knights
    board[8][2] = Knight(8, 2)
    board[8][7] = Knight(8, 7)

    # Rooks
    board[8][3] = Bishop(8, 3)
    board[8][6] = Bishop(8, 6)

    # Queen
    board[8][4] = Queen(8, 4)

    # King
    board[8][5] = King(8, 5)

    # Monster
    board[1][5] = Monster(1, 5)


def print_board(board_list):
    for row in board_list:
        for piece in row:
            piece.draw()
        print()
    print()
