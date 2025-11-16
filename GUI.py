    import tkinter as tk
    #######################################################################################
            def draw_grid(w, h):
            canvas.delete("all")
            for i in range(9):
                canvas.create_line(0, i*(w//8), w, i*(w//8), fill="black")
                canvas.create_line(i*(h//8), 0, i*(h//8), h, fill="black")

        def play(row, col, color,blackscore,whitescore):
            x1 = col * 112 + 10
            y1 = row * 112 + 10
            x2 = (col+1) * 112 - 10
            y2 = (row+1) * 112 - 10
            canvas.create_oval(x1, y1, x2, y2, fill=color)
            status.config(text=f"Black:{blackscore}                      White:{whitescore}")

        def start(widget1,widget2,widget3,widget4):
            widget1.destroy()
            widget2.destroy()
            widget3.config(text="Black:2                      White:2")
            widget4.place(x=472,y=960,)
            draw_grid(896, 896)
            play(3, 3, "white",2,2)
            play(3, 4, "black",2,2)
            play(4, 3, "black",2,2)
            play(4, 4, "white",2,2)

        def click(event):
            row = event.y // 112
            col = event.x // 112
            print("Clicked:", row, col)
        ########################################################################################
        root = tk.Tk()
        root.configure(bg="black")
        root.title("Othello Board")
        root.geometry("1000x1000+400+200")

        canvas = tk.Canvas(root, width=896, height=896, bg="darkgreen",highlightthickness=3)
        canvas.pack(anchor="center")

        btn_start=tk.Button(root, text="Start", command=lambda :start(btn_start,btn_load,status,btn_save))
        canvas.create_window(448,400,window=btn_start)

        btn_load=tk.Button(root,text="Load")
        canvas.create_window(448,448,window=btn_load)

        status = tk.Label(root, text="Othello", font=("Arial", 12), bg="lightgray")
        status.place(x=40,y=900,width=920,height=50)

        btn_save=tk.Button(root,text="Save")

        canvas.bind("<Button-1>",click)


        root.mainloop()
