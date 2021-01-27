#-----------Global variable ------

#-----Game board -----
board = ["-","-","-",
        "-","-","-",
        "-","-","-",]

#if game is still playing
game_still_playing = True

# who won ? or tie
winner = None

#Whos turn is it
current_player = "x"

#display turn
def display_board():
    print(board[0] + " | "+board[1] + " | "+board[2])
    print(board[3] + " | "+board[4] + " | "+board[5])
    print(board[6] + " | "+board[7] + " | "+board[8])

#play a game of tictactoe
def play_game():

    #Display initial board
    display_board()

    #While the game is still playing
    while game_still_playing:

        #handle a single turn of a player
        handle_turn(current_player)

        #check if the game has endend
        check_if_game_over()

        #flip to the othe rplayer
        flip_player()

 # The game has endend
if winner == "x" or winner =="o":
 print(winner + " won.")
elif winner == None:
 print(" Tie.")

#handle a single turn of a player
def handle_turn(player):

    print(player + "'s turn.")
    position = input("choose a position fro  1-9:")
    
    valid = False
    while not valid:

        while position not in ["1", "2", "3", "4", "5", "6", "7", "8","9"]:
            position = input("Invalid position. Choose a position from 1-9:")

        position = int(position) - 1

        if board[position] == "-":
            valid = True
            print("You cannot go there. Go again.")

        board[position] = player 

        display_board()


def check_if_game_over():
    check_for_winner()
    check_for_tie()


def check_for_winner():

    #setting up global variables
    global winner

    #checkrows
    row_winner = check_rows()
    #check columns
    column_winner = check_columns()
    #check diagonals
    diagonal_winner = check_diagonals() 

    #get winner
    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None    
    return



def check_rows():
    #set up global variable
    global game_still_playing
    #check if any of the rows has same value and not empty
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"
    #if any row does have a match flag thats a win
    if row_1 or row_2 or row_3:
        game_still_playing = False
        # return the winner ( Xor O)
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return


def check_columns():
    #set up global variable
    global game_still_playing
    #check if any of the rows has same value and not empty
    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"
    #if any column does have a match flag thats a win
    if column_1 or column_2 or column_3:
        game_still_playing = False
        # return the winner ( Xor O)
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    return
    

def check_diagonals():
    #set up global variable
    global game_still_playing
    #check if any of the rows has same value and not empty
    diagonal_1 = board[0] == board[4] == board[8] != "-"
    diagonal_2= board[6] == board[4] == board[2] != "-"
    #if any diagonal does have a match flag thats a win
    if diagonal_1 or diagonal_2:
        game_still_playing = False
        # return the winner ( Xor O)
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[6]
    return


def check_for_tie():
    #global variable
    global game_still_playing
    if "-" not in board:
        game_still_playing = False
    return


def flip_player():
    #global Variable
    global current_player
    #if current player was x the change to O
    if current_player == "x":
     current_player = "o"
    #if current player was o the change to x
    elif current_player =="o":
        current_player = "x"
    return


play_game()


#board
#display board
#play game
#handle a turn
#check win 
 #check rows
  #check columns
  #chesck diagnols
#check tie
#flip player
