"""
Battleship - Pygame Version
Student Name: Jackson Lieberman
Sources: https://www.pygame.org/docs/, https://www.youtube.com/watch?v=AY9MnQ4x3zk, https://www.youtube.com/watch?v=y9VG3Pztok8, https://www.youtube.com/watch?v=ndtFoWWBAoE
Bonuses: Built in pygame
Date:
Description: Dot Wars in pygame
Log: 2.0
"""


import pygame
import random

pygame.init()                                                                       #set up pygame (initialize)

CELL_SIZE = 100                                                                     #each square is 100x100 pixels
GRID_SIZE = 5                                                                       #5x5 board
TEXT_HEIGHT = 80                                                                    #height of the text bar at the top
WIDTH  = CELL_SIZE * GRID_SIZE                                                      #500
HEIGHT = CELL_SIZE * GRID_SIZE + 80                                                 #580 (extra space at bottom for text)

font = pygame.font.SysFont(None, 36)                                                #sets the font of the caption
small_font = pygame.font.SysFont(None, 28)                                          #smaller font for in-cell labels

screen = pygame.display.set_mode((WIDTH, HEIGHT))                                   #sets the hight and width in pygame
pygame.display.set_caption("Dot Wars")                                              #sets the caption of the display 
font = pygame.font.SysFont(None, 36)                                                #sets the font of the caption

BLUE  = (70, 130, 180)                                                              #sets the colors
RED   = (200, 50, 50)     
GRAY  = (160, 160, 160) 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
message = "Player 1: click to shoot!"                                               #sets the first message youll see, it changes in the main dont worry

board_p1 = ['X'] * 25                                                               #sets the board that player 1 has (everyone has 25 Xs)
board_p1_display = ['X'] * 25                                                       #sets the board the player will see
board_p2 = ['X'] * 25                                                               #sets the board player 2 has
board_p2_display = ['X'] * 25                                                       #sets the board the player will see
                                                                                    #sets variables
shots_left = 10                                                                     #ten shots left
hits_p1 = 0                                                                         #both players havent hit anything yet
hits_p2 = 0
current_player = 1                                                                  #player one goes first
game_over = False                                                                   #game is not over


def place_dots(board):
    """Randomly place 4 dots on the board"""
    dots_placed = 0                                                                 #sets dots placed
    while dots_placed < 4:                                                          #4 times
        spot = random.randint(0, 24)                                                #at a random spot between 0 and 24
        if board[spot] == 'X':                                                      #if the spot hasnt been hit
            board[spot] = 'D'                                                       #change it to a dot
            dots_placed += 1                                                        #add one to the number of dots placed

def draw_board(display_board):
    """Draw the 5x5 grid on screen"""
    for i in range(25):                                                             #25 times
        row = i // 5                                                                #get the row 
        col = i % 5                                                                 #get the collumn
        x = col * CELL_SIZE                                                         #sets where the cells x will be
        y = row * CELL_SIZE + TEXT_HEIGHT                                           #sets where the cells y will be

        if display_board[i] == 'H':                                                 #if the cell has been hit
            color = RED                                                             #set the color to red
            label_text = "Hit"                                                      #label for hit cells
        elif display_board[i] == 'M':                                               #if its been missed
            color = GRAY                                                            #set the color to gray
            label_text = "Miss"                                                     #label for missed cells
        else:                                                                       #if it hasnt been hit or missed
            color = BLUE                                                            #set it to blue
            label_text = None                                                       #no label on un-shot cells

        pygame.draw.rect(screen, color, (x, y, CELL_SIZE, CELL_SIZE))               #fill the cell with the color
        pygame.draw.rect(screen, BLACK, (x, y, CELL_SIZE, CELL_SIZE), 2)            #draw's border

        if label_text is not None:                                                  #if the cell should be labeled
            label = small_font.render(label_text, True, WHITE)                      #render the label
            label_x = x + CELL_SIZE//2 - label.get_width()//2                       #center horizontally in the cell
            label_y = y + CELL_SIZE//2 - label.get_height()//2                      #center vertically in the cell
            screen.blit(label, (label_x, label_y))                                  #draw it


def draw_text(text):
    """Draw message at the top of the screen"""
    pygame.draw.rect(screen, BLACK, (0, 0, WIDTH, TEXT_HEIGHT))                     #clear top bar
    label = font.render(text, True, WHITE)                                          #render the message
    screen.blit(label, (10, 25))                                                    #draw it near the top-left


