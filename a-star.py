#!/usr/bin/python3
# -*- coding: utf-8 -*-
from Board import Board
import sys
import datetime
from Agent import A_Star

if (len(sys.argv) != 3):
    print()
    print("Usage: %s [heuristics] [Path Cost]" %(sys.argv[0]))
    print()
    sys.exit(1)

state = Board(3, 3)
goal = state.readGoal(open("input.txt", "r"))
start_state = state.readGoal(sys.stdin)


def a_star(goal, start_state):
    A_Star(int(sys.argv[1]), int(sys.argv[2]), start_state, goal)

a_star(goal, start_state)




