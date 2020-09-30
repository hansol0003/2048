"""
Project: "2048 in Python!"
Developed by: Kunal Mishra and Paradigm Shift
Autograder support, video introductions added by: Jesse Luo and Michael Tu
Developed for: Beginning students in Computer Science
To run: python3 starter_2048.py
Student Learning Outcomes:
    Various levels of comfort with:
        large projects and abstraction
        understanding, modeling, and maintaining existing code
        variables
        functional programming
        loops and conditionals
        multidimensional arrays/lists
        randomness and distributions
        CLI programming and terminal GUIs
Skill Level:
    assumed knowledge of language and concepts, but without mastery or even comfortability with them
    ~8-15 hours of lecture/lab/homework for a beginner at CS0 level coming into this project
    ~Calibrated at somewhat below the difficulty level of UC Berkeley's 61A project, Hog (less code synthesis but more interpretation required, given the students' backgrounds)
Abstraction Reference Guide:
    main                - responsible for starting the game and directing control to each function, the tests, or quitting
        board           - a variable within main that contains the current board and is passed to most functions as an argument
    System Functions:
        get_key_press   - returns the user's key_press input as an ascii value
        clear           - clears the screen (should be called before each print_board call)
        pause           - a function used by the GUI to allow for a slight delay that is more visually appealing in placing the new piece
    Board Functions:
        make_board      - creates a new, empty square board of N x N dimension
        print_board     - prints out the state of the argument board
        board_full      - returns True if the board is full and False otherwise
    Logic:
        swipe_right     - simulates a right swipe on the argument board
        swipe_left      - simulates a left swipe on the argument board
        swipe_up        - simulates a upward swipe on the argument board
        swipe_down      - simulates a downward swipe on the argument board
        swap            - occurs when the spacebar is pressed and randomly switches two different numbers on the board
        swap_possible   - a helper function that returns True if a swap is possible and False otherwise
    Useful Helper Functions:
        get_piece       - gets the piece from the given board at the given (x,y) coordinates or returns None if the position is invalid
        place_piece     - places the given piece on the given board at the given (x,y) coordinates and returns True or returns False if the position is invalid
        place_random    - user implemented function which places a random 2 OR 4 OR 8 in an empty part of the board
        have_lost       - responsible for determining if the game has been lost yet (no moves remain)
        move_possible   - responsible for determining if a move is possible from a single position
        move            - responsible for moving a piece, at the given (x,y) coordinates in the given direction on the given board

        Please run in Terminal.  Running in any other IDE will result in various errors.
"""


# End of first section
############################################################################################################
################################## DO NOT CHANGE ANYTHING ABOVE THIS LINE ##################################    - Section 2 -
############################################################################################################


# Start of Step 0 ###########################################################################################

def main():
    # Creating my new 4x4 board
    board = make_board(4)

    # Getting the game started with a single piece on the board
    place_random(board)
    print_board(board)

    #i = 0
    # Runs the game loop until the user quits or the game is lost
    while True:

        # Gets the key pressed and stores it in the key variable
        key = get_key_press()

        # Quit case ('q')
        if key == 113:
            print("Game Finished!");
            quit()

        # Up arrow
        elif key == 65:
            my_swipe_up(board)

        # Down arrow
        elif key == 66:
            my_swipe_down(board)

        # Right arrow
        elif key == 67:
            my_swipe_right(board)

        # Left arrow
        elif key == 68:
            my_swipe_left(board)

        # Space bar
        elif key == 32:
            swap(board);
        
        """i = i + 1
        print(i)"""
        # Check to see if I've lost at the end of the game or not
        if have_lost(board):

            print("You lost! Would you like to play again? (y/n)");
            if (input() == 'y'):
                main()
            else:
                quit()


# End of Step 0 #############################################################################################


# Start of Step 1 ###########################################################################################

def get_piece(x, y, board):
    """
    Utility function that gets the piece at a given (x,y) coordinate on the given board
    Returns the piece if the request was valid and None if the request was not valid
    Arg x: integer - x coordinate
    Arg y: integer - y coordinate
    Arg board: board - the board you wish to get the piece from
    """

    # Ensure that x and y are both integers (use assert)
    assert type(x) == type(y) == int

    # What does this do?
    N = len(board)

    # Checking that the (x,y) coordinates given are valid for the N x N board
    if x >= N or y >= N or x < 0 or y < 0:
        return None

    # Getting the piece on the board
    return board[y][x]


