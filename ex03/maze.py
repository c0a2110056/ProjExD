import tkinter as tk
import tkinter.messagebox as tkm
import maze_maker as mm

def key_down(event):
    global key
    key = event.keysym
    #print(key)

def key_up(event):
    global key
    key = ""
    #print("きえたよ")

def main_proc():
    global cx, cy, key, mx, my
    #move = {#キー：押されているキーkey/値：移動幅リスト[x,y]
    #    ""     :[0, 0],
    #    "Up"   :[0, -20],
    #    "Down" :[0, +20],
    #    "Left" :[-20, 0],
    #    "Right":[+20, 0],
    #}
    #cx, cy = cx+move[key][0], cy+move[key][1]
    if key == "Up"    : my-= 1
    if key == "Down"  : my+= 1
    if key == "Left"  : mx-= 1
    if key == "Right" : mx+= 1
    cx,cy = mx*100+50, my*100+50
    canvas.coords("tori",cx,cy)
    root.after(100,main_proc)
if __name__ == "__main__":
    
    root = tk.Tk()
    root.title("迷えるこうかとん")

    canvas = tk.Canvas(width=1500,height=900,bg="black")
    canvas.pack()

    maze_bg = mm.make_maze(15,9) #1:壁/0:床を表す二次元リスト
    mm.show_maze(canvas,maze_bg) # canvasにmaze_bgを描画　

    tori = tk.PhotoImage(file="fig/9.png")
    mx, my = 1,1
    cx,cy = mx*100+50,my*100+50
    canvas.create_image(cx,cy,image=tori,tag="tori")

    key = ""
    root.bind("<KeyPress>",key_down)

    root.bind("<KeyRelease>",key_up)

    main_proc()

    root.mainloop()   