import tkinter as tk

def key_down(event):
    global key
    key = event.keysym
    #print(key)

def key_up(event):
    global key
    key = ""
    #print("きえたよ")

if __name__ == "__main__":
    
    root = tk.Tk()
    root.title("迷えるこうかとん")

    canvas = tk.Canvas(width=1500,height=900,bg="black")
    canvas.pack()

    tori = tk.PhotoImage(file="fig/9.png")
    cx,cy = 300,400
    canvas.create_image(cx,cy,image=tori,tag="tori")

    key = ""
    root.bind("<KeyPress>",key_down)

    root.bind("<KeyRelease>",key_up)

    root.mainloop()   