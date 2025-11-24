import tkinter as tk
####
####
####
class myGUI:
################################################################################################################
    def __init__(self,control):
    ########setup main window
        self.control=control
        self.root = tk.Tk()
        self.root.configure(bg="black")
        self.root.title("Othello")
        self.root.geometry("1000x1000+400+200")
    ########set canvas for board display
        self.canvas = tk.Canvas(self.root, width=896, height=896,  bg="darkgreen", highlightthickness=3)
        self.canvas.pack(anchor="center")
    ########set start button 
        self.btn_start = tk.Button(self.root, text="Start",command=self.start)
        self.canvas.create_window(448, 400, window=self.btn_start)
    ########set load button
        self.btn_load = tk.Button(self.root, text="Load",command=self.load_game)
        self.canvas.create_window(448, 448, window=self.btn_load)
    ########set status bar
        self.status = tk.Label(self.root, text="Othello", font=("Arial", 12), bg="lightgray")
        self.status.pack(side=tk.BOTTOM, fill=tk.X)
    ########set save button
        self.btn_save = tk.Button(self.root, text="Save",command=control.save)
################################################################################################################
    def draw_grid(self, w, h):
    ########clear canvas and draw grid lines
        self.canvas.delete("all")
        for i in range(9):
            self.canvas.create_line(0, i*(w//8), w, i*(w//8), fill="black")
            self.canvas.create_line(i*(h//8), 0, i*(h//8), h, fill="black")
################################################################################################################
    def play(self, row, col, color, blackscore, whitescore,turn):
    ########draw a piece and update status bar  
        x1 = col * 112 + 10
        y1 = row * 112 + 10
        x2 = (col+1) * 112 - 10
        y2 = (row+1) * 112 - 10
        color="black" if color==1 else "white"
        turn="Black"  if turn==1 else "White"
        self.canvas.create_oval(x1, y1, x2, y2, fill=color)
        self.status.config(text=f"Black:{blackscore}              {turn}'s turn              White:{whitescore}")
################################################################################################################
    def start(self):
    ########start a new game and bind click event
        self.btn_save.pack(side=tk.BOTTOM, pady=10)
        self.canvas.bind("<Button-1>",self.click)
        self.draw_grid(896, 896)
        self.play(3, 3, 0, 2, 2,1)
        self.play(3, 4, 1, 2, 2,1)
        self.play(4, 3, 1, 2, 2,1)
        self.play(4, 4, 0, 2, 2,1)
################################################################################################################
    def click(self, event):
    ########calculate row and column from mouse click and pass to controller
        row = event.y // 112
        col = event.x // 112
        self.control.handle_move(row, col)
################################################################################################################
    def load_game(self):
    ########load a saved game and bind click event
        self.btn_save.pack(side=tk.BOTTOM, pady=10)
        self.canvas.bind("<Button-1>",self.click)
        self.draw_grid(896, 896)
        self.control.load()
################################################################################################################
    def run(self):
    ########start the main event loop
       self.root.mainloop()
################################################################################################################      
    def endame(self, blackscore, whitescore):
    ########display end game message
        self.canvas.unbind("<Button-1>")
        self.btn_restart = tk.Button(self.root, text="Restart",command=self.start)
        self.canvas.create_window(448, 500, window=self.btn_restart)
        if blackscore > whitescore:
            winner = "Black"
        elif whitescore > blackscore:
            winner = "White"
        else:
            winner = "No one. It's a tie"
        self.status.config(text=f"Black:{blackscore}              {winner} wins              White:{whitescore}")
###
###
###