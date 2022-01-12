
import random
import re

class Board:
    
    def __init__(self, dim_size, num_bombs):

        # let's keep track of these parameters
        self.dim_size = dim_size
        self.num_bombs = num_bombs 

        # let's create the board
        # helper funtion!
        self.board = self.make_new_board()  # plant the bombs
        self.asign_values_to_board()

        # initialize a set to keep track of which locations we've uncovered
        # we'll save (row, col) tuples into this set
        self.dug = set()    # if we dig at 0, 0, then self.dug = {(0,0)}

    def assign_values_to_board(self):
        
        for r in range(self.dim_size):
            for c in range(self.dim_size):
                if self.board[r][c] == '*':
                    # if this is already a bomb skip
                    continue    
                self.board[r][c] = self.get_num_neighboring_bomb(r, c)
     
    def get_num_neighboring_bomb(self, row, col):


        num_neighboring_bombs = 0
        for r in range(max(0, row - 1), min(self.dim_size - 1, (row + 1)) + 1):
            for c in range(max(0, col - 1), min(self.dim_size - 1, (col + 1)) + 1):
                if r == row and c == col:
                    # our original location, don't check
                    continue
                if self.board[r][c] == '*':
                    num_neighboring_bombs += 1

        return num_neighboring_bombs
    
    def dug(self, row, col):
        # dig at that location
        # return true if successful dig, False if bomb dug

        self.dug.add((row, col))

        if self.board[row][col] == '*':
            return False
        elif self.board[row][col] > 0:
            return True
        
        # self.board[row][col] == 0
        for r in range(max(0, row + 1), min(self.dim_size-1, row + 1)+ 1):
            for c in range(max(0, col +1), min(self.dim_size-1, col +1) +1):
                if (r, c) in self.dug:
                    continue    # dont dig where you have already dug
                self.dig(r, c)
        
        return True

    def __str__(self):
        # this is a function where if you call print on this object,
        # it will print out what this functions return

        visible_board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]
        for row in range(self.dim_size):
            for col in range(self.dim_size):
                if (row, col) in self.dug:
                    visible_board[row][col] = str(self.board[row][col])
                else:
                    visible_board[row][col] = ' '  

        # put in a string    

    def make_new_board(self):

        # construct a new board based on the dimention size and number of bombs
        # we should construct the list of lists here
        # but since we have a 2-D board, list of lists is most natural

        # generate a new board 
        board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]
        # this creates an array like this:
        # [[None, None, ...., None],
        #  [None, None, ...., None],
        #  [......                ],
        #  [None, None, ...., None]]   
        # we can see how this represents a board!
        
        # plant the bombs
        bombs_planted = 0
        while bombs_planted < self.num_bombs:
            loc = random.randint(0, self.dim_size**2 - 1)
            row = loc // self.dim_size
            col = loc % self.dim_size
            
            if board[row][col] == '*':
                # this means we have planted a bomb there
                continue

            board[row][col] = '*'   # plant the bomb
            bombs_planted += 1
        
        return board


# play the game 
def play(dim_size=10, num_bombs=10):
    # Step 1: create the board and plant the bombs
    board = Board(dim_size, num_bombs)

    # Step 2: show the user the board and ask for where they want to dig
    # Step 3: if location is a bomb, show game over message
    #           next to a bomb
    # Step 4: repeat step 2 and 3a/b until there are no more place to dig 
    while len(board.dug) < board.dim_size ** 2 - num_bombs:
        print(board)
        user_input = re.split(',(//s)*', input("Where would you like to dig? Input row, col: "))
        row, col = int(user_input[0]), int(user_input[-1])
        if row < 0 or row >= board.dim_size or col < 0 or col >= dim_size:
            print("Invalid location. Try again.")
            continue

        # if its valid, we dig
        safe = board.dig(row, col)
        if not safe:
            # dug a bomb ahhhhhh
            break

    if safe:
        print("CONGRATULATIONS")    
    else:
        print("SORRY GAME OVER")

        board.dug = [(r, c) for r in range(board.dim_size) for c in range(board.dim_size)]
        print(board)

if __name__ == '__main__':
    play()