import pygame as pg
import sys
import random

def main():
    clock = pg.time.Clock() #　時間計測用のオブジェクト

    #　スクリーンと背景
    pg.display.set_caption("逃げろ！こうかとん")   #　タイトルバーに表示
    screen_sfc = pg.display.set_mode((1600,900)) #　1600x900の画面Surfaceを生成する
    screen_rct = screen_sfc.get_rect()           #　Rect
    bgimg_sfc = pg.image.load("fig/pg_bg.jpg")   #　Surface
    bgimg_rct = bgimg_sfc.get_rect()             #　Rect
    #screen_sfc.blit(bgimg_sfc,bgimg_rct)

    #　こうかとん
    kkimg_sfc = pg.image.load("fig/6.png") #　Surface
    kkimg_sfc = pg.transform.rotozoom(kkimg_sfc,0,2.0) #　Surface
    kkimg_rct = kkimg_sfc.get_rect()       #　Rect
    kkimg_rct.center = 900, 400
    c = 0                                  #  こうかとんがぶつかった回数

    #　爆弾
    
    bmimg_sfc = pg.Surface((20,20)) #　Surface
    bmimg_sfc.set_colorkey((0,0,0))
    color = color_random(0,255)
    pg.draw.circle(bmimg_sfc,color,(10,10),10)
    bmimg_rct = bmimg_sfc.get_rect() #　Rect
    bmimg_rct.centerx = random.randint(0,screen_rct.width)
    bmimg_rct.centerx = random.randint(0,screen_rct.height)
    vx, vy = +1, +1 #　加速度
    

    while True:
        screen_sfc.blit(bgimg_sfc,bgimg_rct)
        
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        key_states = pg.key.get_pressed() #辞書
        if key_states[pg.K_UP]    == True: kkimg_rct.centery -= 1
        if key_states[pg.K_DOWN]  == True: kkimg_rct.centery += 1
        if key_states[pg.K_LEFT]  == True: kkimg_rct.centerx -= 1
        if key_states[pg.K_RIGHT] == True: kkimg_rct.centerx += 1

        if key_states[pg.K_SPACE] == True: #SPACEキーを押されたら
            bmimg_sfc1 = pg.Surface((20,20)) #　Surface
            bmimg_sfc1.set_colorkey((0,0,0))
            pg.draw.circle(bmimg_sfc1,color_random(0,255),(10,10),10)
            bmimg_rct1 = bmimg_sfc1.get_rect() #　Rect
            bmimg_rct1.centerx = random.randint(0,screen_rct.width)
            bmimg_rct1.centerx = random.randint(0,screen_rct.height)
            vx1, vy1 = +1, +1 #　加速度

        #　判定
        if check_bound(kkimg_rct,screen_rct) != (1, 1): #領域外だったら
            if key_states[pg.K_UP]    == True: kkimg_rct.centery += 1
            if key_states[pg.K_DOWN]  == True: kkimg_rct.centery -= 1
            if key_states[pg.K_LEFT]  == True: kkimg_rct.centerx += 1
            if key_states[pg.K_RIGHT] == True: kkimg_rct.centerx -= 1
        screen_sfc.blit(kkimg_sfc,kkimg_rct)

        
        a = size_random()
        bmimg_sfc = pg.Surface((a,a)) #　Surface
        bmimg_sfc.set_colorkey((0,0,0))
        pg.draw.circle(bmimg_sfc,color,(a/2,a/2),a/2)

        #　爆弾の移動
        bmimg_rct.move_ip(vx,vy)
        try:
            if bmimg_rct1: bmimg_rct1.move_ip(vx1,vy1)
        except:
            pass
        

        #　爆弾
        screen_sfc.blit(bmimg_sfc,bmimg_rct)
        try:
            if bmimg_rct1 : screen_sfc.blit(bmimg_sfc1,bmimg_rct1)
        except:
            pass
        
        yoko,tate = check_bound(bmimg_rct, screen_rct)
        vx *= yoko
        vy *= tate

        try:
            yoko1,tate1 = check_bound(bmimg_rct1, screen_rct)
            vx1 *= yoko1
            vy1 *= tate1
        except:
            pass

        #　こうかとんが爆弾にぶつかったら
        try:
            if kkimg_rct.colliderect(bmimg_rct) or kkimg_rct.colliderect(bmimg_rct1):
                n = random.randint(0,9)
                kkimg_sfc = pg.image.load(f"fig/{n}.png") #　Surface
                kkimg_sfc = pg.transform.rotozoom(kkimg_sfc,0,2.0) #　Surface
        except:
            pass

        pg.display.update()
        clock.tick(1000)

def check_bound(rct,scr_rct):
    '''
    [1] rct: こうかとん　or 爆弾のRect
    [2] scr_rct: スクリーンのRect
    '''
    yoko, tate = +1, +1 # 領域内
    if rct.left < scr_rct.left or scr_rct.right < rct.right: yoko = -1 #　領域外
    if rct.top < scr_rct.top or scr_rct.bottom < rct.bottom: tate = -1 #　領域外
    return yoko, tate

def color_random(x,y):
    a = random.randint(x,y)
    b = random.randint(x,y)
    c = random.randint(x,y)
    return (a,b,c)

def new_bomb(scr_rct):
    bmimg_sfc1 = pg.Surface((20,20)) #　Surface
    bmimg_sfc1.set_colorkey((0,0,0))
    pg.draw.circle(bmimg_sfc1,color_random(0,255),(10,10),10)
    bmimg_rct1 = bmimg_sfc1.get_rect() #　Rect
    bmimg_rct1.centerx = random.randint(0,scr_rct.width)
    bmimg_rct1.centerx = random.randint(0,scr_rct.height)
    return bmimg_sfc1, bmimg_rct1

def size_random():
    return random.randint(20,50)
if __name__ == "__main__":
    pg.init()             #　モジュールを初期化する
    main()                #　ゲームのメイン部分
    pg.quit()             #　モジュールの初期化を解除する
    sys.exit()            #　プログラムを終了する