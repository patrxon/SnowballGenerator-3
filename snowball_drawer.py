import pygame as pg
from tuple_operations import calculate_pos


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

    def draw_lines(self, offset, line_arr, size=2, color=(0, 0, 0)):

        prev_point = calculate_pos(offset, list(line_arr)[0], size)
        for line in line_arr:
            next_point = calculate_pos(offset, line, size)

            if line_arr[line] == "j":
                pg.draw.circle(self.win, color, next_point, size // 5)
                pg.draw.circle(self.win, color, prev_point, size // 5)
            elif line_arr[line] == "r":
                pg.draw.line(self.win, color, prev_point, next_point, size // 5)
            elif line_arr[line] == "l":
                pg.draw.line(self.win, color, prev_point, next_point, size // 5)


            prev_point = next_point

