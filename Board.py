"""
    Creating the Board Using ctype 2 dimensional Array
"""

from Array2D import Array2D
import random

class Board():
    blanktile = 0
    # Initialize the The Board row and column
    def __init__(self, numRow, numCol):
        self._board = Array2D(numRow, numCol)
        self._blankLocation = None              # Set Blank Location to None

    # Return the Number of Rows
    def numRows(self):
        return self._board.numRows()

    # Return the number of columns of the board
    def numCols(self):
        return self._board.numRows()

    # Read the Goal from a standard Input
    def readGoal(self, fileName):
            s = self.copy()
             # Open file Location
            file_object = fileName.readlines()   # Read each Lines 
            assert len(file_object) == self.numRows(), \
                "Input Rows less than the initialized"
            i = 0
            j = 0
            while i < len(file_object):       # Iterate over the Lines
                line = file_object[i].split()               
                s._board[i, j] = int(line[j]) # Set each values in the Board
                if int(line[j]) == Board.blanktile:
                    s._blankLocation = (i, j)
                if j < len(file_object) - 1:
                    j += 1
                else:
                    j = 0
                    i += 1         
                    
            return s

    # Return the Board as a String
    def __str__(self):
        return self._board.__str__()

    # Move blanktile up
    def up(self):
        row, col = self._blankLocation
        if row == 0:
            return None
        s = self.copy()    # Create a new copy of the Board
        newrow = row - 1
        s._board[row, col] = s._board[newrow, col]  # Replace blanktile with the new value
        s._board[newrow, col] = Board.blanktile
        s._blankLocation = newrow, col
        return s                                    # Return new configuration of Board

    # Move BlankTile down and return new configuration
    def down(self):
        row, col = self._blankLocation
        if row == self.numRows()-1:
            return None
        s = self.copy()  # create a copy of the Board
        newrow = row + 1
        s._board[row, col] = s._board[newrow, col] # replace blanktile
        s._board[newrow, col] = Board.blanktile
        s._blankLocation = newrow, col
        return s                                   

     # Move BlankTile to left and return new configuration
    def left(self):
        row, col = self._blankLocation
        if col == 0:
            return None
        s = self.copy()
        newcol = col - 1
        s._board[row, col] = s._board[row, newcol] # Replace blanktile
        s._board[row, newcol] = Board.blanktile
        s._blankLocation = row, newcol
        return s

    # Move BlankTile to right and return new configuration
    def right(self):
        row, col = self._blankLocation
        if col == self.numCols()-1:
            return None
        s = self.copy()
        newcol = col + 1
        s._board[row, col] = s._board[row, newcol]  # Replace blanktile
        s._board[row, newcol] = Board.blanktile
        s._blankLocation = row, newcol
        return s
    
    # Shuffle the Board and return the new Configuartion
    def shuffle(self, seed, number_of_moves):
        random.seed(seed)                  
        s = self.copy()                     # Create copy of the current Board
        for _ in range(number_of_moves):
            move = random.randrange(4)
            if move == 0:
                new = s.up()
                if new is not None:
                    s = new
                else:
                    s = s.down()
            elif move == 1:
                new = s.down()
                if new is not None:
                    s = new
                else:
                    s = s.up()
            elif move == 2:
                new = s.left()
                if new is not None:
                    s = new
                else:
                    s = s.right()
            else:
                new = s.right()
                if new is not None:
                    s = new
                else:
                    s = s.left()
        return s

    # Determine if 2 Board configurations are equal
    def __eq__(self, board_B):     
        i = 0
        j = 0
        # Iterate over Board A
        while i < self._board.numRows():
            if board_B._board[i, j] != self._board[i, j]:
                return False
            if j < self.numRows() - 1:
                j += 1
            else:
                j = 0
                i += 1
        return True


    # Return a copy of the current Board
    def copy(self):
        s = Board(self.numRows(), self.numCols())
        i = 0
        j = 0
        while i < self._board.numRows():
            s._board[i, j] = self._board[i, j]
            if s._board[i, j] == 0:
                s._blankLocation = (i, j)
            if j < self.numRows() - 1:
                j += 1
            else:
                j = 0
                i += 1
        return s













                


