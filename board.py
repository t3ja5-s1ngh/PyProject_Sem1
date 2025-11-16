class Board:
    def __init__(self):
        self.player = 0   
        self.grid = [['e' for _ in range(8)] for _ in range(8)]
        #The below 4 lines sets the initial board
        self.grid[3][3] = 'w' 
        self.grid[4][4] = 'w'
        self.grid[3][4] = 'b'
        self.grid[4][3] = 'b'
        self.w_score = 2
        self.b_score = 2

    def print_board(self):
        for row in self.grid:
            print(*row)