import os
from board import *

invalid_input_message = "Please enter a valid input: "
chess_board = []


def clear_screen():
    os.system('cls')


def press_to_continue():
    input("\nPress \'ENTER\' to continue...\n")


def game_introduction():
    print("WELCOME TO MONSTER CHESS")
    press_to_continue()

    clear_screen()

    print("The rules of the game are simple. It's like normal chess, ")
    print("but one side has a single piece--the monster. It moves just ")
    print("like a normal king, but with a catch; it takes two turns instead ")
    print("of one like the other player. ")
    print()

    print("To move a piece as player one, give the location of the piece you ")
    print("would like to move as a pair, such as A2, to move the leftmost pawn.")
    print("Then, give the location of where you would like to move the piece ")
    print("to, also as a pair.")
    print()

    print("As player two has only one piece, you will just be given the option ")
    print("of where you would like to move.")

    press_to_continue()
    clear_screen()


def convert_coordinates(letter_coord, number_coord):
    col = 0
    for index, letter in enumerate(chess_letters):
        if letter_coord == letter:
            col = index

    row = 9 - int(number_coord)

    return [row, col]


def check_user_input_formatting(piece_information):
    if len(piece_information) != 2:
        return False

    first_char = piece_information[0]
    second_char = piece_information[1]

    if not first_char.isalpha() or not second_char.isnumeric():
        return False

    return True


def is_valid_piece(piece_location, board):
    # check that the user input was formatted correctly
    if not check_user_input_formatting(piece_location):
        return False

    row, col = convert_coordinates(piece_location[0], piece_location[1])

    if board[row][col].name == "Empty":
        return False

    return True


def check_loop(boolean_function, piece_string):
    while True:
        if boolean_function(piece_string):
            break
        else:
            piece_string = input(invalid_input_message)


def player_one_turn(player_name, game_board):
    print(player_name, end=" ")
    user_piece_selection = input("it is your turn. Select a piece to move: ")

    check_loop(is_valid_piece, user_piece_selection)

    # check_loop(is_valid_piece, user_piece_selection, game_board)

    # piece_destination = input("Where do you move it: ")
    # check_loop(valid_destination, piece_destination, board)

    # move the piece


game_introduction()

# PLAYER SELECTION
player_one_name = input("Player One, you will be the normal King. Enter your name: ")
player_two_name = input("Player Two, you will be the monster. Enter your name: ")
print()

chess_board = initialize_board()

# GAME LOOP
# Start on player one's turn

# Player One, select a piece
# get user input
# Where would you like to move it?
# get user input
# move piece


turn_count = 0
while True:
    print_board(chess_board)

    if turn_count % 2 == 0:
        player_one_turn(player_one_name, chess_board)

    # else:
    #     player_two_turn(player_two_name, chess_board)

    turn_count += 1
