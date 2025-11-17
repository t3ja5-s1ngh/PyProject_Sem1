import tkinter as tk

class myGUI:

    ###################################################################################
    def __init__(self):
        self.root = tk.Tk()
        self.root.configure(bg="black")
        self.root.title("Othello Board")
        self.root.geometry("1000x1000+400+200")

        self.canvas = tk.Canvas(self.root, width=896, height=896,
                                bg="darkgreen", highlightthickness=3)
        self.canvas.pack(anchor="center")

        self.btn_start = tk.Button(self.root, text="Start",command=lambda: self.start(self.btn_start, self.btn_load, self.status, self.btn_save))
        self.canvas.create_window(448, 400, window=self.btn_start)

        self.btn_load = tk.Button(self.root, text="Load")
        self.canvas.create_window(448, 448, window=self.btn_load)

        self.status = tk.Label(self.root, text="Othello",
                               font=("Arial", 12), bg="lightgray")
        self.status.place(x=40, y=900, width=920, height=50)

        self.btn_save = tk.Button(self.root, text="Save")

        self.canvas.bind("<Button-1>", self.click)

        self.root.mainloop()
    ###################################################################################

    def draw_grid(self, w, h):
        self.canvas.delete("all")
        for i in range(9):
            self.canvas.create_line(0, i*(w//8), w, i*(w//8), fill="black")
            self.canvas.create_line(i*(h//8), 0, i*(h//8), h, fill="black")

    def play(self, row, col, color, blackscore, whitescore):
        x1 = col * 112 + 10
        y1 = row * 112 + 10
        x2 = (col+1) * 112 - 10
        y2 = (row+1) * 112 - 10

        self.canvas.create_oval(x1, y1, x2, y2, fill=color)
        self.status.config(text=f"Black:{blackscore}                      White:{whitescore}")

    def start(self, widget1, widget2, widget3, widget4):
        widget1.destroy()
        widget2.destroy()
        widget3.config(text="Black:2                      White:2")
        widget4.place(x=472, y=960)

        self.draw_grid(896, 896)
        self.play(3, 3, "white", 2, 2)
        self.play(3, 4, "black", 2, 2)
        self.play(4, 3, "black", 2, 2)
        self.play(4, 4, "white", 2, 2)

    def click(self, event):
        row = event.y // 112
        col = event.x // 112
        return row, col


myGUI()

