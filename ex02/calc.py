import tkinter as tk
import tkinter.messagebox as tkm

if __name__ == "__main__":

    root = tk.Tk()
    root.title("calc")
    root.geometry("300x500")

    def button_click(event):
        btn = event.widget
        txt = btn["text"]
        tkm.showinfo(txt,f"[{txt}]ボタンが押されました")

    r,c = 0,0 #行番号r,列番号cの設定
    for i in range(9,-1,-1):
        
        button = tk.Button(root, text=i, width=4, height=2,
                            font=("Times New Roman", 30),
                            command=button_click)
        button.bind("<1>",button_click)
        button.grid(row = r,column = c)
        c += 1
        if (i-1)%3==0:
            r +=1
            c=0
        
    root.mainloop()