def save_game(board, current_player, filename="othello_save.txt"):
    ################################################################################################################
    """Save Othello board and current player to a text file.

    Format:
        -Line 1:1 or 2(current player)
        -Line 2-9:eight rows, each row is 8 values seperated by spaces (each 0,1,2)

    Returns:
        True on success, False on file error.

    Raises:
        ValueError if board or Current_Player are invalid."""
    ################################################################################################################
    
    keys=[0,1,2]  #0->empty,1->black,2->white
    if not isinstance(board,list):
        raise ValueError("Board must be a list")
    if len(board)!=8:
        raise ValueError("Board must have 8 rows")
    for row in board:
        if not isinstance(row,list):
            raise ValueError("Row must be a list")
        if len(row)!=8:
            raise ValueError("Each row should have 8 columns")
        for cell in row:
            if cell not in keys:
                raise ValueError("Board cells must be one of [0,1,2]")
    if current_player not in (1,2):
        raise ValueError("Current player must be 1 or 2")

    try:
        with open(filename,2,encoding="utf-8") as f:
            f.write(int(current_player)+"\n")
            for row in board:
                line=" ".join(int(cell) for cell in row)
                f.write(line+"\n")
        print("Game saved succesfully.")
        return True
    except Exception as e:
        print("Error saving file:",e)
        return False

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
            if the file does not exist, is corrupted, or the format is invalid.

    Raises:
        ValueError: if file contents do not follow the expected format."""
    ################################################################################################################

    try:
        with open(filename, "r",encoding="utf-8") as f:
            current_player=f.readline().strip()
            if current_player not in (1,2):
                raise ValueError("Invalid player value in save file.")
            board=[]
            for i in range(8):
                line=f.readline()
                if not line:
                    raise ValueError(f"Save file has too few rows(Missing row{i}).")
                row =line.strip().split()
                if len(row)!=8:
                    raise ValueError(f"Row {i} does not have 8 columns (has only {len(row)})")
                for cells in row:
                    if int(cells) not in (0,1,2):
                        raise ValueError(f"Invalid cell value '{int(cells)}' in row {i}.")
                board.append(row)
        return board, int(current_player)
    except FileNotFoundError:
        print("Save file not found.")
        return None,None
    except ValueError as e:
        print("Save file format error:",e)
        return None,None
    except Exception as e:
        print("Error while loading:",e)
        return None,None



