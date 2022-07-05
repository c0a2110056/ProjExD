import pygame as pg
import sys

def main():
    clock = pg.time.Clock() #　時間計測用のオブジェクト

    pg.display.set_caption("逃げろ！こうかとん")   #　タイトルバーに表示
    screen_sfc = pg.display.set_mode((1600,900)) #　1600x900の画面Surfaceを生成する
    screen_rct = screen_sfc.get_rect()           #　Rect
    bgimg_sfc = pg.image.load("fig/pg_bg.jpg")   #　Surface
    bgimg_rct = bgimg_sfc.get_rect()             #　Rect
    #screen_sfc.blit(bgimg_sfc,bgimg_rct)

    kkimg_sfc = pg.image.load("fig/6.png") #　Surface
    kkimg_sfc = pg.transform.rotozoom(kkimg_sfc,0,2.0) #　Surface
    kkimg_rct = kkimg_sfc.get_rect()       #　Rect
    kkimg_rct.center = 900, 400


    while True:
        screen_sfc.blit(bgimg_sfc,bgimg_rct)
        
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        key_states = pg.key.get_pressed() #辞書
        if key_states[pg.K_UP]    == True: kkimg_rct.centery -= 1
        if key_states[pg.K_DOWN]  == True: kkimg_rct.centery += 1
        if key_states[pg.K_LEFT]  == True: kkimg_rct.centerx -= 1
        if key_states[pg.K_RIGHT] == True: kkimg_rct.centerx += 1
        screen_sfc.blit(kkimg_sfc,kkimg_rct)

        pg.display.update()
        clock.tick(1000)


if __name__ == "__main__":
    pg.init()             #　モジュールを初期化する
    main()                #　ゲームのメイン部分
    pg.quit()             #　モジュールの初期化を解除する
    sys.exit()            #　プログラムを終了する