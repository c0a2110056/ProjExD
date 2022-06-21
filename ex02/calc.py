import tkinter as tk
import tkinter.messagebox as tkm
from turtle import right

if __name__ == "__main__":

    root = tk.Tk()
    root.title("calc")
    #root.geometry("300x500")

    entry = tk.Entry(root, justify="right",width=10,font=("Times New Roman", 40))
    entry.grid(row=0,column=0,columnspan=3)
    

    def button_click(event):
        btn = event.widget
        txt = btn["text"]
        #tkm.showinfo(txt,f"{txt}のボタンがクリックされました")
        entry.insert(tk.END,txt)

    r,c = 1,0 #行番号r,列番号cの設定
    list = [i for i in range(9,-1,-1)]
    list.append("+")
    for i,j in enumerate(list):
        
        button = tk.Button(root, text=j, width=4, height=2,
                            font=("Times New Roman", 30),
                            )
        button.bind("<1>",button_click)
        button.grid(row = r,column = c)

        c += 1
        if (i+1)%3==0:
            r +=1
            c=0
    
    root.mainloop()