def place_piece(piece, x, y, board):
    """
    Utility function that places the piece at a given (x,y) coordinate on the given board if possible
    Will overwrite the current value at (x,y), no matter what that piece is
    Returns True if the piece is placed successfully and False otherwise
    Arg piece: string - represents a piece on the board ('*' is an empty piece, '2' '8' etc. represent filled spots)
    Arg x: integer - x coordinate
    Arg y: integer - y coordinate
    Arg board: board - the board you wish to place the piece on
    """

    # Ensure that x and y are both integers (use assert)
    assert type(x) == type(y) == int

    # What are the dimensions of the board?
    N = len(board)

    # Checking that the (x,y) coordinates given are valid for the board
    if x >= N or y >= N or x < 0 or y < 0:
        return None

    # Placing the piece on the board
    board[y][x] = piece
    return True


# End of Step 1 #############################################################################################


# Start of Step 2 ###########################################################################################

def place_random(board):
    """
    Helper function which is necessary for the game to continue playing
    Returns True if a piece is placed and False if the board is full
    Places a 2 (60%) or 4 (37%) or 8 (3%) randomly on the board in an empty space
    Arg board: board - the board you wish to place the piece on
    """

    # Check if the board is full and return False if it is
    if board_full(board):
        return False

    # random.random() generates a random decimal between [0, 1) ... Multiplying by 100 generates a number between [0, 100)
    generated = random.random() * 100;

    # Assign to_place according to my generated random number

    if generated < 70:  # YOUR CODE HERE (replace -1) <<<<<
        to_place = "2"

    elif generated < 99 and generated >= 70:  # YOUR CODE HERE (replace -1) <<<<<
        to_place = "4"

    else:
        # What should to_place be if it's not a 2 or 4?
        to_place = "8"

    # Variable keeps track of whether a randomly generated empty spot has been found yet
    found = False
    N = len(board)

    while not found:
        # Generate a random (x,y) coordinate that we can try to put our new value in at
        # How did we "generate" a random number earlier? (hint: x and y should be between [0, N) )
        random_y = random.random() * N
        random_x = random.random() * N

        # Think about why this is necessary ( hint: changes 3.4 (float) -> 3 (int) )
        random_y = int(random_y)
        random_x = int(random_x)

        # If the randomly generated coordinates are empty, we have found a spot to place our random piece
        found = get_piece(random_x, random_y, board) == '*'

    # Place the piece at the randomly generated (x,y) coordinate
    place_piece(to_place, random_x, random_y, board)

    return True


# End of Step 2 #############################################################################################


# Start of Step 3 ###########################################################################################

def have_lost(board):
    """
    Helper function which checks at the end of each turn if the game has been lost
    Returns True if the board is full and no possible turns exist and False otherwise
    Arg board: board - the board you wish to check for a losing state
    """

    N = len(board)

    # Check every (x,y) position on the board to see if a move is possible
    for y in range(N):
        for x in range(N):
            if move_possible(x, y, board):
                return False

    return True


# End of Step 3 #############################################################################################


# Start of Step 4 ###########################################################################################

def end_move(board):
    """
    Prints the board after a swipe, pauses for .2 seconds, places a new random piece and prints the new state of the board
    Arg board: board - the board you're finishing a move on
    """

    # Print the board
    clear();
    print_board(board);

    # Pause for .2 seconds
    pause(.2);

    # Place a random piece on the board at a random (x,y) position
    place_random(board)

    # Print the board again
    clear;
    print_board(board);


# End of Step 4 #############################################################################################


# Start of Step 5 ###########################################################################################
def my_swipe_left(board):

 
    N = 4
    a = ['*', '*', '*', '*']

    for y in range(N):
        for x in range(N):
            a[x] = get_piece(x, y, board)
            #print(a[x])
        collapse(a)
        #print(b[0], b[1], b[2], b[3])
        for x in range(N):
            #print(b[x])
            place_piece(a[x], x, y, board)
            
            
    end_move(board)


