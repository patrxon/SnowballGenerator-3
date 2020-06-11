import pygame as pg
import sys

from snowball_drawer import SnowballDrawer
from line_manager import LineManager

class MainManager:
    def __init__(self, fps, size):
        pg.init()
        self.size = size
        self.win = pg.display.set_mode(self.size)
        self.fps = fps

        self.sbDrawer = SnowballDrawer(100, 100, 1080, 520, self.win)
        self.lnManager = LineManager()

        self.lnManager.add_line((0, 0), (0, 1), ["l", "r", "r", "r", "r", "r"])
        self.lnManager.add_line((4, 4), (4, 5), ["l", "r", "r", "r", "r", "r", "r"])
        self.lnManager.add_line((8, 8), (8, 7), ["r", "l", "l", "l", "l", "l"])
        self.lnManager.add_line((-4, 4), (-5, 5), ["r", "l", "l", "l", "l", "l"])
        self.lines = self.lnManager.get_lines()

        self.work_loop()

    def work_loop(self):
        clock = pg.time.Clock()

        while True:
            self.display()
            self.events()
            self.update()
            clock.tick(self.fps)
            clock.tick(60)

    def update(self):
        self.lnManager.iterate_lines()

    def display(self):
        self.sbDrawer.draw_box()
        for line in self.lines:
            self.sbDrawer.draw_lines((600, 400), line, 10)
        pg.display.flip()

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
