# Implements a 1-D Array Using the ctypes Module
import ctypes

class Array:
    # Creates the Array with the given size of the Array
    def __init__(self, size):
        assert size > 0, 'Array Must be greater than 0'
        self.size = size

        ArrayTypes = ctypes.py_object * size
        self.slots = ArrayTypes()

        self.clear(None)

    # Returns the size of the Array
    def __len__(self):
        return self.size

    # Returns the item in the given index
    def __getitem__(self, index):
        assert index >= 0 and index < len(self.slots), "Index out of range"
        return self.slots[index]

    # Sets a value to the index
    def __setitem__(self, index, value):
        assert index >= 0 and index < len(self.slots), "Index out of range"
        self.slots[index] = value

    # Sets the Value to the Array
    def clear(self, value):
        for i in range(self.size):
            self.slots[i] = value

    def __str__(self):
        result = ""
        for i in range(len(self)):
            result += str(self.slots[i]) + " "
        return result

    # Returns Iteratable list
    def __iter__(self):
        return Arrayiterator(self.slots)



class Arrayiterator:


    # Creates the iteratable List
    def __init__(self, thelist):
        self.list = thelist
        self.idx = 0

    # Returns Iteratable Array
    def __iter__(self):
        return self.list

    # Returns next occuring Value
    def __next__(self):
        if self.idx  < len(self.list):
           let = self.list[self.idx ]
           self.idx  += 1
           return let
        else:
            raise StopIteration

class Array2D:
    # Creates the Size of the Array by number of Column and Rows
    def __init__(self, numRow, numCol):
        
        self.numRow = Array(numRow)

        for i in range(numRow):
            self.numRow[i] = Array(numCol)
    # Returns the number of Rows in the Array
    def numRows(self):
        return len(self.numRow)

    # Returns the number of Column in the Array
    def numCols(self):
        return len(self.numRow[0])

    # Clears and sets the value to a given value
    def clear(self, value):
        for row in range(self.numRows()):
            self.numRow[row].clear(value)
 
    # Returns the item in the given index
    def __getitem__(self, ndx):
        assert len(ndx) == 2, "Invalid number of array"
        row = ndx[0]
        col = ndx[1]
        assert row >= 0 and row < self.numRows()\
           and col >= 0 and col < self.numCols(),\
               "Array out of range"
        therow = self.numRow[row]
        return therow[col]

    # Sets the item in the given index to the value
    def __setitem__(self, ndx, value):
        assert len(ndx) == 2, "Invalid number of array"
        row = ndx[0]
        col = ndx[1]
        assert row >= 0 and row < self.numRows()\
           and col >= 0 and col < self.numCols(),\
               "Array out of range"
        therow = self.numRow[row]
        therow[col] = value

    def __str__(self):
        result = ""
        for i in range(self.numRows()):
            if i < self.numRows()-1:
                result += str(self.numRow[i]) + "\n"
            else:
                result += str(self.numRow[i])

        return result
            
