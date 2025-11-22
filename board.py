class Board:
    def __init__(self):
        self.player = 1 
        self.grid = [[0 for _ in range(8)] for _ in range(8)]
        #The below 4 lines sets the initial board
        self.grid[3][3] = 2 #white is 2
        self.grid[4][4] = 2
        self.grid[3][4] = 1 #black is 1
        self.grid[4][3] = 1
        self.w_score = 2
        self.b_score = 2

    def count(self):
        self.w_score = 0
        self.b_score = 0
        for i in self.grid:
            for j in i:
                if j == 2:
                    self.w_score+=1
                elif j == 1:
                    self.b_score+=1

    def end_game(self):
        if self.w_score + self.b_score == 64 or self.w_score * self.b_score == 0:
            return True
        return False