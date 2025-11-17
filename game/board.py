class Board:
    def __init__(self):
        self.player = 1 
        self.grid = [['e' for _ in range(8)] for _ in range(8)]
        #The below 4 lines sets the initial board
        self.grid[3][3] = 2 #white is 2
        self.grid[4][4] = 2
        self.grid[3][4] = 1 #black is 1
        self.grid[4][3] = 1
        self.w_score = 2
        self.b_score = 2

    def print_board(self):
        for row in self.grid:
            print(*row)