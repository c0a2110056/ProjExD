import tkinter as tk
import tkinter.messagebox as tkm

if __name__ == "__main__":

    def button_click(event):
        btn = event.widget
        txt = btn["text"] #クリックされたボタンの文字
        if txt == "AC":
            entry.delete(0,tk.END) #表示された式の削除
        elif txt == "素数":
            eqn = entry.get()
            if int(eqn) <=1:
                entry.delete(0,tk.END)
                entry.insert(tk.END,"素数なわけない")
            else:
                for i in range(2, round(int(eqn)**0.5+1)):
                    if int(eqn) % i==0:
                        entry.delete(0,tk.END)
                        entry.insert(tk.END,"残念でした")
                        break
                    else:
                        entry.delete(0,tk.END)
                        entry.insert(tk.END,"素数だよ")

        elif txt == "+/-":
            eqn = entry.get()
            entry.delete(0,tk.END)
            entry.insert(tk.END,(-1)*int(eqn))
        elif txt == "%":
            eqn = entry.get()
            entry.delete(0,tk.END)
            entry.insert(tk.END,int(eqn)/100)
        elif txt == "=":
            eqn = entry.get()
            if  "×" in eqn:
                eqn1 = eqn.replace("×","*")
            if "÷" in eqn:
                eqn1 = eqn.replace("÷","/")
            res = eval(eqn1) #数式計算
            entry.delete(0,tk.END) #表示された式の削除
            entry.insert(tk.END,res) #結果を挿入
        else:
            #tkm.showinfo(txt,f"{txt}のボタンがクリックされました")
            entry.insert(tk.END,txt)

    root = tk.Tk()
    root.title("calc")
    #root.geometry("300x500")　固定しないと自動調整してくれる

    entry = tk.Entry(root, justify="right",
                    width=15,font=("Times New Roman", 40)
                    )
    entry.grid(row=0,column=0,columnspan=4)
    

    r,c = 1,0 #行番号r,列番号cの設定
    
    for i,j in enumerate(["AC","素数","%","÷",
                          7,8,9,"×",
                          4,5,6,"-",
                          1,2,3,"+",
                          "+/-",0,".","="]):
        cn = "darkgray"
        textsize = 30
        if j == "×" or j == "-" or j == "+" or j== "÷":
            cn="cadetblue"
            
        elif j== "AC":
            cn="white"
        
        elif j == "=":
            cn="darkslategray"
        


        button = tk.Button(root, text=j, width=4, height=1,
                        bg=cn,
                        font=("Times New Roman", 30),
                        )
        button.bind("<1>",button_click)
        button.grid(row = r,column = c)

        c += 1
        if (i+1)%4==0:
            r +=1
            c=0
    
    root.mainloop()