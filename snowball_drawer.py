import pygame as pg
from tuple_operations import calculate_pos


class SnowballDrawer:

    def __init__(self, x, y, width, height, win):
        self.pos_x = x
        self.pos_y = y
        self.width = width
        self.height = height
        self.win = win

    def draw_bg_box(self):
        rect = (self.pos_x, self.pos_y, self.width, self.height)
        color = (100, 100, 100)
        pg.draw.rect(self.win, color, rect)

    def draw_outer_box(self):
        rects = [(0, 0, 1280, 100),
                 (0, 620, 1280, 100),
                 (0, 100, 100, 520),
                 (1180, 100, 100, 520)]

        color = (0, 0, 0)
        for rect in rects:
            pg.draw.rect(self.win, color, rect)

    def draw_lines(self, offset, line_arr, size=2, color=(0, 0, 0)):
        line_width = size // 5
        if line_width <= 0:
            line_width = 1

        prev_point = calculate_pos(offset, list(line_arr)[0], size)
        for line in line_arr:

            next_point = calculate_pos(offset, line, size)

            if line_arr[line] == "j":
                pg.draw.circle(self.win, color, next_point, line_width)
                pg.draw.circle(self.win, color, prev_point, line_width)
            elif line_arr[line] == "r":
                pg.draw.line(self.win, (0, 0, 255), prev_point, next_point, line_width)
            elif line_arr[line] == "l":
                pg.draw.line(self.win, (0, 255, 0), prev_point, next_point, line_width)

            prev_point = next_point

    def draw_segments(self, offset, line_arr, size=2, color=(0, 0, 0)):
        line_width = size // 5
        if line_width <= 0:
            line_width = 1

        prev_point = calculate_pos(offset, list(line_arr)[len(line_arr) - 2], size)
        next_point = calculate_pos(offset, list(line_arr)[len(line_arr) - 1], size)
        move = line_arr[list(line_arr)[len(line_arr) - 1]]

        if move == "j":
            pg.draw.circle(self.win, color, next_point, line_width)
            pg.draw.circle(self.win, color, prev_point, line_width)
        elif move == "r":
            pg.draw.line(self.win, (0, 0, 255), prev_point, next_point, line_width)
        elif move == "l":
            pg.draw.line(self.win, (0, 255, 0), prev_point, next_point, line_width)
