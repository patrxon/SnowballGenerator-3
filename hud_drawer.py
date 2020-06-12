import pygame as pg


class HudDrawer:

    def __init__(self, sizes, win):
        self.pos_x = sizes[0]
        self.pos_y = sizes[1]
        self.width = sizes[2]
        self.height = sizes[3]
        self.win = win

    def draw_outer_box(self):
        rects = [(0, 0, self.pos_x + self.width, self.pos_y),
                 (0, 0, self.pos_x, self.pos_y + self.height)]

        color = (0, 0, 0)
        for rect in rects:
            pg.draw.rect(self.win, color, rect)
