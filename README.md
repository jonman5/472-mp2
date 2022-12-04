# 472-mp2
Mini Project 2 for COMP 472

Link to repo: https://github.com/jonman5/472-mp2

#Rush Hour Game Solver
Rush Hour is a tiny sliding board game played on a board of 6x6 squares. 
The goal of the game is to get the red car out of a six-by-six grid full of automobiles by moving the other vehicles out of its way. However, the cars and trucks obstruct the path and they can only go forward or backward, which makes the puzzle harder.

###Note: This application has been developed and tested on Python 3.11

#Usage
Add a game board file (.txt) to the directory datatxt (format explained below)

##Special Instructions: 
Execute *pip install windows-curses* before running
More info on Pyhton curses: https://docs.python.org/3/howto/curses.html
For PyCharm users in the run configuration file have the option Emulate terminal in output console cheked

##Run the program:

$ python3 rush_hour_solver.py
Follow the instructions on the screen.

##File Format:
The file needs to be saved as text file with the extension .txt in the folder datatxt 
One gameboard per line (starting from first character of line) with optional fuel levels on same line as gameboard but after gameboard.
Each fuel level associated to a vehicle must be separated by a space character.

B through J represent the cars.
AA is the ambulance car that needs to be freed.


Example File Content:

....GG..BBCC....EFAAHHEF...IEF...IJJ 
