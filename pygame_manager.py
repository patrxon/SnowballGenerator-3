import pygame as pg
import sys

from snowball_drawer import SnowballDrawer

lines = {(1, 1): "n", (1, 0): "j", (2, 0): "n", (3, 1): "n"}


class MainManager:
    def __init__(self, fps, size):
        pg.init()
        self.size = size
        self.win = pg.display.set_mode(self.size)
        self.fps = fps

        self.sbDrawer = SnowballDrawer(100, 100, 1080, 520, self.win)

        self.work_loop()

    def work_loop(self):
        clock = pg.time.Clock()

        while True:
            self.display()
            self.events()
            self.update()
            clock.tick(self.fps)

    def update(self):
        pass

    def display(self):
        self.sbDrawer.draw_box()
        self.sbDrawer.draw_lines((500, 500), lines, 10)
        pg.display.flip()

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
