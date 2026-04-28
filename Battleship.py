"""
Battleship
Student Name: Jackson Lieberman
Date: 
Discription: 
Play battleship against another player
Bonuses: tell player how far they are,  bot that picks randomly
Bugs: 
Log: 1.1
"""


from math import dist
import random

board_p1 = ['X', 'X', 'X', 'X', 'X',                                                               #player 1 board
            'X', 'X', 'X', 'X', 'X',
            'X', 'X', 'X', 'X', 'X',
            'X', 'X', 'X', 'X', 'X',
            'X', 'X', 'X', 'X', 'X']

board_p1_display = ['X', 'X', 'X', 'X', 'X',                                                       #the board player 1 sees
                    'X', 'X', 'X', 'X', 'X',
                    'X', 'X', 'X', 'X', 'X',
                    'X', 'X', 'X', 'X', 'X',
                    'X', 'X', 'X', 'X', 'X']

board_p2 = ['X', 'X', 'X', 'X', 'X',                                                               #player 2 board
            'X', 'X', 'X', 'X', 'X',
            'X', 'X', 'X', 'X', 'X',
            'X', 'X', 'X', 'X', 'X',
            'X', 'X', 'X', 'X', 'X']

board_p2_display = ['X', 'X', 'X', 'X', 'X',                                                       #the board player 2 sees
                    'X', 'X', 'X', 'X', 'X',
                    'X', 'X', 'X', 'X', 'X',
                    'X', 'X', 'X', 'X', 'X',
                    'X', 'X', 'X', 'X', 'X']



def place_dots(board):
    '''
    Places 4 dots randomly on the board
    '''
    dots_placed = 0                             
    while dots_placed < 4:                                                                         # When there are less than 4 dots
        spot = random.randint(0, 24)                                                               #choses a random spot
        if board[spot] == 'X':                                                                     #if the spot is an X
            board[spot] = 'D'                                                                      #replace it with a D
            dots_placed += 1                                                                       #add one to the number of dots placed

def print_board(board):
    '''Print the board in a 5x5 grid'''
    print()                                                                                        #blank line for asthetics
    for i in range(5):                                                                             #print the board line by line
        print(board[i*5], board[i*5+1], board[i*5+2], board[i*5+3], board[i*5+4])
    print()                                                                                        #blank line for asthetics


def shoot(board, display_board, row, col):
    ''' Convert row/col (1-5) to a index, check hit or miss'''
    index = (row - 1) * 5 + (col - 1)                                                              #gets the index on the board

    if board[index] == 'D':                                                                        #if the index is a dot        
        print("You hit one!")                                                                      #tell the user they hit a dot
        board[index] = 'H'                                                                         #changes the spot on the board to a H
        display_board[index] = 'H'                                                                 #changes the spot on the display board to a H
        return True                                                                                #a hit
    else:
        print("You missed!")                                                                       #tell user they missed
        display_board[index] = 'M'                                                                 #change the spot on the board to a M
        dist = closest_dot_distance(index, board)                                                  #get distance to nearest dot
        print(f"Closest dot is {dist} squares away.")                                              #tell the user
        return False                                                                               #a miss
  


def take_turn(player, hits_p1, hits_p2, shots_left):
    ''' The players move'''
    if player == 1:                                                                                #if its player 1s turn
        my_board   = board_p2                                                                      #set the boards accordingly
        my_display = board_p2_display
    else:                                                                                          #if not set the boards to player 2
        my_board   = board_p1           
        my_display = board_p1_display

    print(f"Player {player}'s turn")                                                               #print whose turn it is
    print(f"Here is the board you are shooting at:")
    print_board(my_display)                                                                        #announces and shows the board being shot at
    print(f"You have {shots_left} shots left.")                                                    #tells how many shots are left
           
    try:
        row = int(input("What row would you like to shoot at (1-5): "))                            #asks for row
        col = int(input("What col would you like to shoot at (1-5): "))                            #asks for col
    except ValueError:                                                                             #if they didnt enter an integer
        print("Please enter a number.")                                                            #ask for correction
        return None, hits_p1, hits_p2                                                              #have the user answer again
    if row < 1 or row > 5 or col < 1 or col > 5:                                                   #if the number is more than 5
        print("That is an invalid move.")                                                          #say that its invalid
        return None, hits_p1, hits_p2                                                              #have the user answer again

    index = (row - 1) * 5 + (col - 1)                                                              #now we can get an index
    if my_display[index] == 'H' or my_display[index] == 'M':                                       #if they have already shot
        print("You already shot there!")                                                           #tell the user
        return None, hits_p1, hits_p2                                                              #have the user answer again

    if shoot(my_board, my_display, row, col):                                                      #if the shot function is true
        if player == 1:                                                                            #if its player 1
            hits_p1 += 1                                                                           #increase the number of hits for player 1
        else:                                                                                      #if not increase for player 2
            hits_p2 += 1

    if (player == 1 and hits_p1 == 4) or (player == 2 and hits_p2 == 4):                           #if either player has hit 4 dots
        print(f"Player {player} wins! All dots sunk!")                                             #tell this
        return True, hits_p1, hits_p2                                                              #say they hit

    return False, hits_p1, hits_p2                                                                 #say they didnt hit

