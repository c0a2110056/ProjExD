import random
import tkinter as tk

def make_maze(yoko, tate):
    XP = [ 0, 1, 0, -1]
    YP = [-1, 0, 1,  0]

    maze_lst = []
    for y in range(tate):
        maze_lst.append([0]*yoko)
    for x in range(yoko):
        maze_lst[0][x] = 1
        maze_lst[tate-1][x] = 1
    for y in range(1, tate-1):
        maze_lst[y][0] = 1
        maze_lst[y][yoko-1] = 1
    for y in range(2, tate-2, 2):
        for x in range(2, yoko-2, 2):
            maze_lst[y][x] = 1
    for y in range(2, tate-2, 2):
        for x in range(2, yoko-2, 2):
            if x > 2: rnd = random.randint(0, 2)
            else:     rnd = random.randint(0, 3)
            maze_lst[y+YP[rnd]][x+XP[rnd]] = 1

    return maze_lst

def show_maze(canvas, maze_lst):
    color = ["white", "gray"]
    for y in range(len(maze_lst)):
        for x in range(len(maze_lst[y])):
            canvas.create_rectangle(x*100, y*100, x*100+100, y*100+100, 
                                    fill=color[maze_lst[y][x]])

if __name__ == "__main__":

    root = tk.Tk()
    root.title("迷えるこうかとん")
    canvas = tk.Canvas(width=1500,height=900,bg="black")
    canvas.pack()
    root.mainloop()   