import pygame as pg


class HudDrawer:

    def __init__(self, sizes, win):
        self.pos_x = sizes[0]
        self.pos_y = sizes[1]
        self.width = sizes[2]
        self.height = sizes[3]
        self.win = win

        self.draw_speed = 0

    def change_speed(self, speed, paused):
        self.draw_speed = speed
        if not paused:
            self.draw_speed = -1

    def draw_hud(self):
        self.draw_outer_box()
        self.draw_game_speed()

    def draw_outer_box(self):
        rects = [(0, 0, self.pos_x + self.width, self.pos_y),
                 (0, 0, self.pos_x, self.pos_y + self.height)]

        color = (0, 0, 0)
        for rect in rects:
            pg.draw.rect(self.win, color, rect)

    def draw_game_speed(self):
        if self.draw_speed >= 0:
            speed = str(100/(2**self.draw_speed))
        else:
            speed = "paused"

        pg.font.init()
        myfont = pg.font.SysFont('Comic Sans MS', 30)
        textsurface = myfont.render(speed, False, (255, 255, 255))
        self.win.blit(textsurface, (0, 0))