def my_swipe_right(board):

    N = 4
    a = ['*', '*', '*', '*']

    for y in range(N):
        for x in range(N):
            a[3 - x] = get_piece(x, y, board)
            #print(a[3 - x])
        collapse(a)
        #print(b[0], b[1], b[2], b[3])
        for x in range(N):
            place_piece(a[3 - x], x, y, board)
            
        
    end_move(board)


def my_swipe_up(board):

    N = 4
    a = ['*', '*', '*', '*']
    
    for x in range(N):
        for y in range(N):
            a[y] = get_piece(x, y, board)
            #print(a[y])
        collapse(a)
        #print(b[0], b[1], b[2], b[3])
        for y in range(N):
            place_piece(a[y], x, y, board)
            
            
    end_move(board)


def my_swipe_down(board):

    N = 4
    a = ['*', '*', '*', '*']

    for x in range(N):
        for y in range(N):
            a[3 - y] = get_piece(x, y, board)
            #print(a[3 - y])
        collapse(a)
        #print(b[0], b[1], b[2], b[3])
        for y in range (N):
            #print(b[3 - y])
            place_piece(a[3 - y], x, y, board)
    
    
    end_move(board)



# End of Step 5 #############################################################################################


# End of second section
############################################################################################################
######################## Optional Challenge -- ATTEMPT AFTER FINISHING PROJECT #############################    - Section 3 -
############################################################################################################

def swap(board):
    """
    Optional Challenge: an addition to our game that adds some randomness and chance!
    Randomly swaps 2 different numbers on the board and returns True if a swap is performed and False otherwise
    Purpose: allows you to evade losing for a little while longer (if the swap is useful)

    Note: have_lost does not take into account possible swaps that can "save the day". This is expected behavior.
    """

    print("Not implemented yet!")
    return False


def swap_possible(board):
    """
    Optional Challenge: helper function for swap
    Returns True if a swap is possible on the given board and False otherwise
    """

    print("Not implemented yet!")
    return False

def collapse(a):
 #print(a[0], a[1], a[2], a[3])
    i = 0
    while a[0] == '*' and i < 4:
        a[0] = a[1]
        a[1] = a[2]
        a[2] = a[3]
        a[3] = '*'
        i = i + 1
    if i == 4:
        return

    i = 0
    while a[1] == '*' and i < 3:
        a[1] = a[2]
        a[2] = a[3]
        a[3] = '*'
        i = i + 1
    if i == 3:
        return

    if a[0] == a[1]:
        #print(a[0], a[1])
        a[0] = str(int(a[0]) + int(a[1]))
        #print(a[0])
        a[1] = a[2]
        a[2] = a[3]
        a[3] = '*'
    
    i = 0
    while a[1] == '*' and i < 3:
        a[1] = a[2]
        a[2] = a[3]
        a[3] = '*'
        i = i + 1
    if i == 3:
        return

    i = 0
    while a[2] == '*' and i < 2:
        a[2] = a[3]
        a[3] = '*'
        i = i + 1
    if i == 2:
        return
 
    if a[1] == a[2]:
        #print(a[1], a[2])
        a[1] = str(int(a[1]) + int(a[2]))
        #print(a[1])
        a[2] = a[3]
        a[3] = '*'
    
    i = 0
    while a[2] == '*' and i < 2:
        a[2] = a[3]
        a[3] = '*'
        i = i + 1
    if i == 2:
        return
    
    if a[2] == a[3]:
        a[2] = str(int(a[2]) + int(a[3]))
        a[3] = '*'

 


 #print(a[0], a[1], a[2], a[3])
 

  
  
      
  

# End of third section
############################################################################################################
################################## DO NOT CHANGE ANYTHING BELOW THIS LINE ##################################   - Section 4 -
############################################################################################################


try:
    from utils import *
except ImportError:
    from _2048.utils import *

if __name__ == "__main__":
    # Only want to see the game board at the top
    clear()

    # Starting the game
    main()

# End of fourth section
# End of starter_2048.py
