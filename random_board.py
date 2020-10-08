#!/usr/bin/python3
# -*- coding: utf-8 -*-
from Board import Board
import sys
import os

if (len(sys.argv) != 3):
    print()
    print("Usage: %s [seed] [number of random moves]" %(sys.argv[0]))
    print()
    sys.exit(1)
    

def main():
    seed = int(sys.argv[1])
    number_of_moves = int(sys.argv[2])
    goal = Board(3, 3).readGoal(sys.stdin)
    new = goal.shuffle(seed, number_of_moves)
    print(new)
    
    return goal, new
        

main()
