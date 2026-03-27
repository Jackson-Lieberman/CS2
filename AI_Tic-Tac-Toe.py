"""
Ai Tic tac toe
Student Name: Jackson Lieberman
Date: 4/1/26
Discription: 
Play tic tac toe against either an ai bot or a human!
How to run:
Download the ollama software onto your machine
In terminal:
    pip install openai
    ollama run qwen2.5-coder
Run the code
Bugs: 
Log: 1.2
"""
import random                       
from openai import OpenAI

client = OpenAI(                                                                    #sets the model
base_url="http://localhost:11434/v1/",
api_key="ollama"
)

def get_player_move(board, player):
    """Ask the player for a valid row and column."""
    while True:                                                                     #infite loop
        try:                                                                        
            print(f"Player {player}'s turn.")                                       
            row = int(input("Enter row (1-3): "))-1                                 #asks for a row
            col = int(input("Enter collumn (1-3): "))-1                             #asks for a collumn
            if 0 <= row <= 2 and 0 <= col <= 2:                                     #makes sure the space is in range
                if board[row][col]== " ":                                           #if the space is empty
                    board[row][col] = player                                        #check the space to the players character
                    break
                else:
                    print("That spot is already taken, try again.")                 #if taken tell the user
            else:
                print("Invalid input, please enter numbers between 1 and 3.")       #if out of range tell user
        except ValueError:                                                          #if not intergers tell the user
            print("Invalid input, please enter numeric values.")

def bot_move(board, bot_char):
    print("Bot is thinking...")                                                     #tells user that the ai model is generating a response 
    prompt = f'''Tic tac toe board: {board}.                                        
    You are {bot_char}. 
    Return ONLY the best move as 'row,col' (1-3). 
    Please ONLY give the numbers seperated by a comma. Example respsonse: 1,2'''    #prompt for the ai               
    response = client.chat.completions.create(                                      #asks the model the prompt
        model="qwen2.5-coder",
        messages=[{"role": "user", "content": prompt}]
    )
    move_str = response.choices[0].message.content.strip()                          #strips the the AI response
    try:                                                                            #tries split the response into a row and collumn
        row, col = map(int, move_str.replace(" ", "").split(','))
        if board[row-1][col-1] == " ":                                              #checks the models move is in an empty space so it can do
            board[row-1][col-1] = bot_char
        else:
            raise ValueError                                                        #if it cant then raise an error
    except:                                                                         #if he move cant be exicuted
        print(move_str)                 #FIXING
        for r in range(3):                                                          #do the first possible move
            for c in range(3):
                if board[r][c] == " ":
                    board[r][c] = bot_char
                    return 

def is_draw(board): 
    """Return True if the board is full and there is no winner."""
    for row in board:                                                               #checks if there is any empty spaces
        if " " in row:
            return False                                                            #if there arent empty spaces return false
    return True                                                                     #if there are empty spaces return true


def check_winner(board):
    """Return 'X', 'O', or None."""
    for i in range(3):                                                                             #3 times
        if board[i][0] == board[i][1] == board[i][2] != " ": 
            return board[i][0]                                                                     #check each row
        elif board[0][i] == board[1][i] == board[2][i] != " ": 
            return board[0][i]                                                                     #check each collumn
        elif board[0][0] == board[1][1] == board[2][2] != " ": 
            return board[0][0]                                                                     #check both diagonals
        elif board[0][2] == board[1][1] == board[2][0] != " ": 
            return board[0][2]
    
    return None

def display_board(board):
    """
    Prints the Tic-Tac-Toe board in a grid format.
    """
    print("-------")                                                                #starting -------                                  
    for i, row in enumerate(board):                                                 #3 times
        display_row = [cell if cell else ' ' for cell in row]                       #put each cell in a list
        print(f"|{'|'.join(display_row)}|")                                         #join the list with | in between
        print("-------")                                                            #ending --------
    print()


def first_player():
    '''
    Gets the first player of the game
    '''

    print('''
To choose the first player one of you will play a game of unscramble the word. 
          ''')
    print("Win to be 'X', lose to be 'O'.")

    words = ['flamingo', 'watermelon', 'flight', 'wind', 'xylophone', "anaconda", "black", "yellow", "rainbow"]   #makes a list of words
    
    word = random.choice(words)                                                                               #chose a random word from the list
    letters = list(word)                                                                                      #makes a list from the letters in the word
    random.shuffle(letters)                                                                                   #shuffles the letters 
    display = ''.join(letters)                                                                                #combines the letters into a string
    turns = 3                                                                                                 #sets turns to 5
    print("You have 3 turns to guess the word")                                                               #tell the user they have 5 turns

    while turns > 0:                                                                                          #repeat while you have more turns than 0
        guess= input("Unscramble " + display + " ").lower()                                           #tells the user to unscramble the scrambled word

        if guess == word:                                                                                     #if the guess is correct
            print("You got it!")                                                                              #tell the user they were correct
            print('You are X.')
            return "X"
        turns -= 1                                                                  #remove one of the turns
        if turns > 0:                                                               #if the game is still going
            print(f"Wrong! {turns} turns left.")                                    #tell the user how many turns they have left
            res = input("Rescramble? (y/n): ").lower()                           #ask if the user wants to rescramble
            if res == "y":                                                        #random shuffle if yes
                random.shuffle(letters)
                display = ''.join(letters)
            elif res == "n":                                                       #if not do nothing
                continue
            else:                                                                   #if input isnt valid                                              #if their yes or no was said
                print("invalid input!")                                             #tell them it was invalid
    print(f"Out of turns! The word was {word}. You are O.")
    return "O"




def play_game():
    """Run one complete game of Tic-Tac-Toe."""
    board = [                                                                       #sets the inital board
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]    

    
    while True:                                                                             #checks if the input from the user was valid
        mode = input("Would you like to play against a bot or a human? (answer b/h)").lower()   #asks if the user wants to play another player or a bot

        if mode in ['b', 'h']:
            break                                                                           #if it was, continue
        print("Invalid input! Please type 'b' for bot or 'h' for human.")                   #if not then ask the question again
    current_player = first_player()                                                         #sets the first player
    game_over = False                                                                       #sets the game to not over
    bot_char = "O" if current_player == "X" else "X"                                        #makes the bot what every character the play is not
    current_player = "X"                                                                    # X always starts

    while not game_over:                                                                    #while the game isnt over
        
        display_board(board)                                                                #show the board using the function
        
        if mode == 'b' and current_player == bot_char:                                      #if the player wants to play the bot 
            bot_move(board, bot_char)                                                       #gets the ai move
        else:                                                                               #if the player doesnt wanna play the bot
            get_player_move(board, current_player)                                          #ask the player for their move
        winner = check_winner(board)                                                        #check for a winner
        if winner:                                                                          #if someone won
            display_board(board)                                                            #show the board
            print(f"Player {winner} wins!")                                                 #print the winner
            game_over = True                                                                #make the game over
        elif is_draw(board):                                                                #if theres a draw say it
            display_board(board)
            print("It's a draw!")
            game_over = True                                                                #make the game over
        else:
            current_player = "O" if current_player == "X" else "X"                          #switch players


if __name__ == "__main__":
    while True:
        play_game()
        cont = input('Continue? (y/n)')
        if cont == 'y':
            continue
        elif cont == 'n':
            break
    





