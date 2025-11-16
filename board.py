EMPTY = 'e' #Means cell is empty
WHITE = 'w' #Means cell is filled with white
BLACK = 'b' #Means cell is filled with black 
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
        
    
    def is_full(self):
        for row in self.grid:
            for element in row:
                if element == 'e': return False 
        return True #As soon as all the empty cells are replaced by any colored token it tells that the game is supposed to end
    
    def get_cell(self,r,c):
        return self.grid[r][c]
        
    def is_on_board(self,r,c):
        if (0 <= r and r <= 7 and 0 <= c and c <= 7) : return True
        return False
    
    def get_data(self):
        return self.player, self.grid

    # def set_cell(self,r,c):
        

b = Board()
b.print_board()
print(b.get_score())
print(b.is_full())
print(b.get_cell(1,2))
