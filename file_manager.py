def save_game(board, current_player, filename="othello_save.txt"):
    ################################################################################################################
    """Save Othello board and current player to a text file.

    Format:
        -Line 1:1 or 2(current player)
        -Line 2-9:eight rows, each row is 8 values seperated by spaces (each 0,1,2)

    Returns:
        True on success"""
    ################################################################################################################
    
    keys=[0,1,2]  #0->empty,1->black,2->white
    with open(filename,"w") as f:
        f.write(str(current_player)+"\n")
        for row in board:
            line=" ".join(str(cell) for cell in row)
            f.write(line+"\n")
    print("Game saved succesfully.")
    return True

def load_game(filename="othello_save.txt"):
    ################################################################################################################
    """Load Othello game state from a text file.

    Expected file format:
        Line 1: current player (1 or 2)

        Lines 2-9: 8 roews, each containing 8 space-seperated values.
            Each value must be one of:
                                 0 ->empty
                                 1->black
                                 2 ->white
    Returns:
        (board, current_player)
            board: 8x8 list of lists containing 0, 1, 2
            current_player:1 or 2
        (None,None)
            if the file does not exist, is corrupted, or the format is invalid."""
    ################################################################################################################

    with open(filename, "r") as f:
        current_player=f.readline().strip()
        board=[]
        for i in range(8):
            row =(f.readline()).strip()
            board.append(list(map(int,row.split())))
        return board, int(current_player)



