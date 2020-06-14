import pygame as pg
from tuple_operations import calculate_pos


class SnowballDrawer:

    def __init__(self, sizes, win):
        self.pos_x = sizes[0]
        self.pos_y = sizes[1]
        self.width = sizes[2]
        self.height = sizes[3]
        self.offset = (500, 500)
        self.line_size = 5
        self.refresh = False
        self.win = win

    def change_camera_position(self, new_offset, new_size):
        self.offset = new_offset
        self.line_size = new_size
        self.refresh_draw()

    def draw_snowball(self, line_arr, colors=([255, 0, 0], [0, 0, 255], [0, 255, 0])):

        if self.refresh:
            self.draw_bg_box()
            for line in line_arr:
                self.draw_lines(line, colors)
            self.refresh = False
        else:
            for line in line_arr:
                self.draw_segments(line, colors)

    def refresh_draw(self):
        self.refresh = True

    def draw_bg_box(self):
        rect = (self.pos_x, self.pos_y, self.width, self.height)
        color = (100, 100, 100)
        pg.draw.rect(self.win, color, rect)

    def draw_lines(self, line_arr, colors):
        line_width = self.line_size // 5
        if line_width <= 0:
            line_width = 1

        prev_point = calculate_pos(self.offset, line_arr[0][0], self.line_size)
        for line in line_arr:
            next_point = calculate_pos(self.offset, line[0], self.line_size)
            move = line[1]

            self.draw_line(next_point, prev_point, line_width, move, colors)

            prev_point = next_point

    def draw_segments(self, line_arr, colors):

        line_width = self.line_size // 5
        if line_width <= 0:
            line_width = 1

        prev_point = calculate_pos(self.offset, line_arr[-2][0], self.line_size)
        next_point = calculate_pos(self.offset, line_arr[-1][0], self.line_size)
        move = line_arr[-1][1]

        self.draw_line(next_point, prev_point, line_width, move, colors)

    def draw_line(self, next_point, prev_point, line_width, move, colors):

        if move == "j":
            pg.draw.line(self.win, colors[0], prev_point, next_point, line_width)
        elif move == "r":
            pg.draw.line(self.win, colors[1], prev_point, next_point, line_width)
        elif move == "l":
            pg.draw.line(self.win, colors[2], prev_point, next_point, line_width)
