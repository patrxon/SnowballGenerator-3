import pygame as pg
import sys

from snowball_drawer import SnowballDrawer
from line_manager import LineManager
from tuple_operations import add_up, subtract


class MainManager:
    def __init__(self, fps, size):
        pg.init()
        self.size = size
        self.win = pg.display.set_mode(self.size)
        self.fps = fps

        self.sbDrawer = SnowballDrawer(100, 100, 1080, 520, self.win)
        self.lnManager = LineManager()

        self.lnManager.add_line((0, 0), (0, 1), ["r", "r", "r", "r", "r", "l"])

        self.lines = self.lnManager.get_lines()

        self.offset = (600, 400)
        self.mouse1 = (0, 0)
        self.mouse2 = (0, 0)
        self.change = False
        self.line_size = 5
        self.sbDrawer.draw_bg_box()
        self.work_loop()

    def work_loop(self):
        clock = pg.time.Clock()


        while True:
            self.display()
            self.events()
            self.update()
            clock.tick(self.fps)

    def update(self):
        self.lnManager.iterate_lines()

    def display(self, refresh=False):
        if self.change or refresh:
            self.sbDrawer.draw_bg_box()
            for line in self.lines:
                self.sbDrawer.draw_lines(self.offset, line, self.line_size)
        else:
            for line in self.lines:
                self.sbDrawer.draw_segments(self.offset, line, self.line_size)
        self.sbDrawer.draw_outer_box()
        pg.display.flip()

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()

            if event.type == pg.MOUSEBUTTONDOWN:
                self.mouse1 = pg.mouse.get_pos()
                self.change = True
            if event.type == pg.MOUSEMOTION:
                if self.change:
                    self.mouse2 = pg.mouse.get_pos()
                    diff = subtract(self.mouse2, self.mouse1)
                    self.offset = add_up(self.offset, diff)
                    self.mouse1 = self.mouse2
            if event.type == pg.MOUSEBUTTONUP:
                self.change = False

                if event.button == 4:
                    self.line_size += 1
                elif event.button == 5:
                    self.line_size -= 1

                self.display(True)


            if event.type == pg.MOUSEWHEEL:
                print(event)
