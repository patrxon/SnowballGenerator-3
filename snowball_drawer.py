import pygame as pg
from tuple_operations import calculate_pos


class SnowballDrawer:

    def __init__(self, sizes, win):
        self.pos_x = sizes[0]
        self.pos_y = sizes[1]
        self.width = sizes[2]
        self.height = sizes[3]
        self.refresh = False
        self.win = win

    def draw_snowball(self, offset, line_arr, size=2, colors=([255, 0, 0], [0, 0, 255], [0, 255, 0])):

        if self.refresh:
            self.draw_bg_box()
            for line in line_arr:
                self.draw_lines(offset, line, size, colors)
            self.refresh = False
        else:
            for line in line_arr:
                self.draw_segments(offset, line, size, colors)

    def refresh_draw(self):
        self.refresh = True

    def draw_bg_box(self):
        rect = (self.pos_x, self.pos_y, self.width, self.height)
        color = (100, 100, 100)
        pg.draw.rect(self.win, color, rect)

    def draw_lines(self, offset, line_arr, size, colors):
        line_width = size // 5
        if line_width <= 0:
            line_width = 1

        prev_point = calculate_pos(offset, list(line_arr)[0], size)
        for line in line_arr:
            next_point = calculate_pos(offset, line, size)
            move = line_arr[line]

            self.draw_line(next_point, prev_point, line_width, move, colors)

            prev_point = next_point

    def draw_segments(self, offset, line_arr, size, colors):
        line_width = size // 5
        if line_width <= 0:
            line_width = 1

        prev_point = calculate_pos(offset, list(line_arr)[len(line_arr) - 2], size)
        next_point = calculate_pos(offset, list(line_arr)[len(line_arr) - 1], size)
        move = line_arr[list(line_arr)[len(line_arr) - 1]]

        self.draw_line(next_point, prev_point, line_width, move, colors)

    def draw_line(self, next_point, prev_point, line_width, move, colors):

        if move == "j":
            pg.draw.circle(self.win, colors[0], next_point, line_width)
            pg.draw.circle(self.win, colors[0], prev_point, line_width)
        elif move == "r":
            pg.draw.line(self.win, colors[1], prev_point, next_point, line_width)
        elif move == "l":
            pg.draw.line(self.win, colors[2], prev_point, next_point, line_width)
