from random import randint

board = []
# Create a list of lists.
for x in range(5):
    board.append(["O"] * 5)
    

def print_board(board):
    # Display the board nicely.
    for row in board:
        print " ".join(row)

print "Let's play Battleship!"
print_board(board)

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

def three_by_one_ship(board):
    orientation = randint(0, 1)
    if orientation == 0:
        horizontal_orientation_col_start = randint(0, len(board) - 3)
        horizontal_orientation_col_end = horizontal_orientation_start + 3
        big_ship_row_start = randint(0, len(board) - 1)
        big_ship_row_end = big_ship_row_start
        first_coordinate = (big_ship_row_start, big_ship_col_start)
        second_coordinate = (big_ship_row_end, big_ship_col_end)
        return big_ship_coordinates = {big_ship_row_start: range(big_ship_col_start, big_ship_col_end + 1)}
    else: 
        vertical_orientation_row_start = randint(0, len(board) - 3)
        vertical_orientation_row_end = horizontal_orientation_start + 3
        big_ship_col_start = randint(0, len(board) - 1)
        big_ship_col_end = big_ship_col_start
        first_coordinate = (big_ship_row_start, big_ship_col_start)
        second_coordinate = (big_ship_row_end, big_ship_col_end)
        return big_ship_coordinates = {big_ship_col_start: range(big_ship_row_start, big_ship_row_end + 1)}


def two_by_one_ship(big_ship_coordinates, board):
    orientation = randint(0, 1)
    while intersect == True : 
        if orientation == 0:
            horizontal_orientation_col_start = randint(0, len(board) - 2)
            horizontal_orientation_col_end = horizontal_orientation_start + 2
            small_ship_row_start = randint(0, len(board) - 1)
            small_ship_row_end = small_ship_row_start
            first_coordinate = (small_ship_row_start, small_ship_col_start)
            second_coordinate = (small_ship_row_end, small_ship_col_end)
            small_ship_coordinates = {small_ship_row_start: range(small_ship_col_start, small_ship_col_end + 1)}
            print small_ship_coordinates
        else: 
            vertical_orientation_row_start = randint(0, len(board) - 3)
            vertical_orientation_row_end = horizontal_orientation_start + 3
            small_ship_col_start = randint(0, len(board) - 1)
            small_ship_col_end = small_ship_col_start
            first_coordinate = (small_ship_row_start, small_ship_col_start)
            second_coordinate = (small_ship_row_end, small_ship_col_end)
            small_ship_coordinates = {range(small_ship_row_start, small_ship_row_end + 1): small_ship_col_start}
            print small_ship_coordinates
        for key in big_ship_coordinates:
            if key == small_ship_coordinates.keys():
                intersect == True
            else:
                intersect == False
    return small_ship_coordinates


# Generate the coordinates of the ship by referring to the 
# respective functions.
ship_row = random_row(board)
ship_col = random_col(board)

# Arbitrarily set the limit to four turns.
for turn in range(0, 4):
    # Placed the turn statement at the start of the turn,
    # as that made most sense to me.
    print "Turn", turn + 1
    
    # Take a guess from the user. Notice it is a coordinate.
    guess_row = int(raw_input("Guess Row:"))
    guess_col = int(raw_input("Guess Col:"))

    # Check to see if the player has won the game by
    # correctly guessing the coordinates. Terminate the
    # game if it has been won.
    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk my battleship!"
        break
    # If the user did not win, check various other possibilities.
    else:
        # Make sure they are within the scope of the sea.
        # Notice, it uses up a turn.
        if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
            print "Oops, that's not even in the ocean."
            turn -= 1
        # Make sure that it corresponds to the board for the user to understand. Zero starts are for machines...
        elif(board[guess_row - 1][guess_col - 1] == "X"):
            print "You guessed that one already."
        else:
            print "You missed my battleship!"
            board[guess_row - 1][guess_col - 1] = "X"
        print_board(board)
        if turn == 3:
            print ("Game Over")