def get_index_from_click(mouse_x, mouse_y):
    """Convert mouse click to board index"""
    if mouse_y < TEXT_HEIGHT:                                                       #clicked in the text bar, not the board
            return None
    col = mouse_x // CELL_SIZE                                                      #where the click on the x axis was (in px) /the size of a cell(in px) will give a col
    row = (mouse_y - TEXT_HEIGHT) // CELL_SIZE                                      #where the click on the y axis was (in px) /the size of a cell(in px) will give a row
    if row < 5 and col < 5:                                                         #make sure click is on the board
        return row * 5 + col                                                        #return the row and collumn in a way it can be broken down
    return None                                                                     #if you clicked outside the board return none


def main():
    global hits_p1, hits_p2, shots_left, current_player, game_over, message
    transition = False                                                              #true while showing the "pass the device" screen
    place_dots(board_p1)                                                            #sets the dots for each player
    place_dots(board_p2)


    running = True                                                                  #while the game is running
    while running:

        screen.fill(BLACK)                                                          #make the background black
        if transition:                                                                  #between-turn screen
            label1 = font.render(f"Pass to Player {current_player}", True, WHITE)
            label2 = font.render("Click anywhere to continue", True, WHITE)
            screen.blit(label1, (WIDTH//2 - label1.get_width()//2, HEIGHT//2 - 30))     #centered horizontally
            screen.blit(label2, (WIDTH//2 - label2.get_width()//2, HEIGHT//2 + 10))
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:                                #any click dismisses the screen
                    transition = False
            continue                                                                    #skip the normal turn logic this frame
        #draw the correct display board depending on who is shooting
        if current_player == 1:                                                     #if player one is shooting
            draw_board(board_p2_display)                                            #p1 shoots at p2's board
        else:                                                                       #if not player then its player 2
            draw_board(board_p1_display)                                            #p2 shoots at p1's board

        draw_text(message)                                                          #instructions
        pygame.display.flip()                                                       #update the screen

        for event in pygame.event.get():                                            #if the user clicked anywhere      

            if event.type == pygame.QUIT:                                           #if they hit the X button to close the window
                running = False                                                     #end the running of the game

            if event.type == pygame.MOUSEBUTTONDOWN and not game_over:              #if they clicked and the game isnt over
                index = get_index_from_click(*event.pos)                            #get the position of the click 

                if index is None:                                                   #if they didnt click on the board
                    message = "Click on the board!"                                 #set the message to tell the player to click on the board
                    continue                                                       

                # pick the right boards
                if current_player == 1:                                             #if its player ones turn
                    my_board = board_p2                                             #they interact with player 2's boards
                    my_display = board_p2_display
                else:                                                               #if not player one (then player 2)
                    my_board   = board_p1                                           #they interact with player 1s boards
                    my_display = board_p1_display

                # check already shot
                if my_display[index] == 'H' or my_display[index] == 'M':            #check if the player is trying to shoot at a place they already shot at
                    message = "Already shot there!"                                 #change the message to tell the user they already shot there
                    continue

                if my_board[index] == 'D':                                          #if the user hit
                    my_board[index]   = 'H'                                         #change the space on the boards to a hit
                    my_display[index] = 'H'
                    message = f"Player {current_player} hit one!"                   #change the message to announce that the player hit a dot
                    if current_player == 1:                                         #if its player one that hit
                        hits_p1 += 1                                                #add one to their hits
                    else:                                                           #if not player one (player 2)
                        hits_p2 += 1                                                #add one to their hits
                else:                                                               #if not a hit
                    my_display[index] = 'M'                                         #change the spot to miss
                    message = f"Player {current_player} missed!"                    #announce it

                # check win
                if hits_p1 == 4:                                                    #if player 1 has hit 4 dots
                    message = "Player 1 wins!"                                      #give the message that they won
                    game_over = True                                                #end the game
                    continue
                if hits_p2 == 4:                                                    #if player 2 hit 4
                    message = "Player 2 wins!"                                      #give the message that they won
                    game_over = True                                                #end the game
                    continue

                # switch player
                shots_left -= 1                                                     #remove one from the shots left
                if shots_left == 0:                                                 #if there are no shots left and no one has won
                    message = f"Out of shots! P1: {hits_p1}/4  P2: {hits_p2}/4"     #announce the final score   
                    game_over = True                                                #end the game
                    continue

                current_player = 2 if current_player == 1 else 1                    #switch the current player   
                message = f"Player {current_player} - click to shoot! ({shots_left} shots left)" #update the message to tell the next player to shoot and how many shots are left
                transition = True                                                   #show pass-the-device screen before next turn      

    pygame.quit()

if __name__ == "__main__":
    main()