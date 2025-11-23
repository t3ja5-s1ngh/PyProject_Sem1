import board
import game_logic as logic
import file_manager   
from GUI import myGUI
#############################################################################################################################
#############################################################################################################################
#############################################################################################################################
class Game:
    def __init__(self):
        self.board = board.Board()
        self.gui =myGUI(self)
        self.gui.run()
#############################################################################################################################
    def handle_move(self,row, col):
        self.board.grid,self.board.player=logic.next_state(self.board.grid, row, col, self.board.player)
        self.board.count()
        for r in range(8):
            for c in range(8):
                if self.board.grid[r][c] != 0:
                    self.gui.play(r, c,self.board.grid[r][c], self.board.b_score, self.board.w_score,self.board.player)
#############################################################################################################################
    def save(self):
        file_manager.save_game(self.board.grid, self.board.player)
#############################################################################################################################
    def load(self):
        board_state, current_player = file_manager.load_game()
        self.board.grid = board_state
        self.board.player = current_player
        for r in range(8):
            for c in range(8):
                if self.board.grid[r][c] != 0:
                    self.gui.play(r, c,self.board.grid[r][c], self.board.b_score, self.board.w_score,self.board.player)
#############################################################################################################################
#############################################################################################################################
#############################################################################################################################
controller = Game()
