import pygame as pg
pg.init()
img = pg.image.load('input.jpg')
W, H = img.get_width(), img.get_height()
sc = pg. display.set_mode((W, H))
def in_ranger(x):
    if x<0:
        return 0
    elif x>255 : 
        return 255
    else : 
        return x
Factor = 1/9
Bias = 0
zarayeb= [[1, 1, 1,],
          [1, 1, 1,],
          [1, 1, 1,]]
for x in range(1, W-1):
    for y in range(1, H-1):
        col = img.get_at((x,y))
        R = 0
        G = 0
        B = 0
        for x1 in range(-1 , 2): 
            for y1 in range(-1 , 2):
                color = img.get_at((x + x1,y + y1))
                R += color[0]*zarayeb[x1+1][y1+1]
                G += color[1]*zarayeb[x1+1][y1+1]
                B += color[2]*zarayeb[x1+1][y1+1]
        sc.set_at((x,y),(in_ranger(int(Factor*R+Bias)), in_ranger(int(Factor*G+Bias)), in_ranger(int(Factor*B+Bias))))
pg.image.save(sc, 'output.png')
pg.quit()