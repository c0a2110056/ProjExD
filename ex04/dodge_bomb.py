import pygame as pg
import sys

def main():
    clock = pg.time.Clock() #　時間計測用のオブジェクト

    pg.display.set_caption("逃げろ！こうかとん")   #　タイトルバーに表示
    screen_sfc = pg.display.set_mode((1600,900)) #　1600x900の画面Surfaceを生成する
    screen_rct = screen_sfc.get_rect()           #　Rect
    bgimg_sfc = pg.image.load("fig/pg_bg.jpg")   #　Surface
    bgimg_rct = bgimg_sfc.get_rect()             #　Rect
    screen_sfc.blit(bgimg_sfc,bgimg_rct)

    while True:
        screen_sfc.blit(bgimg_sfc,bgimg_rct)

        for event in pg.event.get():
            if event.type == pg.QUIT: return
        
        pg.display.update()
        clock.tick(1000)


if __name__ == "__main__":
    pg.init()             #　モジュールを初期化する
    main()                #　ゲームのメイン部分
    pg.quit()             #　モジュールの初期化を解除する
    sys.exit()            #　プログラムを終了する