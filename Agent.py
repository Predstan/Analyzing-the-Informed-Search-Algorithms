from Board import Board
import heapq
import datetime
import math

""" class for lIST of Open Node """
class Frontier:
    # Create an instance of the List
    def __init__(self):
        self.thisQueue = []

    # Push the Node into the List sorted by increasing value of the f(n) value
    def push(self, thisNode):
        heapq.heappush(self.thisQueue, (thisNode.fValue, -thisNode.id, thisNode))

    # return the Node in the list with the minimum f(n) value
    def pop(self):
        return heapq.heappop(self.thisQueue)[2]

    # Determine if the Frontier is Empty
    def isEmpty(self):
        return len(self.thisQueue) == 0

    # Returns the length of the Frontier
    def length(self):
        return len(self.thisQueue)

""" Class of the Node """
nodeid = 0
class Node:
    # Initialize the Attritubes of a node
    def __init__(self):
        global nodeid
        self.id = nodeid        # the id of the node
        nodeid += 1
        self.parent = None      # The parent of the Node
        self.action = None      # Action performed to reach this state
        self.state = None       # The state after the action on the parent
        self.gValue = None      # The path Cost g(n) of each state
        self.fValue = None      # The f(n) value where f(n) = heuristic value, h(n) + g(n)
        
"""
Create a class of the Closed List
Use Set to eliminate duplicates
"""
class CheckList():
    
    def __init__(self):
        self.thisList = set()   

    # Add an entry state to the closed list
    def add(self, entry):
        if entry is not None:
            self.thisList.add(entry.__str__())

    # Return the length of the the list
    def length(self):
        return len(self.thisList)
    
    # determine if an entry exist in the the list
    def __contains__(self, entry):
        return entry.__str__() in self.thisList

    


""" Artificial Agent for Solving the Puzzle Board 
    The agent returns the number of closed Nodes, Opened Nodes, the depth of the Optimal solution
    and every Nodes that leads to the Optimal Solution"""
def A_Star(heuristics, gValue, start_state, goal_state):
    
    frontier = Frontier()                     # Create a queue Frontier to store open Nodes
    closed_list = CheckList()                 # Create a list for the examined and closed Nodes
    newNode = Node()                          # Create a Node for the current Board to be solved         
    newNode.state = start_state               
    newNode.gValue = gValue
    newNode.fValue = hValue(heuristics, start_state, goal_state) + newNode.gValue
    parent = newNode                          # Initialize the Board as the parent Node
    
    """ Iterate Over new State of the Board after each action 
        until the Goal or the Solution to the Board is returned
    """
    while parent.state != goal_state:
        # Generate the new state of the Board after each actions(Up, down, left and right)
        # is performed on current state
        children = parent.state.up(), parent.state.down(), parent.state.left(), parent.state.right()

        # Add the current state to the explored/closed List
        closed_list.add(parent.state)

        # Create a Node for each Child generated from the current state of the Board
        for x in range(len(children)):

            # Determine if the action leads to the same state or the new state has been explored
            if children[x] is not None and children[x] not in closed_list:
                # Create new Node for the child if it has not been explored
                newNode = Node()
                newNode.state = children[x]
                newNode.parent = parent
                newNode.action = x
                newNode.gValue = parent.gValue + gValue
                newNode.fValue = hValue(heuristics, children[x], goal_state) + newNode.gValue
                frontier.push(newNode)                  # Push Node into the Frontier

        parent = frontier.pop()                         # Return Node with the least f(n) value


    # Determine if the parent is found
    if parent.state == goal_state:
        
        state = parent
        depth = 0
        V = closed_list.length()    # Total Number of Closed State
        N = V + frontier.length()   # Total Number of Opened state
        

        stacks = stack()            # Stack to keep state from frist action to the Last
        stacks.add(state.state)
        state = state.parent
        
        while state is not None:    # Iterate and keep state in the stack
            stacks.add(state.state)
            state = state.parent
            depth += 1
            
        b = 0
        if depth != 0:
            b = N ** (1/depth)
        print(f"V={V}")
        print(f"N={N}")
        print(f"d={depth}")
        print(f"b={b}")
        print()

        while not stacks.isEmpty():
            print(stacks.pop())
            print()
        
    return V, N, depth, b, stacks 
   
""" Calculate and Return the heuritics value of a state"""
def hValue(heuristics, state, goal):
    # Return zero when no heuristics is required
    if heuristics == 0:
        return heuristics

    # Calculate and return the heuristics 
    # based on the number of displaced tiles
    elif heuristics == 1:
        h = 0
        i = 0
        j = 0
        while i < goal._board.numRows():
            # Do not include the blanktile as a deisplaced tile
            if (state._board[i, j] != goal._board[i, j])\
                and (state._board[i, j] != 0):
                h += 1
            if j < goal.numRows() - 1:
                j += 1
            else:
                j = 0
                i += 1
        return h

    # Calculate and return the heuristics 
    # based on the manhattan distance between state and Goal
    elif heuristics == 2:
        h = 0
        i = 0
        j = 0
        while i < state._board.numRows():
            # Do not include the blanktile 
            if state._board[i, j] != 0:   
                value = state._board[i, j]
                m = 0
                n = 0
                while m < goal._board.numRows():
                    if goal._board[m, n] == value:
                        h += abs(i - m) + abs(j - n) # Add the distance value of each tiles
                    if n < goal.numRows() - 1:
                        n += 1
                    else:
                        n = 0
                        m += 1
            if j < goal.numRows() - 1:
                j += 1
            else:
                j = 0
                i += 1
        return h

    # Calculate and return the heuristics 
    # based on the Elucidean distance between the state and Goal
    else:
        h = 0
        i = 0
        j = 0
        # Iterate over the state configuration
        while i < state._board.numRows():
            # Do not include the blanktile 
            if state._board[i, j] != 0:   
                value = state._board[i, j] # Get the value at the row, col
                m = 0
                n = 0
                # Iterate over the Goal Board
                while m < goal._board.numRows():
                    if goal._board[m, n] == value: # Get the right row and col in the Goal configuration
                        h += math.sqrt((i - m)**2 + (j - n)**2) # Add the distance value of each tiles
                    if n < goal.numRows() - 1:
                        n += 1
                    else:
                        n = 0
                        m += 1
            if j < goal.numRows() - 1:
                j += 1
            else:
                j = 0
                i += 1
        return h
        




# Class for Stacking using LIFO system
class stack():
    def __init__(self):
        self.elements = None
        self.count = 0
    
    # Stack an item into
    def add(self, value):
        newNode = stackNode(value)
        if self.isEmpty():
            self.elements = newNode
        else:
            newNode.next = self.elements
            self.elements = newNode
        self.count += 1
    
    # Return the last item in the Stack
    def pop(self):
        item = self.elements.data
        self.elements = self.elements.next
        self.count -= 1
        return item

    # Determine if Stack is empty
    def isEmpty(self):
        return self.count == 0

# Node Class for Stack 
class stackNode(stack):
    def __init__(self, data):
        self.data = data
        self.next = None



