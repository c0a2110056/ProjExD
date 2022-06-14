import string
import random
import datetime
global taisyou,kesson,roop
taisyou = 10
kesson = 2
roop = 5


def mondai():
    alrst = random.sample(list(string.ascii_uppercase),taisyou)
    hyoujirst = random.sample(alrst,taisyou-kesson)
    kessonrst = []
    for i in range(10):
        if not alrst[i] in hyoujirst:
            kessonrst += alrst[i]
    print("対象文字：")
    print(alrst)
    print("表示文字：")
    print(hyoujirst)
    #print(kessonrst)
    return kessonrst

def ans(r):

    kotae = input("欠損文字はいくつあるでしょうか?")
    if kotae == str(kesson):
        print("正解です。それでは具体的に欠損文字を一つずつ入力してください")
        itimojime = input("1つ目の文字を入力してください：")
        if itimojime in r: #一文字目の正誤判定
            r.remove(itimojime)    
            nimojime = input("2つ目の文字を入力してください：")
            if nimojime in r: #二文字目の正誤判定
                print("大正解！！")
                return 1
            else:   
                print("不正解です。またチャレンジしてください")
                print("-"*50)
            

        else:   
            print("不正解です。またチャレンジしてください")
            print("-"*50)
                    
    else:   
        print("不正解です。またチャレンジしてください")
        print("-"*50)

st = datetime.datetime.now()
for i in range(roop):
    r = mondai()
    if ans(r)==1:
        ed = datetime.datetime.now()
        time = ((ed-st).seconds)
        print(f"{time}秒")
        break
