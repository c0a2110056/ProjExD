import datetime
import random
mondai = ["サザエさんの旦那の名前は？","カツオの妹の名前は","タラオはカツオから見てどんな関係？"]
answer = [["マスオ","ますお"],["ワカメ","わかめ"],["甥","おい","甥っ子","おいっこ"]]
n = random.randint(0,2)
#お褒めいただき光栄ですw
def shutudai():
    print("問題")
    print(mondai[n])
    

def kaito():
    ans =input("答え：")
    if ans in answer[n]:
        print("正解！！！")
    else:
        print("出直してこい")
    ed = datetime.datetime.now()
    time = ((ed-st).seconds)
    print(f"{time}秒")

shutudai()
st = datetime.datetime.now()
kaito()