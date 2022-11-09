# 472-mp2
Mini Project 2 for COMP 472

Rush Hour Game Solver
Rush Hour is a tiny sliding board game played on a board of 6x6 squares. 
The goal of the game is to get the red car out of a six-by-six grid full of automobiles by moving the other vehicles out of its way. However, the cars and trucks obstruct the path and they can only go forward or backward, which makes the puzzle harder.

Note: This application has been developed and tested on Python 3

Usage
Add a game board file (.txt) to the directory datatxt.

Special Instruction: 
pip install windows-curses
For PyCharm users in the run configuration file have the option Emulate terminal in output console cheked

Run the program:

$ python3 rush_hour_solver.py
Follow the instructions on the screen.

File Format - Game Board
B through J represent the cars.
AA is the ambulance car that needs to be freed.
The file needs to be saved as text file with the extension .txt
File Content:

....AA
..BBCC
rr..EF
GGHHEF
...IEF
...IJJ 
