import pygame as pg
import sys
import random

class Screen:
    def __init__(self, title, wh, image):
        pg.display.set_caption(title)
        self.sfc = pg.display.set_mode(wh)       # Surface
        self.rct = self.sfc.get_rect()           # Rect
        self.bgi_sfc = pg.image.load(image)      # Surface
        self.bgi_rct = self.bgi_sfc.get_rect()   # Rect

    def blit(self):
        self.sfc.blit(self.bgi_sfc, self.bgi_rct) 


class Bird:
    def __init__(self, image: str, size: float, xy):
        self.sfc = pg.image.load(image)    # Surface
        self.sfc = pg.transform.rotozoom(self.sfc, 0, size)  # Surface
        self.rct = self.sfc.get_rect()          # Rect
        self.rct.center = xy

    def blit(self,scr: Screen):
        #screen_sfc.blit(kkimg_sfc, kkimg_rct)
        scr.sfc.blit(self.sfc, self.rct)

    def update(self,scr: Screen):
        key_states = pg.key.get_pressed() # 辞書
        if key_states[pg.K_UP]:
            self.rct.centery -= 1
        if key_states[pg.K_DOWN]:
            self.rct.centery += 1
        if key_states[pg.K_LEFT]:
            self.rct.centerx -= 1
        if key_states[pg.K_RIGHT]:
            self.rct.centerx += 1
        # # 練習7
        if check_bound(self.rct, scr.rct) != (1, 1): # 領域外だったら
            if key_states[pg.K_UP]:
                self.rct.centery += 1
            if key_states[pg.K_DOWN]:
                self.rct.centery -= 1
            if key_states[pg.K_LEFT]:
                self.rct.centerx += 1
            if key_states[pg.K_RIGHT]:
                self.rct.centerx -= 1
        self.blit(scr)
    
    def attack(self):
        return Shot(self)
    

class Bomb:
    def __init__(self, color, size, vxy, scr: Screen):
        self.sfc = pg.Surface((2*size, 2*size)) # Surface
        self.sfc.set_colorkey((0, 0, 0)) 
        pg.draw.circle(self.sfc, color, (size, size), size)
        self.rct = self.sfc.get_rect() # Rect
        self.rct.centerx = random.randint(0, scr.rct.width)
        self.rct.centery = random.randint(0, scr.rct.height)
        self.vx, self.vy = vxy 

    def blit(self,scr: Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self,scr: Screen):
        # 練習6
        self.rct.move_ip(self.vx, self.vy)
        # 練習7
        yoko, tate = check_bound(self.rct, scr.rct)
        self.vx *= yoko
        self.vy *= tate
        # 練習5
        self.blit(scr)


class Enemy:
    def __init__(self, image, size, vxy, scr: Screen):
        self.sfc = pg.image.load(image)
        self.sfc = pg.transform.rotozoom(self.sfc, 0, size) 
        self.rct = self.sfc.get_rect() # Rect
        self.rct.centerx = random.randint(0, scr.rct.width)
        self.rct.centery = random.randint(0, scr.rct.height)
        self.vx, self.vy = vxy 

    def blit(self,scr: Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self,scr: Screen):
        self.rct.move_ip(self.vx, self.vy)
        yoko, tate = check_bound(self.rct, scr.rct)
        self.vx *= yoko
        self.vy *= tate
        self.blit(scr)


class Color:
    def _init__(self):
        self.color = color_random()


class Explosion(pg.sprite.Sprite):

    defaultlife = 12
    animcycle = 3
    images = []

    def __init__(self, actor):
        pg.sprite.Sprite.__init__(self, self.containers)
        self.image = self.images[0]
        self.rect = self.image.get_rect(center=actor.rect.center)
        self.life = self.defaultlife


class Shot:
    def __init__(self, chr:Bird):
        self.sfc = pg.image.load("fig/beam.png")
        self.sfc = pg.transform.rotozoom(self.sfc, 0, 0.3)  # Surface
        self.rct = self.sfc.get_rect()          # Rect
        self.rct.midleft = chr.rct.center

    def blit(self,scr: Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self,scr: Screen):
        self.rct.move_ip(+10, 0) # 右方向に速度10で移動する
        self.blit(scr)
        if check_bound(self.rct, scr.rct) != (1,1): # 領域外に出たら
            del self    
        

def main():
    clock = pg.time.Clock()
    scr = Screen("負けるな！こうかとん",(1600,900),"fig/pg_bg.jpg")
    kkt = Bird("fig/6.png", 2.0, (900, 400))
    mons = Enemy("fig/monster2.png",0.1,(+1,+1),scr)
    bkd = Bomb((255,0,0),10,(+1,+1),scr)
    beam = None # ビームの有無
    bak =[bkd] #　爆弾を複数作るためのリスト
    c = Color()
    while True:
        scr.blit()
        # 練習2
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
            if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
                beam = kkt.attack() # スペースキーが押されたらこうかとんがビームをうつ
            if event.type == pg.KEYDOWN and event.key == pg.K_1:
                nb = Bomb((color_random()),10,(+1,+1),scr)
                bak.append(nb)

        
        
        kkt.update(scr)
        for i in bak:
            i.update(scr)

        mons.update(scr)
        if beam:
            beam.update(scr)
        

        if kkt.rct.colliderect(bkd.rct):
            n = random.randint(0,9)
            kkt.rct = kkt.sfc.get_rect()
            xy = kkt.rct.center
            kkt = Bird(f"fig/{n}.png", 2.0,(900,600))

         
        if kkt.rct.colliderect(mons.rct):
            return
        
        pg.display.update()
        clock.tick(1000)



def check_bound(rct, scr_rct):
    '''
    [1] rct: こうかとん or 爆弾のRect
    [2] scr_rct: スクリーンのRect
    '''
    yoko, tate = +1, +1 # 領域内
    if rct.left < scr_rct.left or scr_rct.right  < rct.right : yoko = -1 # 領域外
    if rct.top  < scr_rct.top  or scr_rct.bottom < rct.bottom: tate = -1 # 領域外
    return yoko, tate

def color_random():#　爆弾の色をランダムに決める関数
    x, y = 0, 255
    a = random.randint(x,y)
    b = random.randint(x,y)
    c = random.randint(x,y)
    return (a,b,c)

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()