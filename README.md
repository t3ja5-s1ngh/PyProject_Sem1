# Othello
    A Python Othello game with complete rule handling, board management, and a functional UI. Players can save and load their progress using a built-in file manager.
    
## Features
    8x8 board display  
    Valid move detection
    Auto flip and player turns
    Save and load saved games
    Input through mouse 
    A clean and minimalistic GUI 

## Directory structure
    The entire project consists of mainly 5 files:
### GUI.py: This handles the GUI and the user inputs
### board.py: This sets the board and the tokens for the start of the game
### game_logic.py: This contains the core game logic functions which are called main
### main.py: This is the file where all other files interact.
### file_manager.py: This file saves game and also loads a saved game

## Game instructions
    1) 8×8 board; game starts with 4 discs in the center (2 black, 2 white).
    2) Black moves first; players alternate turns.
    3) A move is valid only if it flips at least one opponent disc.
    4) Flips occur when your disc and an existing disc of your color trap opponent discs in a straight line (horizontal/vertical/diagonal).
    5) All trapped discs are flipped to your color immediately.
    6) If a player has no valid moves, they must pass.
    7) Game ends when both players cannot move.
    8) Winner = player with more discs on the board.
    9) Ties are allowed.

## Setup instructions
    1) Clone the repository
        git clone https://github.com/t3ja5-s1ngh/PyProject_Sem1.git 
        cd PyProject_Sem1
    2) Install python if not already installed (python 3.8+ required)
    3) Install tkinter if not already installed
    4) Run the game 
        python3 main.py
    5) To load a saved game use the load option
    6) To save the game use the save option present below

## Credits
    BE2025001 Aditya - Game logic dev2
    BE2025007 Bharat - Save file manager
    IE2025014 Parth - Game logic dev1
    IE2025015 Kavyansh Agarwal - Board logic
    IE2025033 Tejas Singh - GUI and main.py
