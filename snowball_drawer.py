import pygame as pg


def add_up(tuple_a, tuple_b):
    return tuple(map(sum, zip(tuple_a, tuple_b)))


def multiple(tuple_, times):
    return tuple([times * x for x in tuple_])


class SnowballDrawer:

    def __init__(self, x, y, width, height, win):
        self.pos_x = x
        self.pos_y = y
        self.width = width
        self.height = height
        self.win = win

    def draw_box(self):
        rect = (self.pos_x, self.pos_y, self.width, self.height)
        color = (100, 100, 100)
        pg.draw.rect(self.win, color, rect)

    def draw_lines(self, offset, line_arr, size=2, color=(0,0,0)):
        last_pos = offset
        for line in line_arr:
            pg.draw.line(self.win, color, last_pos, add_up(offset, multiple(line, size)), 2)
            last_pos = add_up(offset, multiple(line, size))
