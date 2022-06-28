import tkinter as tk
import tkinter.messagebox as tkm
import maze_maker as mm
import random 
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
    move = {#キー：押されているキーkey/値：移動幅リスト[x,y]
        ""     :[0, 0],
        "Up"   :[0, -1],
        "Down" :[0, +1],
        "Left" :[-1, 0],
        "Right":[+1, 0],
    }
    try:
        if maze_bg[my+move[key][1]][mx+move[key][0]] == 0:
            my, mx = my+move[key][1], mx+move[key][0]

    except:
        pass
    #if maze_bg[][] == 0: #　もし移動先が床なら
    #if key == "Up"    : my-= 1
    #if key == "Down"  : my+= 1
    #if key == "Left"  : mx-= 1
    #if key == "Right" : mx+= 1
    cx,cy = mx*100+50, my*100+50
    canvas.coords("tori",cx,cy)
    root.after(100,main_proc)

def goal_place():
    a,b = 0,0
    gx,gy = 0,0
    while True:
        a = random.randint(0,8)
        b = random.randint(0,14)
        if maze_bg[a][b] ==0:
            break
    gx,gy = a,b
    return gx,gy


def reset(event):
    global key
    key = event.keysym
    if key == "Space":
        maze_bg = mm.make_maze(15,9) #1:壁/0:床を表す二次元リスト
        mm.show_maze(canvas,maze_bg)

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
    start = tk.Label(root,text="START",fg="green",
            font=("Times New Roman",20)
            )
    start.place(x=cx-100,y=cy-75)

    goal = tk.Label(root,text="GOAL",fg="red",
            font=("Times New Roman",20)
            )
    gx,gy = goal_place()
    dx,dy = gx*100+50,gx*100+50
    goal.place(x=dx-100,y=dy-75)
    key = ""
    root.bind("<KeyPress>",key_down)

    root.bind("<KeyRelease>",key_up)

    root.bind("<KeyPress>",reset)

    if dx==cx and dy==cy:
        tkm.showinfo("やったね！","Comgraturation!!")
    main_proc()

    root.mainloop()   