
def main():

    board = make_board(4)


    place_random(board)
    print_board(board)


    while True:

        key = get_key_press()


        if key == 113:
            print("Game Finished!");
            quit()


        elif key == 65:
            my_swipe_up(board)


        elif key == 66:
            my_swipe_down(board)


        elif key == 67:
            my_swipe_right(board)

        elif key == 68:
            my_swipe_left(board)


        elif key == 32:
            swap(board);
        
     
        if have_lost(board):

            print("You lost! Would you like to play again? (y/n)");
            if (input() == 'y'):
                main()
            else:
                quit()



def get_piece(x, y, board):



    assert type(x) == type(y) == int


    N = len(board)


    if x >= N or y >= N or x < 0 or y < 0:
        return None


    return board[y][x]


def place_piece(piece, x, y, board):



    assert type(x) == type(y) == int

 
    N = len(board)


    if x >= N or y >= N or x < 0 or y < 0:
        return None


    board[y][x] = piece
    return True



def place_random(board):



    if board_full(board):
        return False


    generated = random.random() * 100;



    if generated < 70:  
        to_place = "2"

    elif generated < 99 and generated >= 70:  
        to_place = "4"

    else:
        
        to_place = "8"

    
    found = False
    N = len(board)

    while not found:

        random_y = random.random() * N
        random_x = random.random() * N


        random_y = int(random_y)
        random_x = int(random_x)

        found = get_piece(random_x, random_y, board) == '*'


    place_piece(to_place, random_x, random_y, board)

    return True



def have_lost(board):


    N = len(board)


    for y in range(N):
        for x in range(N):
            if move_possible(x, y, board):
                return False

    return True



def end_move(board):



    clear();
    print_board(board);


    pause(.2);

    place_random(board)


    clear;
    print_board(board);



def my_swipe_left(board):

 
    N = 4
    a = ['*', '*', '*', '*']

    for y in range(N):
        for x in range(N):
            a[x] = get_piece(x, y, board)

        collapse(a)

        for x in range(N):

            place_piece(a[x], x, y, board)
            
            
    end_move(board)


def my_swipe_right(board):

    N = 4
    a = ['*', '*', '*', '*']

    for y in range(N):
        for x in range(N):
            a[3 - x] = get_piece(x, y, board)

        collapse(a)

        for x in range(N):
            place_piece(a[3 - x], x, y, board)
            
        
    end_move(board)


def my_swipe_up(board):

    N = 4
    a = ['*', '*', '*', '*']
    
    for x in range(N):
        for y in range(N):
            a[y] = get_piece(x, y, board)

        collapse(a)

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




def swap(board):


    print("Not implemented yet!")
    return False


def swap_possible(board):


    print("Not implemented yet!")
    return False

def collapse(a):

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

        a[0] = str(int(a[0]) + int(a[1]))

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

        a[1] = str(int(a[1]) + int(a[2]))

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

 



 

  
  
      
  




try:
    from utils import *
except ImportError:
    from _2048.utils import *

if __name__ == "__main__":

    clear()


    main()


