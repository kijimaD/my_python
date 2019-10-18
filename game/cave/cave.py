""" cave - Copyright 2016 Kenichiro Tanaka  """
import sys
from random import randint
from math import sin, radians
import pygame
from pygame.locals import QUIT, Rect, KEYDOWN, K_SPACE
import math

pygame.init()
pygame.key.set_repeat(5, 5)
SURFACE = pygame.display.set_mode((800, 600))
FPSCLOCK = pygame.time.Clock()


def main():
    """ メインルーチン """
    walls = 160 # default: 80
    rect = Rect(0, 300, 10, 10)
    ship_y = 250
    velocity = 0
    score = 0
    offset = 0
    speed = 10
    slope = randint(1, 6)
    updown_speed = 1 # デフォルトは3
    sysfont = pygame.font.SysFont(None, 36)
    ship_image = pygame.image.load("ship.png")
    bang_image = pygame.image.load("bang.png")
    holes = []
    # for xpos in range(walls):
    #     # holes.append(Rect(xpos * 10, 100, 10, 400))
    #     holes.append(Rect(xpos * 5, 100, 5, 400))
    game_over = False

    while True:
        is_space_down = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_SPACE:
                    is_space_down = True

        if not game_over:
            velocity += -updown_speed if is_space_down else updown_speed
            rect.y += velocity
            offset += speed
            if offset % 100 == 0:
                speed += 2

        SURFACE.fill((0, 255, 0))

        # draw ceiling
        points = [(0,0)]
        for pos_x in range(0, 610, 10):
            pos_y = 200 + sin(radians(pos_x + offset) / 2) * 80
            points.append((pos_x, pos_y))
            if pos_x == 10 and rect.y < pos_y:
                game_over = True
        points.append([600, 0])
        pygame.draw.polygon(SURFACE, (165, 42, 42), points)

        # draw floor
        points = [(0, 600)]
        for pos_x in range(0, 610, 10):
            pos_y = 400 + sin(radians(pos_x + offset) / 3) * 60
            points.append((pos_x, pos_y))
            if pos_x == 10 and rect.bottom > pos_y:
                game_over = True
        points.append([600, 600])
        pygame.draw.polygon(SURFACE, (165, 42, 42), points)

        # 自機を移動
        # if not game_over:
        #     score += 10
        #     velocity += (-1 * updown_speed) if is_space_down else updown_speed
        #     ship_y += velocity
        #
        #     # 洞窟をスクロール
        #     edge = holes[-1].copy() # リストの最後をコピーして代入
        #     test = edge.move(0, slope) # 試しに移動させて、飛び出したら傾斜の正負を入れ替えリセットする
        #     if test.top <= 0 or test.bottom >= 600:
        #         slope = randint(1, 6) * (-1 if slope > 0 else 1)
        #         edge.inflate_ip(0, -20)
        #     edge.move_ip(5,slope) # 描写位置を移動させる？
        #     holes.append(edge)
        #     del holes[0] # 左端を削除する
        #     holes = [x.move(-5, 0) for x in holes] # すべて左に動かす

            # 衝突 ?
            # 接触するのはは常に一番左の矩形。それと、自機のy座標を比較する。自機が矩形の範囲内にある＝ゲーム続行
            # if holes[0].top > ship_y or \
            #         holes[0].bottom < ship_y + 80:
            #     game_over = True

        # 描画
        # SURFACE.fill((0, 255, 0))
        for hole in holes:
            pygame.draw.rect(SURFACE, (0, 0, 0), hole)
        SURFACE.blit(ship_image, (0, rect.y))
        score_image = sysfont.render("score is {}".format(score),
                                     True, (0, 0, 225))
        SURFACE.blit(score_image, (600, 20))

        if game_over:
            SURFACE.blit(bang_image, (0, rect.y - 40))

        pygame.display.update()
        FPSCLOCK.tick(10)


if __name__ == '__main__':
    main()