def bot_turn(hits_p2):
    '''Bot randomly picks a spot that hasnt been shot yet'''
    available = []
    for i in range(25):                                                                            #for all spots
        if board_p1_display[i] == 'X':                                                             #check if they haven't been hit/missed
            available.append(i)                                                                    #if not then put them in a list

    spot = random.choice(available)                                                                #pick a random one
    row = spot // 5 + 1                                                                            # convert index back to row/col
    col = spot % 5 + 1

    print(f"Bot shoots at row {row}, col {col}")                                                   #print where the bot is shooting
    if shoot(board_p1, board_p1_display, row, col):                                                #if it hits
        hits_p2 += 1                                                                               #add one to the hits
        print('Bot Board')                                                                                   
        print_board(board_p1_display)                                                              #shows the board


    if hits_p2 == 4:                                                                               #if it has hit 4 dots
        print("Bot wins! All dots sunk!")                                                          #display that
        return True, hits_p2                                                                       #return player 2 (the bot) winning

    return False, hits_p2                                                                          #return it didnt hit

def closest_dot_distance(index, board):
    '''Returns how many squares away the closest dot is'''
    row = index // 5                                                                               #Find the row that was shot at
    col = index % 5                                                                                #find the col
    min_dist = 999                                                                                 #set a minimum distance
    for i in range(25):                                                                            #out of all the spaces
        if board[i] == 'D':                                                                        #if its a dot
            dot_row = i // 5                                                                       #find its row
            dot_col = i % 5                                                                        #find its collumn
            dist = abs(row - dot_row) + abs(col - dot_col)                                         # get the distance
            if dist < min_dist:                                                                    #if the distance is less than the miniumun distance
                min_dist = dist                                                                    #set that distance to the minimum
    return min_dist                                                                                #retuns


def main():
    shots_left = 10                                                                                #defines variables
    hits_p1 = 0
    hits_p2 = 0
    place_dots(board_p1)                                                                           # places the dots on both boards
    place_dots(board_p2)

    print("Welcome to Dot Wars!")                                                                  # welcome message
    mode = input("Play against a bot or human? (b/h): ").lower()                                   #ask if they wanna play a human or bot
    while shots_left > 0 and (hits_p1 < 4 or hits_p2 < 4):                                         #while shots remain and game isn't over

        if hits_p1 < 4:                                                                            # player 1 goes if they haven't won
            result, hits_p1, hits_p2 = take_turn(1, hits_p1, hits_p2, shots_left)
            if result == True:                                                                     # player 1 won
                break                                                                              #end the code
            if result == None:                                                                     # invalid input, don't subtract a shot
                continue                                                                           #ask again
        if hits_p2 < 4:                                                                            # player 2 goes if they haven't won
            if mode == 'b':                                                                        #if the player wants to play a bot
                result, hits_p2 = bot_turn(hits_p2)                                                #give the bot a turn
            else:
                result, hits_p1, hits_p2 = take_turn(2, hits_p1, hits_p2, shots_left)
            if result == True:                                                                     # player 2 won
                break                                                                              #end the code
            if result == None:                                                                     #invalid input
                continue                                                                           #ask again

        shots_left -= 1                                                                            # only subtract a shot after both players go

    if shots_left == 0:                                                                            #if no one has shots left
        print("Out of shots! Game over.")                                                          #say that 
        print(f"P1 hits: {hits_p1}/4")
        print(f"P2 hits: {hits_p2}/4")                                                             #print who hit 


if __name__ == "__main__":
    main()