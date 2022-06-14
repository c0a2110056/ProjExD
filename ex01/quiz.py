import datetime
import random
mondai = ["サザエさんの旦那の名前は？","カツオの妹の名前は","タラオはカツオから見てどんな関係？"]
kotae = [["マスオ","ますお"],["ワカメ","わかめ"],["甥","おい","甥っ子","おいっこ"]]
n = random.randint(0,3)

def shutudai():
    print("問題")
    print(mondai[n])
    

def kaito():
    ans =input("答え：")
    if ans in kotae[n]:
        print("正解！！！")
    else:
        print("出直してこい")
    

shutudai()
st = datetime.datetime.now()
kaito()
ed = datetime.datetime.now()
time = ((ed-st).seconds)
print(f"{time}秒")